# Analyze Dovecot log

## Description

This Python script will produce a summary table of connection information for a given user from a Dovecot log file. The output is a CSV file which may be loaded into a spreadsheet and sorted easily. The script's first argument is the user to analyze. Its second argument is the Dovecot log file. The example below will summarize data for the user *smith* from the file `dovecot` found in the same directory as `analyze-dovecot-log.py` and produce `smith.csv`.

## Use

    $ ./analyze-dovecot-log.py smith dovecot
