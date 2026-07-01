import json
import re


def extract_json(text):
    """
    Extract JSON object from Gemini response.
    """

    # Remove markdown code blocks like ```json ... ```
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Find first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found.")

    return match.group()


def parse_response(response_text):
    """
    Convert Gemini response into Python dictionary.
    """

    try:
        json_text = extract_json(response_text)
        return json.loads(json_text)

    except json.JSONDecodeError as e:
        return {
            "error": "Invalid JSON",
            "details": str(e),
            "raw_response": response_text
        }

    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response_text
        }
        