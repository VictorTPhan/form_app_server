# Formerly Server

This repository hosts the server that the Formerly app uses. This is a Flask server that utilizes the `gunicorn` library and is hosted on render.com. It mainly makes calls to the ChatGPT API.

This repository contains the following:
- **create_form**: A folder containing text files for the system and user prompts for using ChatGPT to create a form.
- **submit_form**: A folder containing text files for the system and user prompts for using ChatGPT to process a form submission.
- **app.py** - The main Flask server that hosts the API endpoints.
- **chat_gpt.py** - An abstraction layer between the server and ChatGPT to make using system and user prompts easier.
- **form_creator.py** - An intermediary Python file to call the `chat_gpt.py` script.

You can view the repository for the Formerly frontend [here](https://github.com/VictorTPhan/form_app).