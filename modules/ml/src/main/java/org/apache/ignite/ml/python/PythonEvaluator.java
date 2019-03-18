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
import org.apache.ignite.IgniteCache;
import org.apache.ignite.lang.IgniteBiPredicate;
import org.apache.ignite.ml.IgniteModel;
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.math.primitives.vector.VectorUtils;
import org.apache.ignite.ml.selection.scoring.evaluator.Evaluator;
import org.apache.ignite.ml.selection.scoring.metric.Metric;
import org.apache.ignite.ml.selection.scoring.metric.classification.Accuracy;
import org.apache.ignite.ml.selection.scoring.metric.regression.RegressionMetrics;

public class PythonEvaluator {

    public static double accuracy(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        return calculate(cache, filter, mdl, preprocessor, new Accuracy<>());
    }

    public static double rmse(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        return calculate(cache, filter, mdl, preprocessor, new RegressionMetrics());
    }

    private static double calculate(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor, Metric<Double> metric) {

        IgniteBiFunction<Integer, double[], Vector> featureExtractor;

        if (preprocessor != null)
            featureExtractor = (k, v) -> preprocessor.apply(k, Arrays.copyOfRange(v, 0, v.length - 1));
        else
            featureExtractor = (k, v) -> VectorUtils.of(Arrays.copyOfRange(v, 0, v.length - 1));

        return Evaluator.evaluate(
            cache,
            filter != null ? filter : (k, v) -> true,
            mdl,
            featureExtractor,
            (Integer k, double[] v) -> v[v.length - 1],
            metric
        );
    }
}
