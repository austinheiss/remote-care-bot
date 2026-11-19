# Run Sheet: Remote Care Robot, Fall Design Presentation

Assignment #8 (final slide deck) and Assignment #9 (presentation video and peer reviews).

| Field | Detail |
|---|---|
| Team | Remote-Care Bot: Austin Heiss (CS), Gavin Lamphier (ID), Liam Patel (ME) |
| Advisor | Andrea Vance |
| Deck | `Presentation/Remote-Care_Bot_Presentation_Final.pptx` (PDF: `Presentation/Remote-Care_Bot_Presentation_Final.pdf`), 10 main slides + 2 backup + 1 speaker-notes slide |
| Time limit | 10:00 presenting + 5:00 questions (confirm with instructor) |
| Presentation slot | _Fill in when the randomized order is posted_ |
| Team presenting before us | _Fill in_ |

## 1. Speaking roles

| Role | Person | Notes |
|---|---|---|
| Presenter (all slides) | Austin Heiss | Sole speaker, per the team's plan on slide 13. |
| Timekeeper | Liam Patel | Holds the timer from the room. Signals at 5:00 (halfway, should be on slide 6), at 8:00 (should be on slide 9), and at 9:30 (wrap up). |
| Slide driver | Austin Heiss | Advances his own slides. |
| Q&A lead | Austin Heiss | Takes each question, answers it or hands it to the owner in section 4. |
| Q&A: mechanical, cost, CAD | Liam Patel | See owners in section 4. |
| Q&A: screens, appearance, accessibility | Gavin Lamphier | See owners in section 4. |
| Video recording and spreadsheet | Austin Heiss | Records the 5 to 10 minute video, posts the deck and video links in the team's row. |

Speaking balance: the course suggests balancing speaking time within about 30 seconds per member, and teamwork is 20% of the grade. With one presenter, Gavin and Liam's visible role is answering questions in their areas. Confirm with the instructor that a single presenter is acceptable, or move slides 6 and 8 to Liam and slide 9 to Gavin.

## 2. Slide plan

Planned total is 10:00 (600 s). The title slide is short (30 s). The other nine main slides get about 63 s each, with the last slide taking the extra seconds to land on 10:00. Backup slides 11 and 12 are only shown if a question needs them. Slide 13 (speaker notes) is not presented.

| # | Slide | Speaker | Start | Length | Hand-off line (last thing said before advancing) |
|---|---|---|---|---|---|
| 1 | Remote Care Robot (title) | Austin | 0:00 | 0:30 | "We're building a home robot that takes some of the load off caregivers. First, who we are." |
| 2 | The team | Austin | 0:30 | 1:03 | "Three disciplines, one robot, and here's the problem it addresses." |
| 3 | Abstract | Austin | 1:33 | 1:03 | "That's the goal. Here's what the people who'd use it actually need." |
| 4 | User stories (US-01 to US-05) | Austin | 2:36 | 1:03 | "Those five stories drive the design. Here's how the pieces fit together." |
| 5 | How the system fits together | Austin | 3:39 | 1:03 | "A design like this lives or dies by its constraints, so here are ours." |
| 6 | Major constraints | Austin | 4:42 | 1:03 | "With those limits set, here's what we've done so far." |
| 7 | Progress so far | Austin | 5:45 | 1:03 | "That's where we are now. Here's where we'll be by the end of the term." |
| 8 | End of term | Austin | 6:48 | 1:03 | "Getting there takes all three of us, so here's who owns what." |
| 9 | Division of work | Austin | 7:51 | 1:03 | "And here's what all of that adds up to at Expo." |
| 10 | Expected demo at Expo | Austin | 8:54 | 1:06 | "That's the Remote Care Robot. Thank you, and we're happy to take questions." |
| 11 | D0 block diagram (backup) | Austin | Q&A only | n/a | Show for questions about components or interfaces. |
| 12 | D1 call server data model (backup) | Austin | Q&A only | n/a | Show for questions about data, consent, or the server. |

Timekeeper checkpoints: on slide 6 at 5:00, on slide 9 at 8:00, on slide 10 by 9:00. If behind by 30 s or more at a checkpoint, cut detail on the next slide rather than speaking faster.

