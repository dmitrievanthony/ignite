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

from ..common import SupervisedTrainer
from ..common import Proxy
from ..common import Utils
from ..common import LearningEnvironmentBuilder

from ..common import gateway

from ..core import Cache
from ..model_selection import CacheView

__evaluator = gateway.jvm.org.apache.ignite.ml.python.PythonEvaluator

def accuracy_score(cache, mdl, preprocessor=None):
    """Calculate accuracy score.

    Parameters
    ----------
    cache : Cache or cache view (cache with filter).
    mdl : Model.
    preprocessor : Preprocessor.
    """
    if isinstance(cache, Cache):
        return __evaluator.accuracy(cache.proxy, None, mdl.proxy, preprocessor)
    elif isinstance(cache, CacheView):
        return __evaluator.accuracy(cache.cache.proxy, cache.cache_filter, mdl.proxy, preprocessor)
    else:
        raise Exception("Cache type is unknown, it should be Cache or CacheView.")

def rmse(cache, mdl, preprocessor=None):
    if isinstance(cache, Cache):
        return __evaluator.rmse(cache.proxy, None, mdl.proxy, preprocessor)
    elif isinstance(cache, CacheView):
        return __evaluator.rmse(cache.cache.proxy, cache.cache_filter, mdl.proxy, preprocessor)
    else:
        raise Exception("Cache type is unknown, it should be Cache or CacheView.")
