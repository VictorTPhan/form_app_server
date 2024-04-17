from flask import Flask, request, jsonify
from flask_cors import CORS

import form_creator

app = Flask(__name__)
CORS(app)

@app.route('/')
def test_method():
    return jsonify("Server is online!")

@app.route('/create_form/', methods=["POST"])
def create_form():
  goal = request.args.get("GOAL")
  problem = request.args.get("PROBLEM")
  form_length = request.args.get("FORM_LENGTH")
  allowed_types = request.args.get("ALLOWED_TYPES")
  solution_task = request.args.get("SOLUTION_TASK")

  return jsonify(form_creator.create_form(goal, problem, form_length, allowed_types, solution_task))

@app.route('/submit_form/', methods=["POST"])
def submit_form():
  goal = request.args.get("GOAL")
  problem = request.args.get("PROBLEM")
  solution_task = request.args.get("SOLUTION_TASK")
  responses = request.args.get("RESPONSES")

  return jsonify(form_creator.submit_form(goal, problem, solution_task, responses))

if __name__ == '__main__':
  app.run(host='0.0.0.0')