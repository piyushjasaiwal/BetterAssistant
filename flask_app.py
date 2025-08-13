from flask import Flask, request, jsonify
from assistant import Assistant

assistant_obj = Assistant()

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/api/v1/query", methods=["POST"])
def query():
    request_body = request.get_json()

    if not request_body:
        return jsonify({"error": "No JSON body found"}), 400
    
    query_text = request_body.get("query")
    if not query_text:
        return jsonify({"error": "Missing 'query' field"}), 400
    
    result = assistant_obj.ask(query_text) 
    return jsonify({"response": result}), 200

@app.route("/api/v1/export", methods=["POST"])
def export_chat():
    file_name = request.args.get("filename", default="logs", type = str)
    assistant_obj.export(filename=file_name)
    return jsonify({"response": "Export successful"}), 200


if __name__ == "__main__":
    app.run(debug=False)