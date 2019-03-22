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
import org.apache.ignite.ml.selection.scoring.metric.classification.BinaryClassificationMetricValues;
import org.apache.ignite.ml.selection.scoring.metric.regression.RegressionMetricValues;

/**
 * Python wrapper for {@link Evaluator}.
 */
public class PythonEvaluator {
    /**
     * Evaluate regression metrics.
     *
     * @param cache Ignite cache.
     * @param filter Filter.
     * @param mdl Model.
     * @param preprocessor Preprocessor.
     * @return Regression metrics.
     */
    public static RegressionMetricValues evaluateRegression(IgniteCache<Integer, double[]> cache,
        IgniteBiPredicate<Integer, double[]> filter,
        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor) {

        return Evaluator.evaluateRegression(
            cache,
            filter != null ? filter : (k, v) -> true,
            mdl,
            getFeatureExtractor(preprocessor),
            (Integer k, double[] v) -> v[v.length - 1]
        );
    }

    /**
     * Evaluate classification metrics.
     *
     * @param cache Ignite cache.
     * @param filter Filter.
     * @param mdl Model.
     * @param preprocessor Preprocessor.
     * @return Classification metrics.
     */
    public static BinaryClassificationMetricValues evaluateClassification(IgniteCache<Integer, double[]> cache,
        IgniteBiPredicate<Integer, double[]> filter,
        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor) {

        return Evaluator.evaluate(
            cache,
            filter != null ? filter : (k, v) -> true,
            mdl,
            getFeatureExtractor(preprocessor),
            (Integer k, double[] v) -> v[v.length - 1]
        );
    }

    /**
     * Builds feature extractor based on preprocessor.
     *
     * @param preprocessor Preprocessor.
     * @return Feature extractor.
     */
    private static IgniteBiFunction<Integer, double[], Vector> getFeatureExtractor(
        IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        if (preprocessor != null)
            return (k, v) -> preprocessor.apply(k, Arrays.copyOf(v, v.length - 1));
        else
            return (k, v) -> VectorUtils.of(Arrays.copyOf(v, v.length - 1));
    }
}
