# Advisor Feedback: Remote Care Robot

## 1. Meeting record

| Field | Detail |
|---|---|
| Date | November 9, 2026 |
| Duration | 50 minutes |
| Attendees | Andrea Vance (advisor), Austin Heiss (CS), Gavin Lamphier (ID), Liam Patel (ME) |
| Format | Online meeting over Microsoft Teams: the team walked through the slide deck, then had an open discussion and questions with the advisor |
| Deck reviewed | The final deck, same version as submitted: 12 slides (10 main + 2 backup), committed in this repo as [`senior_design.pptx`](senior_design.pptx) (PDF: [`senior design.pdf`](senior%20design.pdf)) |

Slide key used in the log: 1 Title, 2 Team, 3 Abstract, 4 User stories, 5 System overview (D0 for the room), 6 Major constraints, 7 Progress so far, 8 End of term, 9 Division of work, 10 Expo demo, 11 D0 block diagram (backup), 12 D1 data model (backup).

## 2. Feedback log

Response is Accepted, Modified (accepted in a changed form), or Declined (with a reason). Status is Open (not started), In progress, or Closed.

| # | Slides | Advisor said | Response | Change | Owner | Status |
|---|---|---|---|---|---|---|
| F1 | 1, 6 | The robot's height is a concern for tripping and safety. | Accepted | Add "trip hazard" to the Health & Safety constraint. Give the base a high-contrast band and lights while it moves, and have it park at the dock or against a wall when idle instead of in walkways. | Liam (base), Gavin (visibility) | Open |
| F2 | 1, 6, 9 | A robot that sits down low is hard to use for people with disabilities. | Modified | Keep the base low for stability, but raise the screen on the telescoping mast to seated eye level during calls. Add a screen height range to the Accessibility constraint and check it in the full-scale CAD mockup. | Liam (CAD), Gavin (reach study) | Open |
| F3 | 3, 4, 5 | Could it be their Siri? A companion that says "hey, it's time to take your medication." | Modified | The robot's voice controls (US-03) stay limited to its own functions, home controls, and reminders. We will not build a general assistant like Siri. Medication reminders are taken up in F7. | Austin | Open |
| F4 | 4, 6 | Trouble with the bathroom, eating, and drinking is why a caretaker is in the home. Fine motor, vision, and balance limits are common, so voice activation is a plus. | Accepted | Strengthen constraint 05: every resident action works by voice or one large on-screen button, with no fine-motor gestures and large high-contrast text. | Gavin (screens), Austin (voice) | Open |
| F5 | 4, 5, 12 | Seeing into the home is a plus so doctors or professionals can check in. | Modified | Add "care professional" as a caller role in the data model, using the same consent rule as family: the resident accepts every call (US-02). There is no viewing without the resident's acceptance. | Austin | Open |
| F6 | 4 | Caretakers don't want to fill pill organizers every day, and automatic dispensers already exist. | Declined | Dispensing needs a manipulator and secure storage, which is outside our product scope (a two-wheel robot with a screen and no arm), and dedicated dispensers already do it. We support taking the medicine through reminders (F7) instead. | Austin (record) | Closed |
| F7 | 4, 10 | Residents skip medicine because they forget. | Accepted | Add a user story for medication reminders: at a scheduled time the robot finds the resident and gives a spoken reminder, the resident confirms by voice, and the caregiver app shows "taken" or "missed." | Austin (logic), Gavin (screens) | Open |
| F8 | 4 | Safety inside the home itself, for example doors left unlocked. | Modified | Extend US-03 so the caregiver app can show lock status and the resident can lock doors by voice, if a smart lock is installed. This is a stretch goal after calls and following work. | Austin | Open (deferred to spring) |
| F9 | 4, 5 | Connect to what they already do on their cellphone. | Modified | The caregiver side is already a phone app (US-05). For the resident, we will sync calendar events from their phone into reminders (F18) rather than replace the phone. | Austin | Open (deferred to spring) |
| F10 | 4, 5, 10 | Fall detection is one of the biggest problems. | Accepted | Move fall detection (US-04) earlier in the plan. Add a fall detection block to the system diagram and D0, and add a fallen-person case to the MuJoCo simulation tests. | Austin | Open |
| F11 | 4 | Pets matter a lot to elderly people: putting food in dog bowls, letting the dog out. | Declined | Feeding pets and opening doors need an arm and door actuation, which are outside our product scope. We accept one related item: pets are treated as moving obstacles in navigation and following tests, so the robot does not trip or chase them. | Austin (tests) | Closed |
| F12 | 1, 3, 6 | Decreasing caregiver burden is a big money saver, including workers' compensation costs. | Accepted | Add the cost and workers' compensation argument to the abstract and the Economic constraint, with one cited source on caregiver injury costs. | Gavin | Open |
| F13 | 5, 6 | Should this come into the bathroom with me? Falls happen most often in the bathroom. | Modified | The robot does not enter the bathroom or turn on its camera there. It waits outside the door and does audio-only check-ins, and it alerts the caregiver if the resident does not answer. | Austin (behavior), Liam (wet floor limits) | Open |
| F14 | 6 | Cost could make someone hesitant. | Accepted | Replace "budget not yet set" with a target price and a draft bill of materials, built from the end-of-term parts selection. | Liam | In progress |
| F15 | 5, 6 | "Something always watching me" and "not taking data" could make someone hesitant. | Accepted | Make the privacy rules visible on the robot: a camera-on light, a physical lens cover, and a short "no video is stored" statement on screen. Add these to the Privacy constraint. | Gavin (design), Austin (software) | Open |
| F16 | 6 | Keep a distance from personal space. | Accepted | Set a fixed minimum following distance in the design docs and in simulation, and add a voice command that sends the robot back to its dock. | Austin | Open |
| F17 | 1 | Team asked what in the robot's look or behavior would build comfort and trust. The advisor answered with small, useful features (F18) rather than looks. | Modified | Run a short appearance and behavior feedback session with caregivers or OT contacts, using the concept renders. | Gavin | Open |
| F18 | 4, 10 | Small things like calendars, appointments, and shower reminders. Think of Sims-style stats: it knows when you last ate, drank water, showered, and slept, so it knows when to remind you. | Modified | Add calendar and appointment reminders. Track "time since last" for meals, water, showers, and sleep from the resident's voice check-ins, not from constant camera watching, which would conflict with F15. Share it with the caregiver only if the resident allows. | Austin (logic), Gavin (screens) | Open |

