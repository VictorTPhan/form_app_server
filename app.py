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
  data = request.json
  goal = data.get("GOAL")
  problem = data.get("PROBLEM")
  form_length = data.get("FORM_LENGTH")
  allowed_types = data.get("ALLOWED_TYPES")
  solution_task = data.get("SOLUTION_TASK")

  print(goal)
  print(problem)
  print(form_length)
  print(allowed_types)
  print(solution_task)

  return jsonify(form_creator.create_form(goal, problem, form_length, allowed_types, solution_task))

@app.route('/submit_form/', methods=["POST"])
def submit_form():
  data = request.json
  goal = data.get("GOAL")
  problem = data.get("PROBLEM")
  solution_task = data.get("SOLUTION_TASK")
  responses = data.get("RESPONSES")

  print(goal)
  print(problem)
  print(solution_task)
  print(responses)

  return jsonify(form_creator.submit_form(goal, problem, solution_task, responses))

if __name__ == '__main__':
  app.run(host='0.0.0.0')