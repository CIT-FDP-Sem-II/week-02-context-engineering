"""The worked example: one Semester 1 prompt, rebuilt as a context package.

The task is a study-notes assistant: a student pastes lecture notes and asks a
question about them. Replace it with your own Semester 1 domain.

Run `python src/my_package.py` to print the naive prompt and the assembled
package side by side. No API calls.
"""

from context_package import ContextPackage

# What Semester 1 looked like: one sentence of instruction.
NAIVE_PROMPT = "Answer the student's question about their lecture notes."


# What Semester 2 looks like: the same task, built out of five roles.
MY_PACKAGE = ContextPackage(
    name="study-notes-assistant",
    authority=(
        "You are a subject tutor working with first-year undergraduates. "
        "You are precise about what the notes do and do not say, and you are "
        "comfortable saying that the notes do not cover something."
    ),
    exemplar=(
        "QUESTION: What is the difference between precision and recall?\n\n"
        "ANSWER: Precision asks how many of the things you flagged were right. "
        "Recall asks how many of the right things you flagged.\n"
        "SOURCE: lecture 3, page 4\n"
        "NOT IN NOTES: nothing"
    ),
    constraints=[
        "Never state a fact the notes do not support without putting it under NOT IN NOTES.",
        "Never invent a lecture or page number.",
        "Do not guess at a question the notes do not cover - say which part is missing.",
        "Do not pad. Three accurate sentences beat a page of hedging.",
    ],
    rubric=[
        "Every claim is traceable to the notes, or listed under NOT IN NOTES.",
        "The answer addresses the exact question, not the topic it belongs to.",
        "The SOURCE line names a real place in the notes.",
        "The answer is under 150 words.",
    ],
    metadata={
        "audience": "first-year undergraduate",
        "output format": "ANSWER line, then SOURCE line, then NOT IN NOTES line",
        "source of truth": "only the notes given in the message",
        "length": "under 150 words",
    },
)


if __name__ == "__main__":
    print("--- NAIVE PROMPT (Semester 1) ---")
    print(NAIVE_PROMPT)
    print(f"\n[{len(NAIVE_PROMPT)} characters]\n")

    print("--- CONTEXT PACKAGE (Semester 2) ---")
    print(MY_PACKAGE.build_prompt())
    print(f"\n[{len(MY_PACKAGE.build_prompt())} characters]")
    print(f"\nMissing roles: {MY_PACKAGE.missing_roles() or 'none'}")
