"""Tests that run without an API key."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context_package import ContextPackage
from my_package import MY_PACKAGE, NAIVE_PROMPT


def test_build_prompt_includes_all_five_roles():
    prompt = MY_PACKAGE.build_prompt()
    for heading in ["AUTHORITY", "METADATA", "EXEMPLAR", "CONSTRAINTS", "RUBRIC"]:
        assert heading in prompt


def test_role_order_is_always_the_same():
    """Two packages are only comparable if they assemble the same way."""
    prompt = MY_PACKAGE.build_prompt()
    positions = [prompt.index(h) for h in
                 ["AUTHORITY", "METADATA", "EXEMPLAR", "CONSTRAINTS", "RUBRIC"]]
    assert positions == sorted(positions)


def test_empty_package_reports_all_five_roles_missing():
    assert len(ContextPackage(name="empty").missing_roles()) == 5


def test_the_worked_package_is_complete():
    assert MY_PACKAGE.missing_roles() == []


def test_empty_roles_are_left_out_not_left_blank():
    package = ContextPackage(name="partial", authority="A", exemplar="E")
    assert "CONSTRAINTS" not in package.build_prompt()


def test_the_package_is_much_longer_than_the_naive_prompt():
    assert len(MY_PACKAGE.build_prompt()) > 10 * len(NAIVE_PROMPT)
