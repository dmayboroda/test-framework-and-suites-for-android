#!/usr/bin/env python
"""
Copyright (C) 2018 Intel Corporation
?
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
?
http://www.apache.org/licenses/LICENSE-2.0
?
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions
and limitations under the License.
?

SPDX-License-Identifier: Apache-2.0
"""
# Used defined libraries
from testlib.base.base_utils import parse_args
from testlib.scripts.android.ui import ui_steps

# ############# Get parameters ############
args = parse_args()

# Setup
ui_steps.press_home(serial=args["serial"])()

# Run
ui_steps.enable_options_from_developer_options(serial=args["serial"],
                                               developer_options=["Show surface updates"])()
ui_steps.disable_options_from_developer_options(serial=args["serial"],
                                                developer_options=["Show surface updates"],
                                                enabled=True)()
