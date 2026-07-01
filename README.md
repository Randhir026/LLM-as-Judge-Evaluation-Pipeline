# LLM-as-Judge Evaluation Pipeline

## Overview

The **LLM-as-Judge Evaluation Pipeline** is an automated evaluation system that uses a Large Language Model (LLM) as a judge to assess the quality of AI-generated responses. Instead of relying on manual evaluation, the pipeline scores responses based on a structured rubric, generates reports, compares different prompts or models, and analyzes potential judge bias.

This project is developed as part of the **Applied AI/ML Engineering Take-Home Assignment – Problem 2**.

---

# Features

* Evaluate AI-generated responses using Gemini.
* Structured scoring rubric.
* JSON/YAML test suite support.
* Robust JSON parsing.
* Prompt and response logging.
* Report generation (JSON & CSV).
* Bias detection.
* Prompt/Model comparison.
* FastAPI REST API.
* Environment variable configuration.

---

# Project Structure

```
llm_judge_pipeline/

│── app.py
│── config.py
│── judge.py
│── parser.py
│── compare.py
│── report.py
│── bias.py
│── logger.py
│── requirements.txt
│── .env
│── README.md

├── prompts/
│     judge_prompt.txt

├── testcases/
│     suite.json

├── logs/
│     prompts.log
│     responses.log

├── reports/
│     report.json
│     report.csv
│     comparison_report.json

└── outputs/
```

---

# Tech Stack

* Python
* FastAPI
* Google Gemini API
* Pandas
* Pydantic
* PyYAML
* Python-dotenv

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd llm_judge_pipeline
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

# Running the Application

Start the server.

```bash
uvicorn app:app --reload
```

Open Swagger UI.

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## GET /

Returns the application status.

Example Response

```json
{
    "message":"LLM-as-Judge Evaluation Pipeline is Running"
}
```

---

## POST /evaluate

Runs the complete evaluation pipeline.

Pipeline Flow

```
Read Test Suite

↓

Generate Judge Prompt

↓

Gemini Judge

↓

Parse JSON

↓

Generate Report

↓

Bias Analysis

↓

Return Results
```

---

# Evaluation Rubric

Each response is scored using the following criteria.

| Criterion             | Score |
| --------------------- | ----- |
| Correctness           | 0–10  |
| Faithfulness          | 0–10  |
| Completeness          | 0–10  |
| Instruction Following | 0–10  |
| Tone                  | 0–10  |
| Safety                | 0–10  |

The final output also contains:

* Overall Score
* Rationale

---

# Logging

Every evaluation stores

* Judge Prompt
* Raw Response
* Timestamp
* Latency

Files

```
logs/prompts.log

logs/responses.log
```

---

# Reports

The system automatically generates

```
reports/report.json

reports/report.csv
```

The report includes

* Total Test Cases
* Pass Rate
* Average Scores
* Overall Statistics

---

# Bias Handling

The pipeline includes basic judge-bias analysis.

Implemented checks

* Position Bias
* Length Bias
* Score Clustering

Generated summary includes

* Flip Rate
* Score Range
* Clustering Detection

---

# Prompt Comparison

The pipeline supports comparing two prompt versions or two models.

Outputs

* Win Rate
* Draws
* Overall Winner

Saved as

```
comparison_report.json
```

---

# Test Suite Format

Example

```json
[
    {
        "id":1,
        "input":"What is AI?",
        "system_prompt":"Answer professionally.",
        "model_output":"AI is Artificial Intelligence.",
        "expected_output":"Artificial Intelligence is the simulation of human intelligence by machines."
    }
]
```

---

# Future Improvements

* Judge ensemble
* Multiple LLM support
* Judge consistency testing
* Token usage tracking
* Human agreement evaluation
* Advanced adversarial bias detection

---

# Conclusion

This project demonstrates how Large Language Models can be used as automated evaluators for AI-generated responses. The pipeline provides structured scoring, report generation, bias analysis, prompt comparison, and REST API integration, making it suitable for evaluating prompt engineering experiments and LLM applications.

---
