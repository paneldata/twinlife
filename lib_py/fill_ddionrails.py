# -*- coding: utf-8 -*-
#!/usr/bin/env python3
""" Custom pre-processing pipeline for TwinLife """

import shutil

import pandas as pd
from ddi.onrails.repos import dor1, merge_instruments

from convert_r2ddi import Parser

STUDY = "twinlife"
VERSION = "v3-0-0"


def questions_variables():

    questions_variables = pd.read_csv("metadata/logical_variables.csv")
    questions_variables.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "variable": "variable_name",
            "questionnaire": "instrument_name",
            "question": "question_name",
        },
        inplace=True,
    )
    questions_variables = questions_variables[
        [
            "study_name",
            "dataset_name",
            "variable_name",
            "instrument_name",
            "question_name",
        ]
    ]

    questions_variables.dropna(axis=0, how="any", inplace=True)
    questions_variables.drop_duplicates(inplace=True)
    questions_variables.to_csv("ddionrails/questions_variables.csv", index=False)


def main():
    # simple copy operations
    shutil.copy("metadata/study.md", "ddionrails/study.md")
    shutil.copy("metadata/analysis_units.csv", "ddionrails/analysis_units.csv")
    shutil.copy(
        "metadata/conceptual_datasets.csv", "ddionrails/conceptual_datasets.csv"
    )
    shutil.copy("metadata/periods.csv", "ddionrails/periods.csv")
    shutil.copy("metadata/datasets.csv", "ddionrails/datasets.csv")

    # custom operation
    questions_variables()

    # operations from ddi.py
    dor1.variables()
    merge_instruments.main()
    Parser(STUDY, version=VERSION).write_json()


if __name__ == "__main__":
    main()
