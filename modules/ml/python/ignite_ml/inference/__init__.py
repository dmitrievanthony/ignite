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

"""Ignite inference functionality.
"""

from ..common import Proxy
from ..common import Utils

from ..common import gateway
from copy import copy

class IgniteModel:
    """Constructs a new instance of Ignite model (local).

    Parameters
    ----------
    mdl : Model.
    """
    def __init__(self, mdl):
        self.mdl = mdl

    def predict(self, X):
        """Predict.

        Parameters
        ----------
        X : Features.
        """
        return self.mdl.predict(X)

class IgniteDistributedModel:
    """Ignite distributed model.

    Parameters
    ----------
    ignite : Ignite instance.
    mdl : Model.
    instances : Number of instances.
    max_per_node : Max number of instance per node.
    """
    def __init__(self, ignite, mdl, instances=1, max_per_node=1):
        """Constructs a new instance of Ignite distributed model.

        Parameters
        ----------
        ignite : Ignite instance.
        reader : Model reader.
        parser : Model parser.
        instances : Number of worker instances.
        max_per_node : Max number of worker instances per ignite node.
        """
        self.ignite = ignite
        self.mdl = mdl

        if isinstance(mdl.proxy, list):
            self.reader = [gateway.jvm.org.apache.ignite.ml.inference.reader.InMemoryModelReader(p) for p in mdl.proxy]
        else:
            self.reader = [gateway.jvm.org.apache.ignite.ml.inference.reader.InMemoryModelReader(mdl.proxy)]

        self.parser = gateway.jvm.org.apache.ignite.ml.inference.parser.IgniteModelParser()
        self.instances = instances
        self.max_per_node = max_per_node

    def predict(self, X):
        """Predict.

        Parameters
        ----------
        X : Features.
        """
        if self.proxy is None:
            raise Exception("Use IgniteDistributedModel() inside with.. as.. command.")
        mdl = copy(self.mdl)
        if isinstance(mdl.proxy, list):
            mdl.proxy = self.proxy
        else:
            mdl.proxy = self.proxy[0]
        return mdl.predict(X)

    def __enter__(self):
        self.proxy = [gateway.jvm.org.apache.ignite.ml.inference.builder.IgniteDistributedModelBuilder(
            self.ignite.ignite, 
            self.instances, 
            self.max_per_node
        ).build(r, self.parser) for r in self.reader]
        return self

    def __exit__(self, t, v, trace):
        if self.proxy is not None:
            for p in self.proxy:
                p.close()
            self.proxy = None
        return False
