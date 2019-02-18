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

DatasetBuilder = gateway.jvm.org.apache.ignite.ml.dataset.DatasetBuilder
DatasetFactory = gateway.jvm.org.apache.ignite.ml.dataset.DatasetFactory
Dataset = gateway.jvm.org.apache.ignite.ml.dataset.Dataset
PartitionContextBuilder = gateway.jvm.org.apache.ignite.ml.dataset.PartitionContextBuilder
PartitionDataBuilder = gateway.jvm.org.apache.ignite.ml.dataset.PartitionDataBuilder
UpstreamEntry = gateway.jvm.org.apache.ignite.ml.dataset.UpstreamEntry
UpstreamTransformerBuilder = gateway.jvm.org.apache.ignite.ml.dataset.UpstreamTransformerBuilder
UpstreamTransformer = gateway.jvm.org.apache.ignite.ml.dataset.UpstreamTransformer
