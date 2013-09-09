analyze-dovecot-log
===================

## Description

This Python script will produce a summary table of connection information for a given user from a Dovecot log file. Its first argument is the user to analyze. Its second argument is the Dovecot log file. The example below will summarize data for the user *smith* from the file `dovecot` found in the same directory as the analyze-dovecot-log.py script.

## Use

    $ ./analyze-dovecot-log.py smith dovecot
