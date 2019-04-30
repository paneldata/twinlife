import os, sys
import pandas as pd

# sys.path.append(os.path.expanduser("~/github/ddi.py/"))
sys.path.append(os.path.expanduser("~/projects/ddionrails/ddi.py/"))


from ddi.onrails.repos import merge_instruments, dor1, copy, convert_r2ddi

def questions_variables():

    questions_variables = pd.read_csv("metadata/logical_variables.csv")
    questions_variables.rename(columns={
        "study":"study_name",
        "dataset":"dataset_name",
        "variable":"variable_name",
        "questionnaire":"instrument_name",
        "question":"question_name"
    }, inplace=True)
    questions_variables = questions_variables[["study_name", "dataset_name",
        "variable_name", "instrument_name", "question_name"]]

    questions_variables.dropna(axis=0, how="any", inplace=True)
    questions_variables.drop_duplicates(inplace=True)
    questions_variables.to_csv("ddionrails/questions_variables.csv", index=False)

def main():
    copy.study()
    dor1.variables()
    copy.f("datasets.csv")
    #copy.f("questionnaires.csv", "instruments.csv")
    questions_variables()
    merge_instruments.main()
    convert_r2ddi.Parser("twinlife", version="v3-0-0").write_json()

if __name__ == "__main__":
    main()
