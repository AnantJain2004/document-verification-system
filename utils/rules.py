def rule_check(text):
    keywords = [
        "explain", "define", "discuss", "algorithm",
        "database","question", "marks",
        "unit", "diagram","differentiate"
    ]

    score = sum(1 for word in keywords if word in text)
    return score >= 10