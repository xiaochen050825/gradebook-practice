from gradebook.core import parse_line, average, grade, top_students


def test_parse_line_strips_spaces():
    assert parse_line("  Alice ,  85 ") == ("Alice", 85)


def test_average():
    assert average([60, 70, 80]) == 70


def test_average_empty():
    assert average([]) == 0.0


def test_grade_boundary_hd():
    assert grade(80) == "HD"


def test_grade_others():
    assert grade(75) == "D"
    assert grade(49) == "N"


def test_top_students():
    assert top_students({"A": 50, "B": 90, "C": 70}, 2) == ["B", "C"]
