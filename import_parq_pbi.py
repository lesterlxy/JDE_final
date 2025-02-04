# WARNING: 
# This script is a proof-of-concept - DO NOT RUN THIS IN POWER BI.
# The script works fine on it's own in python but will blow up your
# memory in Power BI for some reason.

# Description: 
# Programmatically load all .parquet files in a directory with this
# script using the Python connector in Power BI.
# Because the standard parquet connector requires you to load each
# file individually by pasting/typing the path.

import os

import pandas as pd  # noqa: F401 # we are using it in exec

# CHANGE YOUR PARQUET DIRECTORY HERE
PARQ_DIR = "D:/documents/ipynb/JDE_final/.export/"

files = os.listdir(PARQ_DIR)
files = [f for f in files if f.endswith(".parquet")]
for f in files:
    varname = f.split(".")[0]
    fullpath = os.path.join(PARQ_DIR, f)
    exec(f"{varname} = pd.read_parquet(fullpath, engine='pyarrow')")
