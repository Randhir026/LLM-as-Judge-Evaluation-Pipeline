import json

from fastapi import FastAPI

from judge import judge
from parser import parse_response
from report import generate_report
from bias import bias_report

app = FastAPI(
    title="LLM Judge Evaluation Pipeline",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM-as-Judge Evaluation Pipeline is Running"
    }


@app.post("/evaluate")
def evaluate():

    # Load test suite
    with open("testcases/suite.json", "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    results = []

    for test_case in test_cases:

        # Call Gemini Judge
        judge_result = judge(test_case)

        # Parse JSON response
        parsed = parse_response(judge_result["response"])

        # Add useful metadata
        parsed["id"] = test_case["id"]
        parsed["latency"] = judge_result["latency"]

        results.append(parsed)

    # Generate reports
    report = generate_report(results)

    # Bias analysis
    bias = bias_report(results)

    return {
        "report": report,
        "bias_analysis": bias,
        "results": results
    }