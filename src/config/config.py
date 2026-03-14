"""
config.py

This file is used to manage environment variables for the project.

It loads the variables stored in a `.env` file using the `python-dotenv`
library. Environment variables are used to store sensitive information
like API keys so that they are not written directly in the code.

Steps performed in this file:
1. Import the required modules (`os` and `load_dotenv`).
2. Load environment variables from the `.env` file into the system environment.
3. Retrieve the GROQ API key from the environment variables.
4. Store the API key in the variable `GROQ_API_KEY` so it can be used
in other parts of the application.

This helps keep secrets secure and makes configuration easier to manage.
"""

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
