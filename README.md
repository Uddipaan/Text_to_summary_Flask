# Text_to_summary_Flask
---------------------------------------------------------------------------------------------------------------------------------
Note: For windows users, please install Microsoft visual studio tools latest from https://visualstudio.microsoft.com/downloads/.
This is required for Spacy to install on windows.
It should be fine for Linux based users I guess. :)
---------------------------------------------------------------------------------------------------------------------------------

This takes in a description and returns summary
API endpoint is: http://127.0.0.1:8080/summarizer

Input:
{
    "Description": *enter your description*
}
Output:
{
    "Summary": *processed summary based on given description*
}

Steps(Run these commands in sequence):
1. pip install -r requirements.txt
2. python -m spacy download en
3. python app.py
