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

import java.util.HashMap;
import java.util.Map;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.preprocessing.encoding.EncoderTrainer;

/**
 * Python wrapper for {@link EncoderTrainer}.
 */
public class PythonEncoderPreprocessingTrainer {
    /** Delegate. */
    private final EncoderTrainer<Integer, double[]> delegate;

    /**
     * Constructs a new instance of Python encoder preprocessing trainer.
     *
     * @param delegate Delegate.
     */
    public PythonEncoderPreprocessingTrainer(EncoderTrainer<Integer, double[]> delegate) {
        this.delegate = delegate;
    }

    /**
     * Trains preprocessor of local data.
     *
     * @param x X (features).
     * @return Preprocessor.
     */
    public IgniteBiFunction<Integer, double[], Vector> fit(double[][] x) {
        Map<Integer, double[]> data = new HashMap<>();
        for (int i = 0; i < x.length; i++)
            data.put(i, x[i]);

        return delegate.fit(data, 1, (k, v) -> toObject(v));
    }

    /**
     * Trains model on local data.
     *
     * @param cache Ignite cache.
     * @return Model.
     */
    public IgniteBiFunction<Integer, double[], Vector> fitOnCache(IgniteCache<Integer, double[]> cache) {
        return delegate.fit(Ignition.ignite(), cache, (Integer k, double[] v) -> toObject(v));
    }

    private static Object[] toObject(double[] arr) {
        Object[] res = new Double[arr.length];

        for (int i = 0; i < arr.length; i++)
            res[i] = arr[i];

        return res;
    }
}
