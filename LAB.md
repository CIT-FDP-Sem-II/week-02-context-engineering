# Week 2 Lab — Context Engineering

**Time: 2 hours · API calls used: 24**

| # | Activity | Time | Code? |
|---|----------|------|-------|
| 1 | Write `context_package.py` | 25 min | yes |
| 2 | Write `gemini_client.py` | 15 min | yes |
| 3 | Build your own package | 25 min | yes (writing text) |
| 4 | Run both versions on 10 questions | 15 min | run only |
| 5 | Score the answers by hand | 25 min | no |
| 6 | One-role experiment | 10 min | run only |
| 7 | Journal Entry #2 | 5 min | no |

---

## 1. Write `context_package.py` (25 min)

Build a `ContextPackage` class that holds the five roles and glues them into
one system instruction.

It needs:
- five fields: `authority`, `exemplar`, `constraints`, `rubric`, `metadata`
- `build_prompt()` — returns all five as one string, **always in the same order**
- `missing_roles()` — tells you which roles you left empty
- empty roles left out of the output, not printed as empty headings

Attempt it first. Then read `src/context_package.py` — it is about 60 lines.
The docstring explains why the order is fixed.

---

## 2. Write `gemini_client.py` (15 min)

A `GeminiClient` class with one `ask()` method.

It needs:
- the API key read from the environment in **exactly one place**
- a clear failure at construction time if the key is missing, not halfway
  through a 20-call run
- `ask(prompt, system=None)` — `system` is where the assembled package goes

See `src/gemini_client.py` — about 40 lines.

---

## 3. Build your own package (25 min, no API calls)

Open `src/my_package.py`. The worked example is a study-notes assistant.
**Replace it with your own Semester 1 task.**

Minimum for each role:

| Role | Minimum | The question to answer |
|---|---|---|
| Authority | 2 sentences | Who is this, and what do they know that a generic assistant does not? |
| Exemplar | 1 full example | What does a good answer look like — *shown*, not described |
| Constraints | 4 rules | What has the model done that you did not want? Each becomes a rule |
| Rubric | 4 criteria | How would you tell a good answer from a bad one? |
| Metadata | 4 facts | Format, audience, length, source of truth |

The Exemplar is the hard one. Resist describing a good answer. Write one.

Check it with:

```powershell
python src/my_package.py
```

---

## 4. Run both versions (15 min, 20 API calls)

```powershell
python src/compare.py
```

This sends each of the 10 questions twice — once with the naive prompt, once
with your package — and saves all 20 replies to `results/`.

It pauses 4 seconds between calls to stay inside the free tier's rate limit.
The full run takes about 3 minutes. Start it, then read ahead.

Short of time or quota? `python src/compare.py 5` does the first 5 questions
(10 calls). Make sure one of them is question 4 or 5.

---

## 5. Score the answers by hand (25 min, no code)

Open `worksheets/comparison-table.md` and the files in `results/`.

Mark each answer Y or N on five things: right format, cited a source, admitted
what it did not know, invented anything, actually useful.

**Read the answers.** This is the real work of the lab. A script can check
whether the word SOURCE appears; only you can tell whether the thing after it
is true.

Pay particular attention to:
- **Q4 and Q9** — the notes do not cover these. Did either version invent?
- **Q7** — the question contains a false statement. Did either correct it?
- **Q6 and Q8** — did the engineered version get *worse* here?

---

## 6. One-role experiment (10 min, 4 API calls)

Pick the role you think is doing the most work. Comment it out of
`MY_PACKAGE`, then re-run just two questions:

```powershell
python src/compare.py 4
```

Note what broke in the worksheet. The answer is usually not the role you
expected.

---

## 7. Journal Entry #2 (5 min)

Fill in `worksheets/journal-02.md`. **Question:** what changed when you added
explicit Authority and Rubric?

You must name one way the engineered version got **worse**. An entry with no
cost recorded has not looked hard enough.

---

## Before you leave

- [ ] `ContextPackage` with `build_prompt()` working
- [ ] `GeminiClient` with `ask()` working
- [ ] Your own Semester 1 prompt rebuilt with all five roles
- [ ] 20 replies saved in `results/`
- [ ] Comparison table scored by hand
- [ ] One-role experiment run and recorded
- [ ] `python -m pytest tests` passes
- [ ] Journal Entry #2 written
