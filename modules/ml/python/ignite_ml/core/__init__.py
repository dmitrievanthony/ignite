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

"""Ignite cache API.
"""

from ..common import Proxy
from ..common import Utils

from ..common import gateway

import pandas as pd
import numpy as np

class Ignite:
 
    def __init__(self, cfg=None):
        """Constructs a new instance of Ignite.

        Parameters
        ----------
        cfg : Configuration.
        """
        self.cfg = cfg
   
    def get_cache(self, name):
        """Returns existing cache by name.

        Parameters
        ----------
        name : Cache name.
        """
        if self.ignite is None:
            raise Exception("Use Ignite() inside with.. as.. command.")
        java_cache = self.ignite.cache(name)
        return Cache(java_cache)

    def create_cache(self, name, excl_neighbors=False, parts=10):
        """Creates a new cache.

        Parameters
        ----------
        name : Cache name.
        excl_neighbors : Exclude neighbours.
        parts : Number of partitions.
        """
        if self.ignite is None:
            raise Exception("Use Ignite() inside with.. as.. command.")
        affinity = gateway.jvm.org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction(excl_neighbors, parts)
        cc = gateway.jvm.org.apache.ignite.configuration.CacheConfiguration()
        cc.setName(name)
        cc.setAffinity(affinity)
        java_cache = self.ignite.createCache(cc)
        return Cache(java_cache)

    def __enter__(self):
        if self.cfg is not None:
            self.ignite = gateway.jvm.org.apache.ignite.Ignition.start(self.cfg)
        else:
            self.ignite = gateway.jvm.org.apache.ignite.Ignition.start()
        return self

    def __exit__(self, t, v, trace):
        if self.ignite is not None:
            self.ignite.close()

class Cache(Proxy):
    """Ignite cache proxy.
    """
    def __init__(self, proxy, cache_filter=None, preprocessor=None):
        """Constructs a new instance of Ignite cache proxy.

        Parameters
        ----------
        proxy : Cache (proxy object).
        cache_filter : Cache filter.
        preprocessor : Preprocessor.
        """
        Proxy.__init__(self, proxy)

        self.cache_filter = cache_filter
        self.preprocessor = preprocessor

    def __delitem__(self, key):
        raise Exception("Not implemented!")

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.get(key)
        elif isinstance(key, slice):
            result = []
            length = len(self)
            for k in range(*key.indices(length)):
                result.append(self.get(k))
            return np.array(result)
        else:
            raise Exception("Unexpected type of key (%s)." % type(key))

    def __setitem__(self, key, value):
        raise Exception("Not implemented!")

    def get(self, key):
        """Returns value (float array) by key.

        Parameters
        ----------
        key : Key.
        """
        java_array = self.proxy.get(key)
        return Utils.from_java_double_array(java_array)

    def put(self, key, value):
        """Puts value (float array) by key.

        Parameters
        ----------
        key : Key.
        value : Value.
        """
        value = Utils.to_java_double_array(value)
        self.proxy.put(key, value)

    def head(self, n=5):
        scan_query = gateway.jvm.org.apache.ignite.cache.query.ScanQuery()
        
        if self.cache_filter is not None:
            scan_query.setFilter(self.cache_filter)

        cursor = self.proxy.query(scan_query)
        iterator = cursor.iterator()
        
        data = []
        while iterator.hasNext() and n != 0:
            entry = iterator.next()
            key = entry.getKey()
            value = entry.getValue()

            if self.preprocessor is not None:
                initial_array = Utils.from_java_double_array(value)
                preprocessed_value = self.preprocessor.proxy.apply(key, value)
                value = preprocessed_value.asArray()
                array = Utils.from_java_double_array(value)
                array = np.hstack((array, initial_array[-1]))
            else:
                array = Utils.from_java_double_array(value)
    
            data.append(array)
            n = n - 1

        return pd.DataFrame(data)

    def transform(self, preprocessor):
        return Cache(self.proxy, self.cache_filter, preprocessor)

    def filter(self, cache_filter):
        return Cache(self.proxy, cache_filter, self.preprocessor)

    def __len__(self):
        return self.proxy.size(gateway.new_array(gateway.jvm.org.apache.ignite.cache.CachePeekMode, 0))
