# LLM-as-Judge Evaluation Pipeline

## Overview

The LLM-as-Judge Evaluation Pipeline automatically evaluates AI-generated responses using Google Gemini. It scores responses using a structured rubric, generates reports, compares prompts or models, and performs basic bias analysis.

---

## Features

- Automated LLM-based evaluation
- Structured scoring rubric
- JSON test suite support
- Robust JSON parsing
- Prompt and response logging
- Report generation (JSON & CSV)
- Prompt/Model comparison
- Bias detection
- FastAPI REST API

---

## Project Structure

```
llm_judge_pipeline/

│── app.py
│── config.py
│── judge.py
│── parser.py
│── report.py
│── compare.py
│── bias.py
│── logger.py
│── requirements.txt
│── README.md
│── .env

├── prompts/
│   └── judge_prompt.txt

├── testcases/
│   └── suite.json

├── logs/

├── reports/

└── outputs/
```

---

## Technology Stack

- Python 3.x
- FastAPI
- Google Gemini API
- Pandas
- Pydantic
- PyYAML
- Python-dotenv

---

## Installation

### Clone Repository

```bash
git clone https://github.com/randhir026/llm_judge_pipeline.git
cd llm_judge_pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

## Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET /

Returns application status.

### POST /evaluate

Runs the complete evaluation pipeline.

Pipeline:

```
Test Suite
    ↓
Judge Prompt
    ↓
Gemini Judge
    ↓
JSON Parser
    ↓
Evaluation
    ↓
Report Generation
    ↓
Bias Analysis
```

---

## Evaluation Rubric

Each response is scored on:

- Correctness
- Faithfulness
- Completeness
- Instruction Following
- Tone
- Safety

Each criterion is scored from **0–10**.

---

## Generated Reports

The pipeline automatically creates:

```
reports/
├── report.json
├── report.csv
└── comparison_report.json
```

---

## Logging

Every evaluation logs:

- Judge Prompt
- Raw LLM Response
- Timestamp
- Latency

Log files:

```
logs/
├── prompts.log
└── responses.log
```

---

## Bias Analysis

Implemented checks include:

- Position Bias
- Length Bias
- Score Clustering

---

## Prompt Comparison

The system compares two prompt versions or models and reports:

- Win Rate
- Draws
- Overall Winner

---

## Example Test Case

```json
{
  "id": 1,
  "input": "What is AI?",
  "system_prompt": "Answer professionally.",
  "model_output": "AI is Artificial Intelligence.",
  "expected_output": "Artificial Intelligence is the simulation of human intelligence by machines."
}
```

---

## Future Improvements

- Multiple LLM support
- Judge ensemble
- Human agreement evaluation
- Token usage tracking
- Advanced bias mitigation

---

## Author

**Randhir Kumar**

MCA Graduate | AI & Machine Learning Enthusiast

Skills:
- Python
- Machine Learning
- Deep Learning
- NLP
- Computer Vision
- Generative AI
- FastAPI
- LLM Applications

---

## License

This project is developed for educational and assignment purposes.
