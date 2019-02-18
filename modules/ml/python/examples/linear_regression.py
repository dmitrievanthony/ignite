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

import ignite_ml
from ignite_ml.org.apache.ignite.ml.regressions.linear import LinearRegressionLSQRTrainer
from ignite_ml.org.apache.ignite.ml.util import SandboxMLCache
from ignite_ml.org.apache.ignite.ml.util import MLSandboxDatasets
from ignite_ml.org.apache.ignite import Ignition
from ignite_ml.org.apache.ignite.cache.query import ScanQuery

# Get instance of Apache Ignite.
ignite = Ignition.ignite()

# Create and fill cache with data.
dataCache = SandboxMLCache(ignite).fillCacheWith(MLSandboxDatasets.MORTALITY_DATA)

# Create linear regression trainer.
trainer = LinearRegressionLSQRTrainer()

# Training linear regression model.
mdl = trainer.fit(
    ignite,
    dataCache,
    ignite_ml.IgniteBiFunction(lambda k, v: v.copyOfRange(1, v.size())),
    ignite_ml.IgniteBiFunction(lambda k, v: v.get(0))
)

print('Prediction\tTruth')
print()

# Iterating and makeing predictions.
cursor = dataCache.query(ScanQuery())
iterator = cursor.iterator()
while iterator.hasNext():
    row = iterator.next()
    val = row.getValue()
    prediction = mdl.predict(val.copyOfRange(1, val.size()))
    print('%f\t%f' % (prediction, val.get(0)))