import json
import os

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)


def compare_results(results_a, results_b,
                    name_a="Model A",
                    name_b="Model B"):
    """
    Compare two evaluation result sets.
    """

    if len(results_a) != len(results_b):
        raise ValueError("Both result sets must have the same number of test cases.")

    wins_a = 0
    wins_b = 0
    draws = 0

    comparison = []

    for i, (a, b) in enumerate(zip(results_a, results_b), start=1):

        score_a = a.get("overall", 0)
        score_b = b.get("overall", 0)

        if score_a > score_b:
            winner = name_a
            wins_a += 1

        elif score_b > score_a:
            winner = name_b
            wins_b += 1

        else:
            winner = "Draw"
            draws += 1

        comparison.append({
            "test_case": i,
            name_a: score_a,
            name_b: score_b,
            "winner": winner
        })

    if wins_a > wins_b:
        overall_winner = name_a
    elif wins_b > wins_a:
        overall_winner = name_b
    else:
        overall_winner = "Tie"

    report = {
        "summary": {
            name_a: wins_a,
            name_b: wins_b,
            "draws": draws,
            "overall_winner": overall_winner
        },
        "comparison": comparison
    }

    with open(
        os.path.join(REPORT_DIR, "comparison_report.json"),
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(report, file, indent=4)

    print("Comparison report generated.")

    return report