__version__ = '0.3'

import importlib
import os
import sys
import pep8

sys.path.append(os.getcwd())
CONFIG_MODULE = os.environ.get("FLAKE8_REGEX_CONFIG_MODULE")

PATTERNS_CONFIG = (getattr(importlib.import_module(CONFIG_MODULE), 'rules')
                   if CONFIG_MODULE else None)


def check_regex_patterns(physical_line):
    if PATTERNS_CONFIG:
        if pep8.noqa(physical_line):
            return

        for pattern_cfg in PATTERNS_CONFIG:
            match = pattern_cfg['regex'].search(physical_line)
            if match:
                return (match.start(),
                        str.format('R{} {}', pattern_cfg['code'], pattern_cfg['message']))


check_regex_patterns.name = name = 'flake8-regex'
check_regex_patterns.version = __version__
