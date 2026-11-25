# Presenter 4 — say this

Slides 27 → 31. About 3 minutes 15. Swap [P5] for the next speaker's name.

---

## 27 · THE SCREEN

We're at month four. It's a six-month project, so there are two months left. This is the screen I looked at every Monday.

Four numbers. Schedule, 62% done, against 80% planned. Budget, 11% over. Twenty-seven open defects, nine of them serious. Tests passing, 71%, against a target of 95.

I'll say it plainly. We were behind. And the numbers sat on one screen where I couldn't argue with them.

## 28 · THE VERDICT

Same four numbers against the plan, so each one gets a verdict. Behind. Over. Below the bar. Scope, controlled. Two change requests came in and both went through the process, so scope didn't run away from us.

Bad numbers happen on every project. What matters is when you find out. We found out in month four, not month six. Silence is what kills a project, not a number.

## 29 · QUALITY

So quality is 71 against 95. What do you do with that? Ship it and hope, or stop?

We stopped. We lost a week.

Here's the bug. Two receptionists, same doctor, same 10:30. Both click book at the same second. Both get "this slot is free." Both save. Two patients, one slot.

The check was on the screen. The screen asks, gets a yes, and saves. Two people asking at the same time both get a yes.

So we fixed it where it can't be raced. The database now allows one appointment per slot, full stop. The second save fails, whatever the screen thought.

Then we tested it the only way that proves anything. Two bookings fired at the same instant. Not one after the other, because that test passes even while the bug is there.

## 30 · RISKS AND REQUESTS

Back to initiation for a second. Two of our feasibility answers came back conditional. Can staff actually use it? Can we protect the records? Those went on the risk register and we reviewed them every week.

One example. The SMS service. If it fails, the patient gets no confirmation and turns up unsure. So we built an email fallback. The booking still holds.

And two new requests came in during the project. Both logged, both costed, both decided by the sponsor. Nothing got built because someone asked nicely in the corridor.

## 31 · THE RULE

Which brings the rule. Nothing is built without a written request. No request, no impact check, no build.

And when something breaks, the response is always the same. Fix it. Retest it. Re-sequence the plan. Report it. The sponsor heard the new date in the same week we did.

That's monitoring and control. [P5] will take you through closure.

---

## DELIVERY

- 29 is the one to slow down on. The week we lost is the most believable thing in the story.
- Don't read the table. Read the verdicts: behind, over, below the bar, controlled.
- If you're running late, cut 30 to two sentences: the conditional answers, and the SMS-to-email backup.
- The race explanation is the whole point of 29. If the audience doesn't understand "two people clicking at once," the fix sounds like magic.
