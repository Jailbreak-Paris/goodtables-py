# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import json

# Module API

from .inspector import Inspector
from .registry import preset, check
from .validate import validate, init_datapackage
from . import spec
from .error import Error
from . import exceptions

# Version

import io
import os
__version__ = io.open(
    os.path.join(os.path.dirname(__file__), 'VERSION'),
    encoding='utf-8').read().strip()

# Register

import importlib
import importlib.util
from . import config


def init(spec_path=None):
    spec.spec = load_spec(spec_path)  # Overwrite in goodtables.spec module
    for module in config.PRESETS:
        importlib.import_module(module)
    for module in config.CHECKS:
        importlib.import_module(module)


def load_check_from_module(path):
    module_name = os.path.splitext(os.path.basename(path))[0]
    module_spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)


def load_checks_from_dir(checks_dir):
    """Dynamically append contrib checks list"""
    for name in os.listdir(checks_dir):
        if not name.endswith('.py') or name == '__init__.py':
            continue
        path = os.path.join(checks_dir, name)
        load_check_from_module(path)


def load_spec(path=None):
    # spec.json location can be changed using SPEC_LOCATION env variable
    if path is None:
        path = os.path.join(os.path.dirname(__file__), 'spec.json')
    spec = json.load(io.open(path, encoding='utf-8'))
    return spec
