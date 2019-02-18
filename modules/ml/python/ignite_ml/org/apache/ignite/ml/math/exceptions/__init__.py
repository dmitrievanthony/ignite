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

CardinalityException = gateway.jvm.org.apache.ignite.ml.math.exceptions.CardinalityException
ColumnIndexException = gateway.jvm.org.apache.ignite.ml.math.exceptions.ColumnIndexException
IndexException = gateway.jvm.org.apache.ignite.ml.math.exceptions.IndexException
MathIllegalArgumentException = gateway.jvm.org.apache.ignite.ml.math.exceptions.MathIllegalArgumentException
MathRuntimeException = gateway.jvm.org.apache.ignite.ml.math.exceptions.MathRuntimeException
NoDataException = gateway.jvm.org.apache.ignite.ml.math.exceptions.NoDataException
NonSquareMatrixException = gateway.jvm.org.apache.ignite.ml.math.exceptions.NonSquareMatrixException
RowIndexException = gateway.jvm.org.apache.ignite.ml.math.exceptions.RowIndexException
SingularMatrixException = gateway.jvm.org.apache.ignite.ml.math.exceptions.SingularMatrixException
UnsupportedOperationException = gateway.jvm.org.apache.ignite.ml.math.exceptions.UnsupportedOperationException
