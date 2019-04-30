#!/bin/sh 

if [ ! -d ./ddionrails ]; then 
   /usr/bin/mkdir ./ddionrails || exit
else
  echo "cleanup dir: ./ddionrails/* " >&2
  /usr/bin/rm -rf ./ddionrails/*
fi

echo "start ./lib_py/fill_ddionrails.py" >&2
python3 ./lib_py/fill_ddionrails.py
