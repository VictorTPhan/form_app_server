import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-zdQ2gSRT9t4kARy8qFK6T3BlbkFJmYVa09l6hVA45rqcz1Lk",
)

system_prompt = """
You are a helpful assistant that can provide solutions to problems. Users will send you the first response in the following JSON format:

{
    "GOAL": <the desired goal>,
    "PROBLEM": <the user's problem>,
    "FORM_LENGTH": <the amount of questions they want in the form>,
    "ALLOWED_TYPES": <is a list that may contain only the following (but not all): SHORT_ANSWER_RESPONSE, LONG_ANSWER_RESPONSE, MULTIPLE_CHOICE, CHECKBOX>,
    "SOLUTION_TASK": <what the user wants you to do>
}

Note that [MULTIPLE_CHOICE] and [CHECKBOX] are questions with several options, but the user can only select 1 answer for [MULTIPLE_CHOICE]. 
Once you receive the first response, you will process it using this template:

I want [GOAL] but [PROBLEM]. Create a form for me to fill out with [FORM_LENGTH] questions that you would like to know first.
The questions in this form can be [ALLOWED_TYPES].
I will then fill out this form and send it back to you.
Once you process my submission, [SOLUTION_TASK].

You will send back a response in JSON format as follows. The field questions must be of size [FORM_LENGTH].
{
    "form_name": <name of form>
    "questions": [
        {
            "type": "SHORT_ANSWER_RESPONSE",
            "question": <the question>
        },
        {
            "type": "LONG_ANSWER_RESPONSE",
            "question": <the question>
        },
        {
            "type": "MULTIPLE_CHOICE",
            "question": <the question>,
            "options": <list of all option strings>
        },
        {
            "type": "CHECKBOX",
            "question": <the question>,
            "options": <list of all option strings>
        },
    ]
}
"""

user_prompt = """
{
    "GOAL": "cook something for a potluck",
    "PROBLEM": "I'm bad at cooking",
    "FORM_LENGTH": 5,
    "ALLOWED_TYPES": [SHORT_ANSWER_RESPONSE, LONG_ANSWER_RESPONSE, MULTIPLE_CHOICE, CHECKBOX],
    "SOLUTION_TASK": "give me a recipe that I could follow."
}
"""

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
  ]
)
print(response.choices[0].message.content)

system_prompt = """
You are a helpful assistant that can provide solutions to problems. Imagine you have previously given a user a form to fill out before you can help them.
A user will send you the following JSON:

{
    "GOAL": <the desired goal>,
    "PROBLEM": <the user's problem>,
    "SOLUTION_TASK": <what the user wants you to do>,
    "RESPONSES": [
        {
            "question": <the question>,
            "answer": <the user's answer>
        }
    ]
}

The user wants to [GOAL] but [PROBLEM]. They want you to [SOLUTION_TASK]. Fulfill their request with their responses in mind.
"""

user_prompt = """
{
    "GOAL": "cook something for a potluck",
    "PROBLEM": "I'm bad at cooking",
    "SOLUTION_TASK": "give me a recipe that I could follow."
    "RESPONSES": [
        {
            "question": "What is your favorite cuisine?",
            "answer": "I like Vietnamese food."
        },
        {
            "question": "What cooking techniques do you struggle with?",
            "answer": "I'm not great with knife skills and I often fear that I'll burn myself while cooking. I also have trouble knowing when something is considered cooked."
        },
        {
            "question": "Which of the following ingredients do you feel comfortable working with?",
            "answer": ["Vegetables", "Meat", "Pasta", "Spices", "Dairy"]
        },
        {
            "question": "Select the kitchen equipment you have access to:",
            "answer": ["Oven", "Stovetop", "Microwave", "Slow Cooker"]
        },
        {
            "question": "Do you have any dietary restrictions or preferences?",
            "answer": "No."
        }
    ]
}
"""

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
  ]
)
print(response.choices[0].message.content)