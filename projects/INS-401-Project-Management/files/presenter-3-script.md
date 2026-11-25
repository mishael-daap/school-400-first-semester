# Presenter 4 — Execution (and Planning)

> Your group outline labels this block "Presenter 3". You speak fourth. Slides and content are
> unchanged; only the handoff name changed, because you now hand off to the next speaker, not to P4.

**Slides:** 11, 12, 13 → bridge into execution
**Target:** 4 minutes (30 min ÷ 7 presenters ≈ 4:15 each)
**Spine:** *We promised five things, refused five, staffed five people, and proved it every Friday.*

Read the bold lines as they are. The notes under them are for when you lose your place.

---

## SLIDE 11 · SCOPE · 0:00 – 1:15

**"Thank you, [previous speaker]. So we had a plan, a price and a date. Now the hard part: what exactly did we promise to build in six months?"**

**"This slide is the answer, and it is deliberately short. Five things in, five things out."**

**In:** registration and login; online booking, reschedule and cancel; the doctor list with live availability; SMS or email confirmation; staff management of patient records.

**Out:** billing and insurance, pharmacy and laboratory, full clinical notes, telemedicine, and a native mobile app.

**"Why so strict? Because each one of those is a project by itself."**

- Billing needs the hospital's finance system.
- Pharmacy needs stock and a supplier feed.
- Telemedicine needs video infrastructure and a second legal conversation.
- A native app is the same product built twice.

**"We had six months, so every yes had to survive one question: does this help a patient get an appointment? If it doesn't, it waits."**

**"And we wrote the exclusions down and got them signed at planning. That is why, in month three, when someone asked for pharmacy, we could point at a page instead of arguing in a corridor."**

*Cue: pause after "five things out." Let them read the two columns. Do not read all ten items in a flat list.*

---

## SLIDE 12 · FEATURES · 1:15 – 2:10

**"So what are those five things made of? Three groups of features. Each group answers an objective from the charter."**

**Group one, the patient.** Register, log in, book, reschedule, cancel. That is the waiting-time objective.

**Group two, visibility.** See the doctors, see what is genuinely open, get a confirmation by SMS or email. That kills double booking, and it removes most of the phone calls to reception.

**Group three, staff.** Search a patient, manage the day's list, block a slot when a doctor is called away. That is the one-record objective.

**"Notice what is missing. No chatbot, no ratings, no medical history upload."**

**"A feature list is not a wish list. Every line here has a name next to it and a test that proves it works."**

*Cue: point at the phone mock-up on the left when you say "see what is genuinely open." It is the same three doctors from slide 5 — the story is continuous.*

---

## SLIDE 13 · RESOURCES · 2:10 – 3:05

**"To build that in six months we needed five people, not fifteen."**

**"A manager, developers, a database administrator, a designer, and testers. That is it. Small on purpose."**

Then the split, fast:

- **Manager** plans, tracks, controls change, reports. He does not code.
- **Developers** build the four modules.
- **DBA** owns the schema and the booking rule.
- **Designer** owns the screens.
- **Testers** test and log defects.

**"The technical side is hosting, the database, the machines and the test devices. The services are version control, and the SMS and email gateway."**

**"Why this shape works: every role owns something you can see and test. When the booking rule broke, we knew whose desk it landed on."**

*Cue: the DBA line is the important one. The rule that stops double booking lives in the database, not in the screen. Say it like it matters, because slide 24 proves it.*

---

## BRIDGE INTO EXECUTION · 3:05 – 4:00

**"Planning gave us three things: a boundary, a list, and a team. Execution is where those three meet reality."**

**"For three months the team built, integrated, reviewed and reported. Every single week."**

- Fifteen-minute stand-up every morning, to surface blockers.
- One board. One owner and one status per task.
- Git for every change, sprint planning every two weeks.
- A working demo to the sponsor on Friday. Not a status report — the actual software.

**"Tools and techniques: Agile with Scrum ceremonies, Git, sprint planning. The documents that came out of it: the SRS and the resource allocation plan. The deliverables: working modules — login, booking, SMS confirmation — and the technical documentation."**

