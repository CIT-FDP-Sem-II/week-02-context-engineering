# Week 2 — Context Engineering: Building Reliable AI Inputs

**CIT AI-Native Engineering Program · Year 1 · Semester 2 · Module M1**

Prompt engineering gets you a good answer sometimes. Reliability needs the
input to be *constructed*. This week turns the five-role framework from
Semester 1 into code, and measures what that actually buys.

**Lab time: 2 hours. API calls: 24.** See [LAB.md](LAB.md).

> The two classes written here — `ContextPackage` and `GeminiClient` — are
> re-used in Weeks 3, 7, 9 and 13. You copy them forward by hand, so every
> week's repo runs on its own.

## Contents

| Path | What it is |
|---|---|
| `src/context_package.py` | `ContextPackage` — five roles, `build_prompt()` |
| `src/gemini_client.py` | `GeminiClient` — one `ask()` method |
| `src/my_package.py` | The worked package, and the naive prompt it is measured against |
| `src/compare.py` | Runs both versions on 10 questions, saves replies to `results/` |
| `inputs/notes.txt` | The lecture notes every question is asked against |
| `inputs/questions.txt` | 10 questions — 3 happy paths, 7 built to break something |
| `worksheets/comparison-table.md` | Where you score the answers **by hand** |
| `worksheets/journal-02.md` | AI Decision Journal Entry #2 |
| `tests/` | 9 tests. No API key needed. |

## The five roles

| Role | Question it answers | What goes wrong without it |
|---|---|---|
| **Authority** | Who is the model? | Generic voice, wrong caution level |
| **Exemplar** | What does good look like? | Right content, unusable shape |
| **Constraint** | What must it not do? | Invented citations, padding |
| **Rubric** | How is it judged? | No self-correction before replying |
| **Metadata** | What must it know? | Wrong format, audience, length |

`build_prompt()` assembles them in a fixed order — Authority, Metadata,
Exemplar, Constraints, Rubric. Fixed on purpose: two packages are only
comparable if they assemble the same way, or you are measuring layout rather
than content.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # mac/linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env                 # mac/linux: cp .env.example .env
```

## Running

```powershell
python src/my_package.py       # print naive vs package side by side - no API calls
python -m pytest tests         # 9 tests - no API calls

python src/compare.py          # 20 API calls, ~3 minutes
python src/compare.py 5        # first 5 questions only - 10 API calls
```

> **Not verified in this repo:** `compare.py` needs a live key and has not
> been run here. Everything else runs offline and is verified.

## Free-tier budget

`compare.py` pauses 4 seconds between calls to stay under the free tier's
rate limit, so a full run takes about 3 minutes. If you hit
`RESOURCE_EXHAUSTED`, wait a minute — do not re-run in a loop.

Short of quota? `python src/compare.py 5` halves it.

## What the machine does and does not do

The program sends the calls and saves the replies. **It does not score them.**
Scoring happens by hand in `worksheets/comparison-table.md`.

That is deliberate. A script can check whether the word SOURCE appears. Only
you can check whether the thing after it is true. Week 9 builds a proper
evaluation dataset with expected answers; until then, reading is the method.

---

## Set B (non-IT background)

Claude-assisted code is fine. Being able to explain it is not optional.

**`src/context_package.py`**
- `ContextPackage` — a box holding the five parts of a context: a name, the
  authority text, the exemplar text, a list of constraints, a list of rubric
  criteria, and a dictionary of metadata facts.
- `missing_roles()` — looks at all five and returns the names of any that are
  empty.
- `build_prompt()` — the important one. Glues the five roles together into one
  block of text with headings, always in the same order, and returns it. That
  text is what gets sent to Gemini.

**`src/gemini_client.py`**
- `MissingKeyError` — its own error type for "no key", because that is a setup
  problem and retrying it will not help.
- `GeminiClient.__init__` — finds the key, picks the model, builds the client.
  Fails straight away if the key is missing.
- `GeminiClient.ask(prompt, system)` — sends one message, returns the reply as
  text. Pass `system` for an engineered run, leave it out for a naive one.

**`src/compare.py`**
- `main()` — reads the notes and the questions, then for each question: one
  naive call, one engineered call, save both to `results/`, pause, repeat.

### What Set B may simplify

- The **Metadata role may describe the format in plain English** — "a
  paragraph, then a line saying where it came from" is fine instead of naming
  field types.
- The comparison may be written in **plain terms** in Journal Entry #2 ("the
  engineered one put a source on every answer, the naive one didn't") rather
  than as a scored total. If you do that, still quote two real answers.
- You may run **5 questions instead of 10**, as long as one of them is Q4 or
  Q9 — the ones the notes do not cover.

### What Set B may **not** simplify

- All five roles must have real content in them. The grader runs
  `missing_roles()`.
- Every reply must be **saved to a file by the program**, not copied out of
  the terminal by hand.
