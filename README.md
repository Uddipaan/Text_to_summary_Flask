# Text_to_summary_Flask
This takes in a description and returns summary

API endpoint is: http://127.0.0.1:8080/summarizer

Input JSON:
{
    "Description": *enter your description*
}

Steps(Run these commands in sequence):
1. pip install -r requirements.txt
2. python -m spacy download en
3. python app.py