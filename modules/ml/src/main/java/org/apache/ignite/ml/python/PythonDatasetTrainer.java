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
import org.apache.ignite.ml.IgniteModel;
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.math.primitives.vector.VectorUtils;
import org.apache.ignite.ml.structures.LabeledVector;
import org.apache.ignite.ml.trainers.SingleLabelDatasetTrainer;

/**
 * Python wrapper for {@link SingleLabelDatasetTrainer}.
 *
 * @param <M> Type of a model.
 */
public class PythonDatasetTrainer<M extends IgniteModel> {
    /** Delegate. */
    private final SingleLabelDatasetTrainer<M> delegate;

    /**
     * Constructs a new instance of Python dataset trainer.
     *
     * @param delegate Delegate.
     */
    public PythonDatasetTrainer(SingleLabelDatasetTrainer<M> delegate) {
        this.delegate = delegate;
    }

    /**
     * Trains model on local data.
     *
     * @param x X (features).
     * @param y Y (labels).
     * @param preprocessor Preprocessor.
     * @return Model.
     */
    public M fit(double[][] x, double[] y, IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        Map<Integer, LabeledVector<Double>> data = new HashMap<>();

        for (int i = 0; i < x.length; i++)
            data.put(i, new LabeledVector<>(VectorUtils.of(x[i]), y[i]));

        if (preprocessor != null)
            return delegate.fit(data, 1, (k, v) -> preprocessor.apply(k, v.features().asArray()), (k, v) -> v.label());

        return delegate.fit(data, 1, (k, v) -> v.features(), (k, v) -> v.label());
    }

    /**
     * Trains model of cached data.
     *
     * @param cache Ignite cache.
     * @param preprocessor Preprocessor.
     * @return MOdel.
     */
    public M fitOnCache(IgniteCache<Integer, double[]> cache,
        IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        if (preprocessor != null)
            return delegate.fit(
                Ignition.ignite(),
                cache,
                (k, v) -> preprocessor.apply(k, Arrays.copyOfRange(v, 0, v.length - 1)),
                (k, v) -> v[v.length - 1]
            );

        return delegate.fit(
            Ignition.ignite(),
            cache,
            (k, v) -> VectorUtils.of(Arrays.copyOfRange(v, 0, v.length - 1)),
            (k, v) -> v[v.length - 1]
        );
    }
}
