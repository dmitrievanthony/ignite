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
import org.apache.ignite.ml.selection.scoring.evaluator.Evaluator;
import org.apache.ignite.ml.selection.scoring.metric.Metric;
import org.apache.ignite.ml.selection.scoring.metric.classification.Accuracy;
import org.apache.ignite.ml.trainers.FeatureLabelExtractor;

public class PythonEvaluator {

//    public static double accuracy(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
//        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor) {
//        return calculate(cache, filter, mdl)
//    }
//
//    private static <L> L calculate(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
//        IgniteModel<Vector, Double> mdl, IgniteBiFunction<Integer, double[], Vector> preprocessor, Metric<L> metric) {
//        return Evaluator.evaluate(
//            cache,
//            mdl,
//            (k, v) -> preprocessor.apply(k, Arrays.copyOfRange(v, 0, v.length - 1)),
//            (k, v) -> v[v.length - 1],
//            new Accuracy<>()
//        );
//    }
//
//    private static <L> L calculate(IgniteCache<Integer, double[]> cache, IgniteBiPredicate<Integer, double[]> filter,
//        IgniteModel<Vector, Double> mdl, FeatureLabelExtractor<Integer, double[], Double> featureLbExtractor) {
//
//    }
}
