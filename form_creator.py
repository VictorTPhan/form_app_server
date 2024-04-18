import chat_gpt
import json
from pathlib import Path

def read_text_file(path):
    file_path = Path(path)
    file_content = file_path.read_text()
    return file_content

def create_form(goal, problem, form_length, allowed_types, solution_task):
    create_form_system_prompt = read_text_file("create_form/system_prompt.txt")
    create_form_user_prompt = read_text_file("create_form/user_prompt.txt")
    create_form_user_prompt = create_form_user_prompt.replace("<GOAL>", goal)
    create_form_user_prompt = create_form_user_prompt.replace("<PROBLEM>", problem)
    create_form_user_prompt = create_form_user_prompt.replace("<FORM_LENGTH>", form_length)
    create_form_user_prompt = create_form_user_prompt.replace("<ALLOWED_TYPES>", str(allowed_types))
    create_form_user_prompt = create_form_user_prompt.replace("<SOLUTION_TASK>", solution_task)

    return json.loads(chat_gpt.get_json_response(create_form_system_prompt, create_form_user_prompt))

def submit_form(goal, problem, solution_task, responses):
    submit_form_system_prompt = read_text_file("submit_form/system_prompt.txt")
    submit_form_user_prompt = read_text_file("submit_form/user_prompt.txt")
    submit_form_user_prompt = submit_form_user_prompt.replace("<GOAL>", goal)
    submit_form_user_prompt = submit_form_user_prompt.replace("<PROBLEM>", problem)
    submit_form_user_prompt = submit_form_user_prompt.replace("<SOLUTION_TASK>", solution_task)
    submit_form_user_prompt = submit_form_user_prompt.replace("<RESPONSES>", str(list(responses.items())))

    return json.loads(chat_gpt.get_standard_response(submit_form_system_prompt, submit_form_user_prompt))