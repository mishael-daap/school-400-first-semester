# Presenter 4 — Monitoring and Control

**Slides:** 27 → 31 (Act 4)
**Target:** 4 minutes for five slides — 45 seconds each
**Spine:** *We never asked "does it feel on track?" We asked "what are the four numbers this week?"*

Read the bold lines as they are. The grey notes are for when you lose your place.

---

## SLIDE 27 · FOUR NUMBERS · 0:00 – 0:55

**"Thank you, [previous speaker]. So the software was being built. The real question is whether it was on time, on budget, and actually working."**

**"We didn't answer that with a feeling. We answered with four numbers, on one screen, every week."**

Then read them like a doctor reading results:

- **Schedule: 62% done, against 80% planned.**
- **Budget: 11% over.**
- **27 open defects, 9 of them high severity.**
- **71% of tests passing, against a 95% target.**

**"Every one of those numbers has a name and a date behind it. The 40-second booking time was our headline KPI, and we timed it on a real phone, on the hospital wifi, not on a developer's laptop."**

**"Four numbers, one screen. If a number moves, someone explains why that week."**

*Cue: the slide already says 62 / 11 / 27 / 71. Do not re-read it slowly — say what it means. Month four: we were behind, over, and not yet good enough.*

---

## SLIDE 28 · PLANNED VS ACTUAL · 0:55 – 1:40

**"This is the same four numbers as a table, because a table forces a verdict."**

- Schedule: planned 80, actual 62. **Behind.**
- Cost: planned on budget, actual +11%. **Over.**
- Quality: target 95, actual 71. **Below bar.**
- Scope: no changes planned, two came in. **Controlled.**

**"Look at the fourth row. Two change requests, and the project still says controlled. That is not luck. That is change control working."**

**"The lesson on this slide is one line: silence is the failure mode, not the variance. A number going the wrong way is information. A number nobody mentions is how projects die."**

*Cue: we tracked against the Gantt chart from planning, plus a weekly status report. Same baseline every week, or the comparison means nothing.*

---

## SLIDE 29 · QUALITY BELOW EXPECTATIONS · 1:40 – 2:25

**"So what do you do when the quality number is 71 and the target is 95? You stop."**

**"We delayed the release by a week rather than ship a faulty booking module. That decision cost us a week. Shipping it would have cost us the hospital's trust."**

The sequence, in order:

1. Stop the release.
2. Find the cause — it was the booking rule, not the screen.
3. Fix it in the database, where the rule lives.
4. Retest with two sessions racing for the same slot.
5. Release, and log what happened.

**"A defect found in testing is a bug. The same defect found by a patient is a reputation."**

*Cue: this is your strongest slide. Slow down. The point is that quality is a decision with a cost, and we paid it.*

---

## SLIDE 30 · RISKS AND EXTRA REQUIREMENTS · 2:25 – 3:10

**"Now back to something from initiation. Two of our feasibility answers came back conditional."**

**"Can staff actually use it? Can we protect the records? Those weren't answered once at the start and forgotten. They sat in the risk register and we reviewed them every week."**

One concrete example:

**"The SMS service was a single point of failure. If it went down, the patient gets no confirmation and turns up unsure. So we built a backup: if the SMS fails, the confirmation goes out by email instead. The booking still holds."**

**"And every new request went into a log. Two came in, both costed, both decided by the sponsor. Nothing was built because someone asked nicely in the corridor."**

*Cue: the risk register had one owner per risk. The requirement log had one decision per request.*

---

## SLIDE 31 · CHANGE CONTROL AND CORRECTIVE ACTION · 3:10 – 4:00

**"Last slide, and it's the rule that kept the other four honest: nothing is built without a written request."**

**"No request, no impact check, no build. Not because we liked paperwork, but because an unrecorded change is a change nobody can cost, test or defend later."**

**"And when something did go wrong, the corrective action was always the same four steps: fix it, retest it, re-sequence the plan, report it."**

**"We re-baselined openly. The sponsor saw the new date and the new number in the same week we did."**

**"That is monitoring and control. [P5] will show you what happened when we closed it."**

*Cue: end on the handoff. Do not add anything after it.*

---

## CUE CARD — print or keep on your phone

```
27  FOUR NUMBERS, ONE SCREEN
    62% vs 80 planned | +11% budget | 27 defects (9 high) | 71% vs 95
    KPI: 40-second booking, timed on a real phone
    If a number moves, someone explains why.

28  PLANNED vs ACTUAL
    Behind · Over · Below bar · Controlled (2 changes)
    Silence is the failure mode, not the variance.

29  QUALITY 71 vs 95
    Stop the release. Find the cause. Fix the rule, not the screen.
    Retest two sessions racing for one slot.
    Bug in testing = bug. Bug in front of a patient = reputation.

30  RISKS + EXTRA REQUESTS
    Conditional feasibility answers: can staff use it, can we protect records.
    SMS down -> email fallback, booking still holds.
    Two requests, both logged, both decided by the sponsor.

31  CHANGE CONTROL
    No request, no impact check, no build.
    Corrective action: fix, retest, re-sequence, report.
    Hand off: "[P5] shows what happened when we closed it."
```

---

## IF THEY ASK

**"62% against 80% — was the project failing?"**
No. It was behind and we knew it in month four, with two months left. The failure would have been finding out in month six.

**"Why 11% over budget?"**
Mostly people cost and the extra week of testing. We reported it the week it happened, not at closure.

**"If you were behind, why delay the release too?"**
Because the booking module was the product. Shipping a module that double-books would have failed the one objective the hospital actually cares about.

**"How is a 40-second booking time measured?"**
From tapping "book" to seeing the confirmation, on a normal phone, on the hospital network, at peak time. Not on a developer machine.

**"What is the difference between monitoring and control?"**
Monitoring is the numbers. Control is what you do when they move: fix, retest, re-sequence, report. A report with no action is just a diary.

**"What could go wrong, and what would you do?"**
SMS provider dies → email fallback already built. A high-severity defect appears late → stop the release, fix, retest, tell the sponsor the new date that same week.

---

## DELIVERY NOTES

- Five slides in four minutes is fast. 45 seconds each, and the numbers are on screen — you are interpreting, not narrating.
- The one line to land: **"Silence is the failure mode, not the variance."**
- Month four is the emotional turn of the presentation: we were behind. Say it plainly, then show that we knew and acted. That is more credible than a clean story.
- Do not read the table on slide 28 row by row in a monotone. Read the verdict words: behind, over, below bar, controlled.
