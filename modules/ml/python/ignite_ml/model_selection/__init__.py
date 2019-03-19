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

import numpy as np
from numbers import Number

from ..core import Cache

from ..common import SupervisedTrainer
from ..common import Proxy
from ..common import Utils
from ..common import LearningEnvironmentBuilder

from ..common import gateway

class CacheView:
    """Cache view (cache with filter).
    """
    def __init__(self, cache, cache_filter):
        """Constructs a new instance of cache view.

        Parameters
        ----------
        cache : Cache or cache view (cache with filter).
        cache_filter : Cache filter.
        """
        self.cache = cache
        self.cache_filter = cache_filter

def train_test_split(cache, test_size=0.25, train_size=0.75, random_state=None):
    split = gateway.jvm.org.apache.ignite.ml.selection.split.TrainTestDatasetSplitter().split(train_size, test_size)
    train_filter = split.getTrainFilter()
    test_filter = split.getTestFilter()
    
    if isinstance(cache, Cache):
        return (CacheView(cache, train_filter), CacheView(cache, test_filter))
    else:
        raise Exception("Not implemented")
