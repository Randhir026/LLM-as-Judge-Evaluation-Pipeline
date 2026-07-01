import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

PROMPT_LOG = os.path.join(LOG_DIR, "prompts.log")
RESPONSE_LOG = os.path.join(LOG_DIR, "responses.log")


def log_prompt(prompt):
    """
    Save the prompt sent to the judge model.
    """

    with open(PROMPT_LOG, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 80 + "\n")
        file.write(f"Timestamp : {datetime.now()}\n\n")
        file.write(prompt)
        file.write("\n")


def log_response(response, latency):
    """
    Save the raw response returned by the judge model.
    """

    with open(RESPONSE_LOG, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 80 + "\n")
        file.write(f"Timestamp : {datetime.now()}\n")
        file.write(f"Latency   : {latency} seconds\n\n")
        file.write(response)
        file.write("\n")