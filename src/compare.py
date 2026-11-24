"""Run the naive prompt and the context package on the same questions.

    python src/compare.py            # all 10 questions = 20 API calls
    python src/compare.py 3          # first 3 questions  =  6 API calls

Both versions get the SAME question and the SAME notes. The only difference is
that the engineered run passes the package as a system instruction. If you
changed the question too, you would not know which change caused the result.

Every reply is saved to results/ so you can read them side by side afterwards.
Scoring them is your job, by hand, in worksheets/comparison-table.md - a
machine can check the format, but only you can check whether the answer is
any good.
"""

import sys
import time
from pathlib import Path

from gemini_client import GeminiClient, MissingKeyError
from my_package import MY_PACKAGE, NAIVE_PROMPT

ROOT = Path(__file__).parent.parent
RESULTS = ROOT / "results"

# The free tier allows about 15 requests a minute. Four seconds between calls
# keeps us comfortably under it.
PAUSE_SECONDS = 4


def main():
    notes = (ROOT / "inputs" / "notes.txt").read_text(encoding="utf-8")
    questions = (ROOT / "inputs" / "questions.txt").read_text(encoding="utf-8").split("\n")
    questions = [q.strip() for q in questions if q.strip()]

    if len(sys.argv) > 1:
        questions = questions[: int(sys.argv[1])]

    try:
        client = GeminiClient()
    except MissingKeyError as exc:
        print(f"STOPPED: {exc}")
        return 1

    RESULTS.mkdir(exist_ok=True)
    system = MY_PACKAGE.build_prompt()
    print(f"{len(questions)} questions, 2 calls each = {len(questions) * 2} API calls\n")

    for number, question in enumerate(questions, 1):
        message = f"{question}\n\n{notes}"
        print(f"[{number}] {question}")

        naive = client.ask(f"{NAIVE_PROMPT}\n\n{message}")
        time.sleep(PAUSE_SECONDS)

        engineered = client.ask(message, system=system)
        time.sleep(PAUSE_SECONDS)

        (RESULTS / f"{number:02d}-naive.txt").write_text(naive, encoding="utf-8")
        (RESULTS / f"{number:02d}-engineered.txt").write_text(engineered, encoding="utf-8")
        print(f"    naive {len(naive.split()):>3} words | engineered {len(engineered.split()):>3} words")

    print(f"\nSaved to {RESULTS}")
    print("Now fill in worksheets/comparison-table.md by reading them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
