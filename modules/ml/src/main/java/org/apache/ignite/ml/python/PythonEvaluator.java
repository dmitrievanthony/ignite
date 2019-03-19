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
import java.util.Iterator;
import javax.cache.Cache;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.cache.query.QueryCursor;
import org.apache.ignite.cache.query.ScanQuery;
import org.apache.ignite.lang.IgniteBiPredicate;
import org.apache.ignite.ml.IgniteModel;
import org.apache.ignite.ml.math.functions.IgniteBiFunction;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.math.primitives.vector.VectorUtils;
import org.apache.ignite.ml.selection.scoring.evaluator.Evaluator;
import org.apache.ignite.ml.selection.scoring.metric.classification.BinaryClassificationMetricValues;
import org.apache.ignite.ml.selection.scoring.metric.regression.RegressionMetricValues;
import org.apache.ignite.ml.selection.split.TrainTestDatasetSplitter;
import org.apache.ignite.ml.selection.split.TrainTestSplit;

/**
 * Python wrapper for {@link Evaluator}.
 */
public class PythonEvaluator {

    public static void test() {
        IgniteCache<Integer, double[]> cache = null;
        QueryCursor<Cache.Entry<Integer, double[]>> cursor = cache.query(new ScanQuery<>());
        Iterator<Cache.Entry<Integer, double[]>> iterator = cursor.iterator();

        TrainTestDatasetSplitter<Integer, double[]> splitter = new TrainTestDatasetSplitter<>();
        TrainTestSplit<Integer, double[]> split = splitter.split(0.75);



        while (iterator.hasNext()) {
            Cache.Entry<Integer, double[]> entry = iterator.next();
            double[] value = entry.getValue();
        }
    }

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

    private static IgniteBiFunction<Integer, double[], Vector> getFeatureExtractor(
        IgniteBiFunction<Integer, double[], Vector> preprocessor) {
        if (preprocessor != null)
            return (k, v) -> preprocessor.apply(k, Arrays.copyOf(v, v.length - 1));
        else
            return (k, v) -> VectorUtils.of(Arrays.copyOf(v, v.length - 1));
    }
}
