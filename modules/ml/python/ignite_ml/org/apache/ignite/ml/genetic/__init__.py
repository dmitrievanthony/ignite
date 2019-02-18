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

Chromosome = gateway.jvm.org.apache.ignite.ml.genetic.Chromosome
CrossOverJob = gateway.jvm.org.apache.ignite.ml.genetic.CrossOverJob
CrossOverTask = gateway.jvm.org.apache.ignite.ml.genetic.CrossOverTask
FitnessJob = gateway.jvm.org.apache.ignite.ml.genetic.FitnessJob
FitnessTask = gateway.jvm.org.apache.ignite.ml.genetic.FitnessTask
GAGrid = gateway.jvm.org.apache.ignite.ml.genetic.GAGrid
Gene = gateway.jvm.org.apache.ignite.ml.genetic.Gene
IFitnessFunction = gateway.jvm.org.apache.ignite.ml.genetic.IFitnessFunction
MutateJob = gateway.jvm.org.apache.ignite.ml.genetic.MutateJob
MutateTask = gateway.jvm.org.apache.ignite.ml.genetic.MutateTask
RouletteWheelSelectionJob = gateway.jvm.org.apache.ignite.ml.genetic.RouletteWheelSelectionJob
RouletteWheelSelectionTask = gateway.jvm.org.apache.ignite.ml.genetic.RouletteWheelSelectionTask
TruncateSelectionJob = gateway.jvm.org.apache.ignite.ml.genetic.TruncateSelectionJob
TruncateSelectionTask = gateway.jvm.org.apache.ignite.ml.genetic.TruncateSelectionTask
