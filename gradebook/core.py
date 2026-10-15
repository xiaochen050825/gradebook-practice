from typing import Dict, List


def parse_line(line: str) -> tuple:
    """Parse 'name, score' into (name, int score). Extra spaces are ignored."""
    name, score = line.split(",")
    return name.strip(), int(score)


def average(scores: List[int]) -> float:
    """Return the average score, or 0.0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / (len(scores))


def grade(score: int) -> str:
    """HD >= 80, D >= 70, C >= 60, P >= 50, otherwise N."""
    if score >= 80:
        return "HD"
    if score >= 70:
        return "D"
    if score >= 60:
        return "C"
    if score >= 50:
        return "P"
    return "N"


def top_students(scores: Dict[str, int], n: int) -> List[str]:
    """Return the names of the n highest scorers, highest first."""
    ranked = sorted(scores, key=lambda name: scores[name], reverse=True)
    return ranked[:n]
