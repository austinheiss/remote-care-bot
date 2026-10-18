# Assignment 4: User Stories and Use Cases

**Project:** In Home Assistive Robot / remote-care-bot  

| Team member | Discipline |
| --- | --- |
| Gavin Lamphier | Industrial Design |
| Liam Patel | Mechanical Engineer |
| Austin Heiss | Computer Science |

Our robot is a compact two-wheel robot with a front-facing screen and no arm. It lets a family caregiver have a video conversation with an older or disabled adult at home, and it can follow the resident from room to room so the conversation doesn't have to end when they get up. The resident decides when calls start, when the robot follows, and when it stops.

## 1. Stakeholder map

| Category | Specific roles | Needs |
| --- | --- | --- |
| Primary | Older or disabled adult who lives alone or spends much of the day alone | Keep talking with family while moving around the home; decide who can see them and when. US-01, US-02. |
| Secondary | Remote family caregiver (for example, an adult child in another city) | Understand what actually happened when a call doesn't connect, without guessing about the resident's health. US-03. |
| Hidden | Other people in the home, such as a spouse, roommate or visitor | Not be followed, filmed or bumped into by a robot that isn't there for them. US-04. |
| Hidden | Residents who use a wheelchair or have limited reach or dexterity | Use the robot's controls and screen from a seated position. US-05. |

## 2. User stories

### US-01 - Keep a call going while moving to another room

**Category:** Primary - older adult who lives alone.  
**Story:** As an older adult on a video call with my daughter, I want the call to come with me when I walk to another room, so that I don't have to end the conversation or shout across the house.

| INVEST | Self-check |
| --- | --- |
| Independent | Builds on an accepted call but delivers its own value: the conversation survives a room change. |
| Negotiable | How the resident asks the robot to follow is left open. |
| Valuable | The conversation continues instead of being cut short. |
| Estimable | One short route on one floor at the robot's tested speed of 0.2 m/s. |
| Small | One resident-requested room change; stairs and remote driving are excluded. |
| Testable | UC-01 and AC-01.1 to AC-01.3. |

### US-02 - Decide before the camera turns on

**Category:** Primary - older adult who lives alone.  
**Story:** As an older adult who lives alone, I want to accept or decline each caregiver call before my camera and microphone turn on, so that no one can see or hear into my home without my say-so.

| INVEST | Self-check |
| --- | --- |
| Independent | Works with the robot stationary and without following. |
| Negotiable | How the call is announced and answered is left open. |
| Valuable | The resident stays in control of their own privacy. |
| Estimable | One incoming call from one named caregiver. |
| Small | Accept, decline or end a single call. |
| Testable | AC-01.1 and AC-02.2. |

### US-03 - Understand why a call didn't connect

**Category:** Secondary - remote family caregiver.  
**Story:** As a family caregiver who lives in another city, I want to know whether my parent declined my call, didn't answer, or the robot lost its connection, so that I don't mistake a dropped call for my parent being fine or being in trouble.

| INVEST | Self-check |
| --- | --- |
| Independent | Can be tested with simulated call outcomes, without the robot moving. |
| Negotiable | Wording and layout of each outcome are left open, as long as each one looks different. |
| Valuable | The caregiver can decide whether to try again, call another way, or wait. |
| Estimable | Four outcomes: connected, declined, no answer, connection lost. |
| Small | One call attempt; emergency alerts and health monitoring are excluded. |
| Testable | UC-02 and AC-02.1 to AC-02.3. |

### US-04 - Don't get followed by mistake

**Category:** Hidden - spouse, roommate or visitor in the home.  
**Story:** As a spouse who shares the home, I want the robot to stop rather than start following me when I walk between it and my partner, so that it doesn't trail me around the house or run into me.

| INVEST | Self-check |
| --- | --- |
| Independent | Can be tested with recorded camera footage before any motors are involved. |
| Negotiable | How the robot tells people apart is left open. |
| Valuable | Other people in the home aren't followed or bumped. |
| Estimable | One other person crossing the robot's view. |
| Small | One crossing event during one follow. |
| Testable | AC-01.3. |

### US-05 - Reach the controls from a chair

**Category:** Hidden - resident who uses a wheelchair.  
**Story:** As a resident who uses a wheelchair, I want to reach the robot's stop and privacy controls from my seat, so that I can end a call or stop the robot without standing up or asking for help.

