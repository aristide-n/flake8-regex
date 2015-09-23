# flake8-regex
Searches for regex patterns provided in a configuration file

## Usage

These steps are tested using Mac OSX 10.10.5 and python 3.4.2

1- Get flake8 and flake8-regex:

```
pip install flake8 flake8-regex
```

2- Create a config module such as

**file**: your_config_module.py

```
import re

rules = [
    {
        'regex': re.compile(r"""(^simple.*|
                                 ^pattern.*)""", re.X),
        'code': '100',  # Any 3 digit code, 'R' namespace will be prefixed to that in the report
        'message': "neither 'simple' nor 'pattern' are allowed at the beginning of a line",
    },
]

```
**Important note**: The config file can be named anything, but the list MUST be named `rules`

3- Set a FLAKE8_REGEX_CONFIG_MODULE environment variable

```
export FLAKE8_REGEX_CONFIG_MODULE=absolute.path.to.your_config_module
```

4- run it!

For example:

**for file**: code.py

```
simple = "foo"
pattern = "bar"
good = None
```

```
flake8 code.py

code.py:1:1: R100 neither 'simple' nor 'pattern' are allowed at the beginning of a line
code.py:2:1: R100 neither 'simple' nor 'pattern' are allowed at the beginning of a line
```

## Known issues

The current implementation only reports the first item in the list of rules that matches the line
evaluated. In the future all matching items will be reported.
