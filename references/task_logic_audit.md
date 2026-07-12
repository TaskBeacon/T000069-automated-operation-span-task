# Task Logic Audit

## 1. Paradigm Intent
Automated Operation Span measures verbal working-memory capacity while attention alternates between arithmetic processing and serial letter storage.

## 2. Block/Trial Workflow
Instruction -> 15 math-practice items -> personalized math deadline -> three combined practice sets of size 2 -> 15 scored sets (sizes 3-7, three each, randomized) -> summary. Within each set: `(solve operation -> verify TRUE/FALSE -> letter 800 ms)` repeated N times -> ordered recall -> set feedback 2000 ms.

## 3. Condition Semantics
Set size is the number of interleaved operation-letter pairs. Main set sizes 3, 4, 5, 6, and 7 occur three times each. Proposed arithmetic answers are balanced true/false. Letters are sampled without replacement from F, H, J, K, L, N, P, Q, R, S, T, Y.

## 4. Response and Scoring Rules
SPACE advances after mental solution; F=False and J=True judge the proposal. Recall uses the twelve letter keys in serial order. A letter is total-correct only if recalled in its original position. Absolute span sums set sizes for perfectly recalled sets. Math accuracy below 85% flags the score as invalid rather than changing recall credit.

## 5. Stimulus Layout Plan
Arithmetic and letters are centered. Recall shows a compact two-row letter matrix, the current serial position, and chosen letters. No operation and letter are concurrently visible.

## 6. Trigger Plan
Distinct triggers mark operation, verification, letter, recall, feedback, true/false responses, letter responses, and timeout, plus experiment/block boundaries.

## 7. Architecture Decisions (Auditability)
Each preplanned condition contains the complete set, allowing operation truth, letter order, and set size to be replayed. `run_trial.py` only sequences preplanned items with StimUnit. PsyFlow owns trial IDs, responses, triggers, timing, and phase data.

## 8. Inference Log
Keyboard responses replace the source mouse interface without changing choice semantics. A 30-second per-letter recall ceiling prevents indefinite sessions; source recall was untimed. Arithmetic templates use integer-valued one- and two-step operations matched to the source examples.
