from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-zdQ2gSRT9t4kARy8qFK6T3BlbkFJmYVa09l6hVA45rqcz1Lk",
)

def get_json_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def get_standard_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content