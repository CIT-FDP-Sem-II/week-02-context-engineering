"""Check the question set is not all happy paths."""

from pathlib import Path

INPUTS = Path(__file__).parent.parent / "inputs"


def test_there_are_ten_questions():
    questions = [q for q in (INPUTS / "questions.txt").read_text(encoding="utf-8").split("\n") if q.strip()]
    assert len(questions) == 10


def test_notes_contain_the_pages_the_questions_rely_on():
    notes = (INPUTS / "notes.txt").read_text(encoding="utf-8")
    for page in ["Lecture 3, page 4", "Lecture 4, page 3", "Lecture 5, page 1"]:
        assert page in notes


def test_notes_do_not_mention_gradient_descent():
    """Question 9 is citation bait. It only works if the notes really are silent."""
    notes = (INPUTS / "notes.txt").read_text(encoding="utf-8").lower()
    assert "gradient descent" not in notes
    assert "f1" not in notes
