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

from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
gateway.start_callback_server()

class IgniteBiFunction:
    def __init__(self, lambda_function):
        self.gateway = gateway
        self.lambda_function = lambda_function

    def apply(self, a, b):
        return self.lambda_function(a, b)

    def andThen(self, after):
        return IgniteBiFunction(lambda k, v: after.apply(self.apply(k, v)))

    class Java:
        implements = ["org.apache.ignite.ml.math.functions.IgniteBiFunction"]