| INVEST | Self-check |
| --- | --- |
| Independent | Can be tested on a bench mockup with no call or movement. |
| Negotiable | Where the controls go is left open; the screen sits only about 24 cm above the floor today, so they may need to be separate from it. |
| Valuable | The resident keeps control without depending on someone else. |
| Estimable | Two controls tested from one seated position. |
| Small | Reach and press only; screen readability is a separate story. |
| Testable | A seated tester presses stop and privacy without leaning out of the chair, in 3 of 3 tries. |

<!-- PDF_PAGE_BREAK -->

## 3. Use cases

### UC-01 - Continue a caregiver call into another room

**Linked story:** US-01 (also covers US-02 and US-04).  
**Primary actor:** Resident.  
**Secondary actors:** Remote caregiver; other people in the home.

**Preconditions:**

1. Caregiver C has the resident's permission to call, and FOLLOW is turned off.
2. The robot is parked next to the resident on a cleared single-floor route.
3. Both devices are online and send a heartbeat once per second.

**Main success flow:**

1. **Caregiver:** Calls the resident.
2. **System:** Announces the call with C's name. The camera and microphone stay off.
3. **Resident:** Accepts the call.
4. **System:** Starts the call and shows that the camera and microphone are on.
5. **Resident:** Asks the robot to follow and walks toward another room.
6. **System:** Follows the resident at no more than 0.2 m/s and keeps the call going.
7. **Resident:** Stops in the new room.
8. **System:** Stops within 1 m of the resident and keeps the call going.
9. **Resident:** Ends the call.
10. **System:** Turns off the camera and microphone, turns FOLLOW off, and shows Ended.

**Alternate flow A1 - Resident declines:** At step 3, the resident declines. The system tells C the call was declined, and the camera and microphone never turn on.

**Exception flow X1 - The robot loses the resident:** During step 6, the resident leaves the camera's view or another person walks between them. The robot stops and stays stopped, the call continues from where it stopped, and the screen asks the resident to restart following. It never starts following someone else on its own.

**Postcondition:** The call has ended, the robot is stopped and FOLLOW is off. No audio or video was recorded.

### UC-01 acceptance criteria

1. **AC-01.1 - Consent before camera (main flow).** **Given** the UC-01 preconditions, **When** C calls, **Then** the resident sees C's name within 2 seconds, and the camera and microphone stay off until the resident accepts.
2. **AC-01.2 - Following during a call (main flow).** **Given** an active call with FOLLOW on, **When** the resident walks 5 m to another room and stops, **Then** the robot never exceeds 0.2 m/s, stops within 1 m of the resident, and the call stays connected the whole time.
3. **AC-01.3 - Target lost (X1).** **Given** the robot is following during a call, **When** the resident leaves the camera's view or another person crosses between them, **Then** the robot's travel request drops to zero within 1 second, it settles within 25 mm of where it lost the resident, its speed stays under 5 mm/s for a full second within 10 seconds of the loss, the call stays connected, and the robot doesn't move again until the resident restarts following.

<!-- PDF_PAGE_BREAK -->

### UC-02 - Find out why a call didn't connect

**Linked story:** US-03.  
**Primary actor:** Remote caregiver.  
**Secondary actors:** Resident; the robot.

**Preconditions:**

1. Caregiver C has the resident's permission to call.
2. The robot is online and no call is active.

**Main success flow:**

1. **Caregiver:** Calls the resident.
2. **System:** Shows C that the robot is ringing.
3. **Resident:** Accepts the call.
4. **System:** Shows C that the call is connected.

**Alternate flow A1 - No answer:** At step 3, the resident doesn't respond for 60 seconds. The system stops ringing and shows C "No answer". It doesn't suggest anything about the resident's health.

**Exception flow X1 - Connection lost:** At any step, no heartbeat arrives from the robot for 5 seconds. The system ends the attempt and shows C "Robot offline" with the time it was last online.

**Postcondition:** C sees exactly one outcome: Connected, Declined, No answer or Robot offline.

### UC-02 acceptance criteria

1. **AC-02.1 - Connected (main flow).** **Given** the UC-02 preconditions, **When** the resident accepts, **Then** C sees Connected within 2 seconds.
2. **AC-02.2 - Declined (US-02).** **Given** the robot is ringing, **When** the resident declines, **Then** C sees Declined within 2 seconds, and the resident's camera and microphone never turned on.
3. **AC-02.3 - Robot offline (X1).** **Given** the robot is ringing or connected, **When** 5 seconds pass without a heartbeat, **Then** C sees Robot offline and the time it was last online, and never sees Connected or No answer for that attempt.
