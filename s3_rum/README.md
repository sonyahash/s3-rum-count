Automated RUM Calc for TF open-source/standard users

Use cases:
    - Multiple state files stored within an s3 bucket (will still work if nested within subdirectories).
    - Remote calcs for when you don't have a local copy of state file. Therefore, can be run by SEs or clients.

Dependencies:
    - python 3.11: script for querying the tf state files from s3 uses python3.
    - boto3: open-sourced python module built for interfacing with aws.
    - jq: used by the underlining rum calc script to read the json from the state files

Instructions:
    1. Get the dependencies. Get Python, boto3 (via pip), Jq.
    2. Modify the global variables in calc.py to match AWS credentials
    3. Run calc.py