## 3. Rehearsal log

Log at least one full-group timed rehearsal. Record the real times measured; leave a row blank until it has happened.

| # | Date | Present | Timekeeper | Total | Slide 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Changes after this run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | | | | | |
| 2 | | | | | | | | | | | | | | | |
| 3 | | | | | | | | | | | | | | | |

Per-section totals (fill from the row above): Intro (slides 1 to 3): ____ · Design (slides 4 to 6): ____ · Plan (slides 7 to 10): ____

## 4. Anticipated questions

Owner is the team member who answers. Austin takes each question first and hands off by name.

| # | Question | Owner | Short answer |
|---|---|---|---|
| Q1 | How is this different from an Amazon Echo Show or a tablet on a stand? | Austin | It moves. It follows the resident between rooms during a call and can find them for a check-in, and the resident has to accept every call before the camera turns on (US-01, US-02). |
| Q2 | What stops a caregiver from watching the resident without permission? | Austin | The call and consent manager keeps video off until the resident accepts the call, video is encrypted, and no video is stored (slide 5, constraints 02 and 04). We're also adding a camera-on light and a physical lens cover (advisor feedback F15). |
| Q3 | Isn't a low robot a trip hazard for an older adult? | Liam | Yes, our advisor raised it. We're adding a high-contrast band and running lights on the base, and the robot parks at its dock or against a wall when idle instead of in walkways (F1). |
| Q4 | Can someone in a wheelchair or with limited reach use the screen? | Gavin | The base stays low for stability, but the screen rises on the telescoping mast to seated eye level during calls. Every resident action works by voice or one large button, with no fine-motor gestures (F2, F4). |
| Q5 | How will fall detection work, and how accurate will it be? | Austin | Not fully answered yet. We've moved fall detection (US-04) earlier in the plan and are adding a fallen-person case to the MuJoCo simulation. Our next step is to pick the detection approach and measure it in simulation before any accuracy claim. |
| Q6 | What will it cost, and who pays for it? | Liam | Not fully answered yet. The budget is funded but the price isn't set. Our next step is a target price and a draft bill of materials from the end-of-term parts selection, due Dec 2. The argument for buyers is reduced caregiver burden and injury cost (F12, F14). |
| Q7 | Why not let it dispense medication or care for pets? | Austin | Both need an arm and secure storage, which is outside our product scope, and dedicated pill dispensers already exist. We support medication through spoken reminders with a "taken" or "missed" status in the caregiver app instead (F6, F7, F11). |
| Q8 | What happens in the bathroom, where most falls happen? | Austin | The robot doesn't enter or turn on its camera there. It waits outside the door, does audio-only check-ins, and alerts the caregiver if the resident doesn't answer (F13). |
| Q9 | How does it stop safely if something goes wrong? | Liam | A wired stop button cuts motion directly through the motion controller, separate from software (slide 5). The robot also has a max speed and a minimum following distance, and stops following if it loses the resident. Physical stopping hasn't been tested yet. |
| Q10 | Why simulate in MuJoCo instead of building the robot first? | Austin | We can test following, mapping, and falls safely and repeatably before buying parts, and the same tests carry over to the physical robot in the spring. |
| Q11 | What does the caregiver app do beyond calling? | Gavin | It shows the robot's status, alerts for falls or missed check-ins, and medication reminder results. A professional caregiver role is being added with the same consent rule as family (F5, F7). |
| Q12 | What's your biggest risk for the spring? | Austin | Moving from simulation to hardware on time: parts arriving, the chassis being ready, and person following holding up in a real home. Our end-of-term parts selection and CAD mockup are aimed at reducing that. |

Q5 and Q6 are the two questions we can't fully answer yet. Answer them as "We have not resolved that yet, and here is our next step."

## 5. Day-of checklist

- Final deck uploaded to the LMS as `Remote-Care_Bot_Presentation_Final` before class starts. No edits once the team is called.
- Backup copy on USB or offline cloud storage, tested on a machine that isn't Austin's.
- Timekeeper has a phone timer ready and knows the three checkpoints.
- Listen during other teams' slots; any of us may be called on to ask a question.
