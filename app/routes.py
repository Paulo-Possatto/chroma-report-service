from flask import Flask, request, jsonify, send_file
from db_connector import MongoDBConnector
from report_generator import ReportGenerator
import os

app = Flask(__name__)
db_connector = MongoDBConnector()

@app.route("/generate-report", methods=["POST"])
def generate_report():
    transformer_id = request.json.get("transformer_id")
    results = db_connector.fetch_results(transformer_id)
    
    if not results:
        return jsonify({"message": "No data found!"}), 404
    
    file_path = "/tmp/report_{identifier}.docx".format(identifier=transformer_id)
    ReportGenerator.create_word_report(results, file_path)
    return send_file(file_path, as_attachment=True)
