/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.ignite.ml.python;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.functions.IgniteDifferentiableVectorToDoubleFunction;
import org.apache.ignite.ml.math.functions.IgniteFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.math.primitives.vector.VectorUtils;
import org.apache.ignite.ml.nn.MLPTrainer;
import org.apache.ignite.ml.nn.MultilayerPerceptron;
import org.apache.ignite.ml.nn.UpdatesStrategy;
import org.apache.ignite.ml.nn.architecture.MLPArchitecture;
import org.apache.ignite.ml.optimization.LossFunctions;
import org.apache.ignite.ml.optimization.updatecalculators.SimpleGDParameterUpdate;
import org.apache.ignite.ml.optimization.updatecalculators.SimpleGDUpdateCalculator;
import org.apache.ignite.ml.structures.LabeledVector;
import org.apache.ignite.ml.trainers.FeatureLabelExtractor;

/**
 * Python wrapper for {@link MLPTrainer}.
 */
public class PythonMLPDatasetTrainer {
    /** Delegate. */
    private final MLPTrainer<SimpleGDParameterUpdate> delegate;

    /**
     * Constructs a new instance of Python MLP dataset trainer.
     *
     * @param arch MLP architecture.
     * @param loss Loss function.
     * @param learningRate Learning rate.
     * @param maxIterations Max number of iterations.
     * @param batchSize Batch size.
     * @param locIterations Number of local iterations.
     * @param seed Seed.
     */
    public PythonMLPDatasetTrainer(MLPArchitecture arch,
        IgniteFunction<Vector, IgniteDifferentiableVectorToDoubleFunction> loss,
        double learningRate, int maxIterations, int batchSize, int locIterations, Long seed) {

        delegate = new MLPTrainer<>(
            arch,
            LossFunctions.MSE,
            new UpdatesStrategy<>(
                new SimpleGDUpdateCalculator(learningRate),
                SimpleGDParameterUpdate::sumLocal,
                SimpleGDParameterUpdate::avg
            ),
            maxIterations,
            batchSize,
            locIterations,
            seed == null ? System.currentTimeMillis() : seed
        );
    }

    /**
     * Trains model of local data.
     *
     * @param x X (features).
     * @param y Y (labels).
     * @param preprocessor Preprocessor.
     * @return Model.
     */
    public MultilayerPerceptron fit(double[][] x, double[][] y,
        IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        Map<Integer, LabeledVector<double[]>> data = new HashMap<>();

        for (int i = 0; i < x.length; i++)
            data.put(i, new LabeledVector<>(VectorUtils.of(x[i]), y[i]));

        if (preprocessor != null)
            return delegate.fit(
                data,
                1,
                (k, v) -> preprocessor.apply(k, v.features().asArray()),
                (k, v) -> v.label()
            );

        return delegate.fit(
            data,
            1,
            (k, v) -> v.features(),
            (k, v) -> v.label()
        );
    }

    /**
     * Trains model of cached data.
     *
     * @param cache Ignite cache.
     * @param preprocessor Preprocessor.
     * @return Model.
     */
    public MultilayerPerceptron fitOnCache(IgniteCache<Integer, double[]> cache,
        IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        if (preprocessor != null)
            return delegate.fit(
                Ignition.ignite(),
                cache,
                (k, v) -> new LabeledVector<>(
                    VectorUtils.of(Arrays.copyOfRange(v, 0, v.length - 1)),
                    new double[] {v[v.length - 1]}
                )
            );

        return delegate.fit(
            Ignition.ignite(),
            cache,
            (k, v) -> new LabeledVector<>(
                VectorUtils.of(Arrays.copyOfRange(v, 0, v.length - 1)),
                new double[] {v[v.length - 1]}
            )
        );
    }
}
