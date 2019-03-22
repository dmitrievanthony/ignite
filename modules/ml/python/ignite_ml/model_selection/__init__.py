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
# limitations under the License

from ..core import Cache
from ..common import gateway

def train_test_split(cache, test_size=0.25, train_size=0.75, random_state=None):
	"""Splits given cache on two parts: test and train with given sizes.
	"""
    if not isinstance(cache, Cache):
        raise Exception("Unexpected type of cache (%s)." % type(cache))    

    split = gateway.jvm.org.apache.ignite.ml.selection.split.TrainTestDatasetSplitter().split(train_size, test_size)
    train_filter = split.getTrainFilter()
    test_filter = split.getTestFilter()
    return (cache.filter(train_filter), cache.filter(test_filter))
