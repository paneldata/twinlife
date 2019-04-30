#!/bin/sh 

BIN_RM=/usr/bin/rm
STATA_BIN=/usr/local/stata/stata-se

TEMP_DIR="./temp"

DATA_VERSION="v3-0-0"

TMP_DATA_DIR="${TEMP_DIR}/${DATA_VERSION}/en"


if [ ! -d "${TEMP_DIR}" ]; then
  echo "# mkdir \"${TEMP_DIR}\"" >&2
  mkdir "${TEMP_DIR}" || exit 
fi

## cleanup/delete all  
echo "# cleanup/delete $TEMP_DIR/*" >&2
${BIN_RM} -rf $TEMP_DIR/*

echo "# create \$TMP_DATA_DIR = $TMP_DATA_DIR" >&2
mkdir -p "$TMP_DATA_DIR"

echo "# run stata (SAVEOLD ...)" >&2
${STATA_BIN} -b do lib_stata/save_old.do

echo "# run: ./lib_R/run_r2ddi.R" >&2
Rscript lib_R/run_r2ddi.R
