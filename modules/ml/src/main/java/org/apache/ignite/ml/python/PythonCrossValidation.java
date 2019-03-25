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
import org.apache.ignite.Ignition;
import org.apache.ignite.ml.IgniteModel;
import org.apache.ignite.ml.math.primitives.vector.Vector;
import org.apache.ignite.ml.math.primitives.vector.VectorUtils;
import org.apache.ignite.ml.selection.cv.CrossValidation;
import org.apache.ignite.ml.selection.scoring.metric.Metric;
import org.apache.ignite.ml.trainers.SingleLabelDatasetTrainer;

public class PythonCrossValidation {

    public static <M extends IgniteModel<Vector, Double>> double[] score(SingleLabelDatasetTrainer<M> trainer, Metric<Double> metric,
        IgniteCache<Integer, double[]> cache, int cv) {
        CrossValidation<M, Double, Integer, double[]> crossValidation = new CrossValidation<>();

        double[] res = crossValidation.score(
            trainer,
            metric,
            Ignition.ignite(),
            cache,
            (Integer k, double[] v) -> VectorUtils.of(Arrays.copyOf(v, v.length - 1)),
            (Integer k, double[] v) -> v[v.length - 1],
            cv
        );

        System.out.println("Res : " + Arrays.toString(res));

        return res;
    }
}
