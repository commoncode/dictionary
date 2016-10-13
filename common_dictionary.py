#!/usr/bin/env python

import json

DARYLISMS = ['whereas', 'were']

with open('dictionary.json') as f:
    dictionary = json.loads(f.read())
    common_dictionary = {k: v for k, v in dictionary.items() if k.lower().startswith('c') or k.lower() in DARYLISMS}

    with open('common_dictionary.json', 'w') as d:
        d.write(json.dumps(common_dictionary, indent=2))
