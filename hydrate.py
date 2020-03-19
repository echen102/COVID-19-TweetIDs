#!/usr/bin/env python3

#
# This script will walk through all the tweet id files and
# hydrate them with twarc. The line oriented JSON files will
# be placed right next to each tweet id file.
#
# Note: you will need to install twarc, and run twarc configure
# from the command line to tell it your Twitter API keys.
#

import gzip
import json

from twarc import Twarc
from pathlib import Path

twarc = Twarc()
data_dirs = ['2020-03']

def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('.txt'):
                hydrate(path)

def hydrate(id_file):
    print('hydrating {}'.format(id_file))

    gzip_path = id_file.with_suffix('.jsonl.gz')
    if gzip_path.is_file():
        print('skipping json file already exists: {}'.format(gzip_path))
        return

    with gzip.open(gzip_path, 'w') as output:
        for tweet in twarc.hydrate(id_file.open()):
            output.write(json.dumps(tweet).encode('utf8') + b"\n")

if __name__ == "__main__":
    main()
