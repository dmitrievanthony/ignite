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

class Ignite:
 
    def __init__(self, cfg=None):
        """Constructs a new instance of Ignite.

        Parameters
        ----------
        cfg : Configuration.
        """
        self.cfg = cfg
   
    def getCache(self, name):
        """Returns existing cache by name.

        Parameters
        ----------
        name : Cache name.
        """
        if self.ignite is None:
            raise Exception("Use Ignite() inside with.. as.. command.")
        java_cache = self.ignite.cache(name)
        return Cache(java_cache)

    def createCache(self, name, excl_neighbors=False, parts=10):
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
    def __init__(self, proxy):
        """Constructs a new instance of Ignite cache proxy.

        Parameters
        ----------
        proxy : Proxy object.
        """
        Proxy.__init__(self, proxy)

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

    def size(self):
        """Returns size of the cache.
        """
        return self.proxy.size()
