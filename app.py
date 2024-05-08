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
  '''
  A POST API that is called whenever the application wants to create a form.
  This requires a JSON payload containing the form's parameters (determined by the system prompt)
  '''
  data = request.json
  goal = data.get("GOAL")
  problem = data.get("PROBLEM")
  form_length = data.get("FORM_LENGTH")
  allowed_types = data.get("ALLOWED_TYPES")
  solution_task = data.get("SOLUTION_TASK")

  return jsonify(form_creator.create_form(goal, problem, form_length, allowed_types, solution_task))

@app.route('/submit_form/', methods=["POST"])
def submit_form():
  '''
  A POST API that is called whenever the application submits a response to
  a generated form. This requires a JSON payload containing the response's parameters
  (determined by the system prompt)
  '''
  
  data = request.json
  goal = data.get("GOAL")
  problem = data.get("PROBLEM")
  solution_task = data.get("SOLUTION_TASK")
  responses = data.get("RESPONSES")

  return jsonify(form_creator.submit_form(goal, problem, solution_task, responses))

if __name__ == '__main__':
  app.run(host='0.0.0.0')