import os
import json
import pandas as pd

# Create reports directory
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report(results):
    """
    Generate report.json and report.csv
    """

    if not results:
        print("No results found.")
        return

    df = pd.DataFrame(results)

    numeric_columns = [
        "correctness",
        "faithfulness",
        "completeness",
        "instruction_following",
        "tone",
        "safety",
        "overall"
    ]

    # Calculate average scores
    averages = {}

    for col in numeric_columns:
        if col in df.columns:
            averages[col] = round(df[col].mean(), 2)

    # Pass Rate (Overall >= 7)
    pass_count = 0

    if "overall" in df.columns:
        pass_count = len(df[df["overall"] >= 7])

    pass_rate = round((pass_count / len(df)) * 100, 2)

    summary = {
        "total_cases": len(df),
        "pass_rate": pass_rate,
        "average_scores": averages
    }

    # Save JSON
    with open(os.path.join(REPORT_DIR, "report.json"),
              "w",
              encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    # Save CSV
    df.to_csv(
        os.path.join(REPORT_DIR, "report.csv"),
        index=False
    )

    print("Report generated successfully.")

    return summary