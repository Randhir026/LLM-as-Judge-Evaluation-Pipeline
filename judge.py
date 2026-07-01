import time
from config import model
from logger import log_prompt, log_response


def load_prompt():
    """
    Load the judge prompt template.
    """
    with open("prompts/judge_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(test_case):
    """
    Replace placeholders in the prompt template
    with actual values from the test case.
    """

    prompt = load_prompt()

    prompt = prompt.replace("{input}", test_case.get("input", ""))
    prompt = prompt.replace("{system_prompt}", test_case.get("system_prompt", ""))
    prompt = prompt.replace("{model_output}", test_case.get("model_output", ""))
    prompt = prompt.replace("{expected_output}", test_case.get("expected_output", ""))

    return prompt


def judge(test_case):
    """
    Send the prompt to Gemini,
    log prompt & response,
    and return the result.
    """

    # Build prompt
    prompt = build_prompt(test_case)

    # Log prompt
    log_prompt(prompt)

    # Start timer
    start_time = time.time()

    # Call Gemini
    response = model.generate_content(prompt)

    # Calculate latency
    latency = round(time.time() - start_time, 2)

    # Log raw response
    log_response(response.text, latency)

    # Return results
    return {
        "prompt": prompt,
        "response": response.text,
        "latency": latency
    }