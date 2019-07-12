from flask import Flask
from flask import request, jsonify
from src.textservice import summarizer

app = Flask(__name__)


@app.route('/summarizer', methods=['POST', 'GET'])
def summary():

    content = request.get_json()
    desc = content['Description']
    res_summary = summarizer(desc)

    result = {
        "Summary": res_summary
    }

    return jsonify(result)


app.run(host='127.0.0.1', port=8080)
