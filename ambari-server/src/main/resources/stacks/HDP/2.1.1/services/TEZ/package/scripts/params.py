#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *

# server configurations
config = Script.get_config()

conf_dir = "/etc/tez/conf"
pid_dir = default('/configurations/global/tez_pid_dir', '/var/run/hadoop-tez/')
log_dir = default('/configurations/global/tez_log_dir', '/var/log/hadoop-tez/')

hadoop_home = '/usr'
java64_home = config['hostLevelParams']['java_home']

tez_user = 'tez'
user_group = config['configurations']['global']['user_group']