# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import json


# Internal

def _load_spec():
    # spec.json location can be changed using SPEC_LOCATION env variable
    env_spec_path = os.environ.get('SPEC_LOCATION')
    path = env_spec_path if env_spec_path \
        else os.path.join(os.path.dirname(__file__), 'spec.json')
    spec = json.load(io.open(path, encoding='utf-8'))
    return spec


# Module API

spec = _load_spec()
