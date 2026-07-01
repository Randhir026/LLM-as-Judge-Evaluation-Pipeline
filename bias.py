import copy


def check_position_bias(test_case, judge_function):
    """
    Check position bias by evaluating A vs B
    and B vs A.
    """

    case_ab = copy.deepcopy(test_case)

    result_ab = judge_function(case_ab)

    case_ba = copy.deepcopy(test_case)

    case_ba["model_output"], case_ba["expected_output"] = (
        case_ba["expected_output"],
        case_ba["model_output"]
    )

    result_ba = judge_function(case_ba)

    score_ab = result_ab.get("overall", 0)
    score_ba = result_ba.get("overall", 0)

    flipped = score_ab != score_ba

    return {
        "score_ab": score_ab,
        "score_ba": score_ba,
        "position_bias_detected": flipped
    }


def check_length_bias(result):
    """
    Check whether a high score was given
    to an unusually long answer.
    """

    answer = result.get("model_output", "")

    words = len(answer.split())

    score = result.get("overall", 0)

    return {
        "answer_length": words,
        "overall_score": score,
        "length_bias_warning": (
            words > 200 and score >= 9
        )
    }


def check_score_clustering(results):
    """
    Detect if all scores are nearly identical.
    """

    scores = [
        r.get("overall", 0)
        for r in results
    ]

    if not scores:
        return {
            "clustering_detected": False
        }

    spread = max(scores) - min(scores)

    return {
        "score_range": spread,
        "clustering_detected": spread < 1
    }


def bias_report(results):
    """
    Generate a bias summary report.
    """

    clustering = check_score_clustering(results)

    return {
        "total_cases": len(results),
        "score_clustering": clustering
    }