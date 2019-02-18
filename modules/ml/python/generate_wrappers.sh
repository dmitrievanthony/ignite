#!/bin/bash

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

for_file() {
    echo $1 | sed -e "s/.*\.\(.*\)/\1/g" | xargs -I{} echo "{} = $1" >> $2
}

export -f for_file

for_dir() {
    mkdir -p ../../../python/ignite_ml/$1
    echo '# Licensed to the Apache Software Foundation (ASF) under one or more' > ../../../python/ignite_ml/$1/__init__.py
    echo '# contributor license agreements.  See the NOTICE file distributed with' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# this work for additional information regarding copyright ownership.' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# The ASF licenses this file to You under the Apache License, Version 2.0' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# (the "License"); you may not use this file except in compliance with' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# the License.  You may obtain a copy of the License at' >> ../../../python/ignite_ml/$1/__init__.py
    echo '#' >> ../../../python/ignite_ml/$1/__init__.py
    echo '#      http://www.apache.org/licenses/LICENSE-2.0' >> ../../../python/ignite_ml/$1/__init__.py
    echo '#' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# Unless required by applicable law or agreed to in writing, software' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# distributed under the License is distributed on an "AS IS" BASIS,' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# See the License for the specific language governing permissions and' >> ../../../python/ignite_ml/$1/__init__.py
    echo '# limitations under the License.' >> ../../../python/ignite_ml/$1/__init__.py
    echo "" >> ../../../python/ignite_ml/$1/__init__.py
    echo "from ignite_ml import gateway" >> ../../../python/ignite_ml/$1/__init__.py
    echo "" >> ../../../python/ignite_ml/$1/__init__.py
    ls $1 | grep java | grep -v - | xargs -I{} echo $1/{} | sed -e 's/\//./g' | sed -e "s/.java$//g" | sed -e "s/\(.*\)/gateway.jvm.\1/g" | xargs -I{} bash -c "for_file {} ../../../python/ignite_ml/$1/__init__.py"
    git add ../../../python/ignite_ml/$1/__init__.py
}

export -f for_dir

cd ../src/main/java/
find . -type d -printf '%P\n' | xargs -I{} bash -c 'for_dir {}'
