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

FitnessJob = gateway.jvm.org.apache.ignite.ml.genetic.FitnessJob
RouletteWheelSelectionJob = gateway.jvm.org.apache.ignite.ml.genetic.RouletteWheelSelectionJob
CrossOverTask = gateway.jvm.org.apache.ignite.ml.genetic.CrossOverTask
CrossOverJob = gateway.jvm.org.apache.ignite.ml.genetic.CrossOverJob
TruncateSelectionJob = gateway.jvm.org.apache.ignite.ml.genetic.TruncateSelectionJob
MutateTask = gateway.jvm.org.apache.ignite.ml.genetic.MutateTask
RouletteWheelSelectionTask = gateway.jvm.org.apache.ignite.ml.genetic.RouletteWheelSelectionTask
GAGrid = gateway.jvm.org.apache.ignite.ml.genetic.GAGrid
Chromosome = gateway.jvm.org.apache.ignite.ml.genetic.Chromosome
IFitnessFunction = gateway.jvm.org.apache.ignite.ml.genetic.IFitnessFunction
Gene = gateway.jvm.org.apache.ignite.ml.genetic.Gene
TruncateSelectionTask = gateway.jvm.org.apache.ignite.ml.genetic.TruncateSelectionTask
FitnessTask = gateway.jvm.org.apache.ignite.ml.genetic.FitnessTask
MutateJob = gateway.jvm.org.apache.ignite.ml.genetic.MutateJob