## 3. Summary of changes

The advisor's feedback moves the project from a call-and-follow robot toward a daily companion that reminds, checks in, and detects falls. We accepted fall detection as a top priority, and accepted medication, calendar, and routine reminders as new user stories. We declined pill dispensing and pet care because both need an arm, which is outside our product scope, and dispensers already exist. The physical design will raise the screen on the mast to seated eye level while making the low base more visible to reduce tripping. Privacy stays the core trust feature: the resident accepts every call, the robot does not film in the bathroom, and the camera state is visible.

## 4. Open items

| # | Item | From | Owner | Expected close |
|---|---|---|---|---|
| 1 | Add fall detection block to system diagram and D0; add fallen-person simulation case | F10 | Austin | Dec 2, 2026 |
| 2 | Write new user stories: medication reminders, calendar and routine reminders, care professional calls | F5, F7, F18 | Austin | Nov 25, 2026 |
| 3 | Update constraints slide: trip hazard, screen height range, voice-or-one-button rule, visible privacy cues, minimum following distance | F1, F2, F4, F15, F16 | Austin, Gavin, Liam | Nov 25, 2026 |
| 4 | Add cost and workers' compensation argument with a source to the abstract and Economic constraint | F12 | Gavin | Nov 25, 2026 |
| 5 | Target price and draft bill of materials | F14 | Liam | Dec 2, 2026 |
| 6 | Raised-screen mast pose and visible base band in the full-scale CAD mockup | F1, F2 | Liam | Dec 2, 2026 |
| 7 | Add care professional role to the D1 data model | F5 | Austin | Dec 2, 2026 |
| 8 | Pets as moving obstacles in simulation tests | F11 | Austin | Jan 29, 2027 |
| 9 | Bathroom behavior: wait at door, audio-only check-in, no-answer alert | F13 | Austin, Liam | Feb 12, 2027 |
| 10 | Appearance and behavior feedback session with caregivers or OT contacts | F17 | Gavin | Feb 12, 2027 |
| 11 | Reminder screens and "time since last" tracking from voice check-ins | F7, F18 | Austin, Gavin | Feb 26, 2027 |
| 12 | Smart lock status and phone calendar sync (stretch) | F8, F9 | Austin | Mar 26, 2027 |
