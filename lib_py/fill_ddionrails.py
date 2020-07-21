# -*- coding: utf-8 -*-
#!/usr/bin/env python3
""" Custom pre-processing pipeline for TwinLife """

import shutil

import pandas as pd
from ddi.onrails.repos import dor1, merge_instruments

from convert_r2ddi import Parser

STUDY = "twinlife"
VERSION = "v3-0-0"


def main():

    # operations from ddi.py
    dor1.variables()
    merge_instruments.main()
    Parser(STUDY, version=VERSION).write_json()


if __name__ == "__main__":
    main()
