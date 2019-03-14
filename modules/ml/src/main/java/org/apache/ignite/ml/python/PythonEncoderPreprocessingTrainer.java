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
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.preprocessing.encoding.EncoderTrainer;

/**
 * Python wrapper for {@link EncoderTrainer}.
 */
public class PythonEncoderPreprocessingTrainer {
    /** Delegate. */
    private final EncoderTrainer<Integer, Object[]> delegate;

    /**
     * Constructs a new instance of Python encoder preprocessing trainer.
     *
     * @param delegate Delegate.
     */
    public PythonEncoderPreprocessingTrainer(EncoderTrainer<Integer, Object[]> delegate) {
        this.delegate = delegate;
    }

    /**
     * Trains preprocessor of local data.
     *
     * @param x X (features).
     * @return Preprocessor.
     */
    public IgniteBiFunction<Integer, Object[], Vector> fit(double[][] x) {
        Map<Integer, Object[]> data = new HashMap<>();
        for (int i = 0; i < x.length; i++) {
            Object[] arr = new Object[x[i].length];
            for (int j = 0; j < x[i].length; j++)
                arr[j] = x[i][j];
            data.put(i, arr);
        }

        return delegate.fit(data, 1, (k, v) -> v);
    }
}