**"That is the build. [P5] will show you what we measured while it was happening."**

*Cue: if you are the last speaker before a break, this is your exit line. Do not add anything after the handoff.*

---

## IF YOU ALSO OWN SLIDES 22–26 (90 seconds)

Only use this if the group gives you the execution act. Otherwise stop at the bridge.

**Slide 22 — activities.** "Build, integrate, review, communicate. Developers build the four modules, the DBA secures the database, the manager coordinates and reports." Then the line that lands: **"Execution is judged by the Friday demo, not by the timesheet."**

**Slide 23 — registration and booking.** "A validated form, one patient ID, and a slot that locks on confirm. Mrs Okafor picks 10:30 and the slot closes behind her."

**Slide 24 — the database.** "Six tables. The one that matters is `UNIQUE (schedule_id)`. One slot can hold exactly one appointment. We put that rule in the schema, not the screen, because two people clicking at the same second both pass a screen check."

**Slide 25 — coordination.** "Stand-up, visible board, weekly demo. When a task slipped: find the cause, reassign, tell the sponsor."

**Slide 26 — extra features.** "It goes through change control and gets assessed before anything is built. The request is logged, never built quietly."

---

## CUE CARD — print or keep on your phone

```
11 SCOPE
  5 in : login · booking · availability · SMS/email · staff records
  5 out: billing · pharmacy · clinical notes · telemedicine · native app
  One question per yes: does it get a patient an appointment?
  Signed exclusions beat corridor arguments.

12 FEATURES
  Patient: register, book, reschedule, cancel      -> waiting time
  Visibility: doctors, open slots, confirmation    -> no double booking
  Staff: search, day list, block slots             -> one record
  A feature list is not a wish list.

13 RESOURCES
  5 people: manager · devs · DBA · designer · testers
  Manager does not code. DBA owns the booking rule.
  Tech: hosting, DB, devices. Services: Git, SMS/email.
  Every role owns something you can see and test.

BRIDGE
  Boundary + list + team -> meet reality.
  Stand-up, board, Git, sprint, Friday demo of the software.
  SRS + resource plan -> working modules + docs.
  Hand off: "[P4] shows what we measured."
```

---

## IF THEY ASK

**"Why not billing or pharmacy?"**
Each is a separate system with its own integrations and its own risk. Adding one would have pushed go-live past six months. We listed them as phase two, in writing.

**"No clinical notes — how do doctors work?"**
They keep their current notes process. This system owns appointments and the patient record, not diagnosis. Mixing the two would have doubled the scope and the legal exposure.

**"Did you get scope creep?"**
Two requests came in during execution. Both were logged, costed, and decided by the sponsor. One was deferred to phase two. Nothing was built quietly.

**"Waterfall or Agile?"**
Hybrid, and on purpose. The boundary — scope, budget, six months — was fixed up front. Inside that boundary we built in two-week sprints with a demo every Friday.

**"How do you actually stop double booking?"**
A unique constraint on `schedule_id` in the database, so a second booking on the same slot fails at the data layer. Then a test with two sessions racing for the same slot. A screen check alone loses that race.

**"What would you do differently?"**
At month four we were at 62% against a planned 80%. Our testing estimates were optimistic. I would estimate testing at double what feels comfortable, and start it earlier.

**"What could go wrong, and what would you do?"** (the closing activity question)
A module ships late: cut the lowest-value feature, not the testing. A key person leaves: the DBA documents the schema and the rule. The hospital asks for extras: change control, sponsor decides, baseline updated.

---

## DELIVERY NOTES

- 4 minutes is about 560 spoken words. The script above is 570. If you run long, cut the "why so strict" list on slide 11 to two examples.
- Do not read the slide. The audience can read. Say the one sentence the slide cannot say.
- Your three slides are all "planning". The transition is the whole job: land on "execution is where the plan meets reality," then hand off cleanly.
- Numbers to have ready: five in, five out, five people, six months, three months of execution, four modules, weekly demo.
