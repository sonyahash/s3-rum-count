<h4>Automated RUM Calc for Terraform Community</h4>
<h5>Created by Alex Zhong Solutions Engineering Summer 2023</h5>

<h5>Use cases: </h5>
    - Multiple state files stored within an s3 bucket (will still work if nested within subdirectories). <br>
    - Remote calcs for when you don't have a local copy of state file. Therefore, can be run by SEs or clients.<br>

<h5>Dependencies:</h5>
    - Python 3.11: script for querying the tf state files from s3 uses python3.<br>
    - Boto3: open-sourced python module built for interfacing with aws.<br>
    - jq: used by the underlining rum calc script to read the json from the state files<br>

<h5>Instructions:</h5>
    1. Get the dependencies. Get Python, boto3 (via pip), Jq.<br>
    2. Modify the global variables in calc.py to match AWS credentials<br>
    3. Run calc.py<br>
