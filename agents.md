# agents.md — school

Rules for anything inside this semester. Root `agents.md` still applies.

## Three kinds of work arrive here

**Notes.** One file per course per class day: `projects/<course>/files/notes-YYYY-MM-DD.md`.

```
# **<day month year>, <HH:MM>**

---
```

- The file opens with the real clock time the file is created, 24-hour, as a bold h1.
  Nothing sits above it — no course title, no "Class notes" line, no `## Date` heading.
- After the `---`, go straight into the first section heading.
- Add each dictation as a new section: heading, then bullets or a table.
- Fix spelling and grammar. Never change content. Never add facts I did not say.
- Code examples in Java unless I say otherwise.
- Diagrams: Mermaid only, no explanation of the diagram.
- If the dictation is unclear or possibly wrong, write it as given and tell me in the reply.

**Assignments.** A lecturer hands out work. It goes in that course's `files/`, never at
semester level. Then write two lines in `activities/`: one on the day it is due, tagged with
the course, and one on the day I say I will work on it. If no due date was given, ask me.

**Announcements.** A lecturer says something that changes a date, a venue or a rule. Update
`files/MY_TIMETABLE.md` or the affected `project.md`, then tell me in one line what changed.

## Never

- Never delete a notes file. Exam revision comes from them.
- Never edit `files/student-info.md` facts without asking.
- Never merge two courses into one file.

## Logging

Append one line to `wiki/log.md` after each batch of notes or any date change.
