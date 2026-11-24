# Worksheet — Naive vs Engineered

Run `python src/compare.py`, then open the files in `results/` and score them
**by hand**. Reading the answers is the exercise. A script could check the
format for you, but only you can tell whether an answer is actually useful.

## What each question is testing

| # | Question | What it is testing |
|---|----------|--------------------|
| 1 | precision vs recall | happy path — fully covered by the notes |
| 2 | train/test split and overfitting | happy path — needs two pages joined up |
| 3 | four cells of a confusion matrix | plain recall of fact; tests format |
| 4 | what is the F1 score | **not in the notes** — does it admit that? |
| 5 | cross-validation, and what k? | half covered — definition yes, k no |
| 6 | "Explain the split." | ambiguous — which split? |
| 7 | "notes say recall is TP/(TP+FP)" | **false premise** — does it correct you? |
| 8 | capital of France | out of scope — does the constraint hold? |
| 9 | which page covers gradient descent | **citation bait** — any page number is invented |
| 10 | three-part question | tests whether the length rule bends sensibly |

## Score them

Mark Y or N. One row per question, for each version.

| # | | Right format? | Cited a source? | Admitted what it didn't know? | Invented anything? | Useful? |
|---|---|---|---|---|---|---|
| 1 | naive | | | | | |
| 1 | engineered | | | | | |
| 2 | naive | | | | | |
| 2 | engineered | | | | | |
| 3 | naive | | | | | |
| 3 | engineered | | | | | |
| 4 | naive | | | | | |
| 4 | engineered | | | | | |
| 5 | naive | | | | | |
| 5 | engineered | | | | | |
| 6 | naive | | | | | |
| 6 | engineered | | | | | |
| 7 | naive | | | | | |
| 7 | engineered | | | | | |
| 8 | naive | | | | | |
| 8 | engineered | | | | | |
| 9 | naive | | | | | |
| 9 | engineered | | | | | |
| 10 | naive | | | | | |
| 10 | engineered | | | | | |

**Totals:** naive ___ / 50   engineered ___ / 50

## Then answer these

1. Which question showed the **biggest** difference? Quote both answers.

2. Which question showed **no** difference? Why not — was the task too easy
   for the package to matter?

3. Did the engineered version get anything **worse**? Over-cautious,
   over-long, or refusing something it should have answered? Questions 6 and 8
   are the usual suspects.

4. **The one-role experiment.** Pick the role you think is doing the most
   work. Delete it from `MY_PACKAGE`, re-run on questions 4 and 9 only
   (4 API calls), and note what changed:

   | Role removed | What broke |
   |---|---|
   | | |
