# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ignite_ml import gateway

UnknownClassLabelException = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.UnknownClassLabelException
Recall = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.Recall
Precision = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.Precision
ClassMetric = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.ClassMetric
BinaryClassificationMetricValues = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.BinaryClassificationMetricValues
Metric = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.Metric
Fmeasure = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.Fmeasure
Accuracy = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.Accuracy
BinaryClassificationMetrics = gateway.jvm.org.apache.ignite.ml.selection.scoring.metric.BinaryClassificationMetrics
