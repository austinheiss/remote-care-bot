# Peer design review notes

Project: In-Home Assistive Robot  
Team: Gavin Lamphier, Liam Patel, Austin Heiss  
Status: Feedback recorded; follow-up validation open.  
Reviewer: Clare Hooper (mirror project).  
Review date: October 26, 2026.  
Feedback reported by: Austin Heiss, November 11, 2026.  
Last updated: November 11, 2026.

## Reviewing-team coverage

The recorded reviewer is Clare Hooper (mirror project). Austin reported three feedback themes from her. These notes cover that reported feedback. The statements below are paraphrases, not direct quotations. Bathroom safety and camera privacy are separate actions arising from one theme.

## Follow-up schedule

The written design revisions for PR-01 through PR-04 were applied on November 11, 2026. Their proposed verification follow-up target is November 18, 2026, aligned with presentation preparation. The final design report is due December 2, 2026. These are proposed planning dates for the follow-ups. Proposed dates do not imply that the physical, privacy or usability checks are complete.

## Peer action items

| ID | Criterion | Issue and reviewing team | Concrete action | Owner | Priority | Due date | Status and design link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PR-01 | Risk | Robot may be too short to notice and become a trip hazard. Clare Hooper (mirror project); reported by Austin. | Define visibility/stability/clearance/reach and parking criteria for both base candidates; require full-scale mockup comparisons before dimensions are approved. | Liam Patel; Gavin Lamphier assists | Must-fix | Design revision: November 11, 2026 (applied); verification: November 18, 2026 (proposed) | Visibility/parking design updated for both base candidates; mockups/physical checks open. D2 Robot platform, D-NF10, E49, R8, Figure 2. |
| PR-02 | Risk | Bathrooms present slip/injury concerns and the robot could add an obstruction. Clare Hooper (mirror project); reported by Austin. | Specify a guarded route, local armArea/expiry and profile-specific stop behavior; define supported tests for boundary/guard uncertainty before motion. | Liam Patel; Austin Heiss assists | Must-fix | Design revision: November 11, 2026 (applied); verification: November 18, 2026 (proposed) | Guarded trial, armArea and expiry/recovery design specified; physical checks open. D2 Local authority/motion, D-NF11, E50, E53-E56, R9, Figure 2. |
| PR-03 | Risk | Cameras in or aimed toward the bathroom threaten privacy. Clare Hooper (mirror project); reported by Austin. | Specify full-route bathroom-view exclusion, shared media/tracking capture revocation and the hardware gate; define shutdown/off/unknown checks. No ambient microphone monitoring is added. | Austin Heiss; Gavin Lamphier assists | Must-fix | Design revision: November 11, 2026 (applied); verification: November 18, 2026 (proposed) | Shared media/tracking capture gate and revoke behavior specified; physical closure/view tests open. D2 Platform capture/local authority, D-NF12, E51, E54, E56, R9, Figures 1/2. |
| PR-04 | Clarity | Ease of use should be a primary focus for residents with varying technology familiarity and abilities. Clare Hooper (mirror project); reported by Austin. | Specify plainly labeled controls, readable non-color-only states, reachable alternate input and caregiver text-size/VoiceOver support; define key-task/error/assistance observations. | Gavin Lamphier; Austin Heiss assists | Must-fix | Design revision: November 11, 2026 (applied); verification: November 18, 2026 (proposed) | Interaction criteria added; formative evaluation open. D2 Resident controls/iOS, D-NF13, E52, R8, Figure 1. |

Criteria: completeness, feasibility, clarity, risk. Priorities: must-fix, worth considering, out of scope for now. The design-revision date records the document correction; the later verification dates are proposed targets, not test-completion claims. Physical and usability evaluations have not been recorded as completed.

## Feedback summary

- Risk drew the most recorded actions: three of four; clarity accounts for one. These are action counts, not reviewer counts.
- All three received themes are represented and attributed to Clare Hooper.
- D2 now records visibility/clearance and parking checks, bathroom/wet-area exclusion, camera view/privacy limits, and accessible interaction criteria. Error cases E49-E56, requirements D-NF10-D-NF13, and review-driven rationale R8/R9 trace those changes. The mechanisms now include physical trial barriers, a local expiring area permit, independent guard/enable inputs and shared capture revocation.
- No bathroom fall detector, ambient microphone monitoring, or claim of universal usability is added. Missing tests remain open.

## Feedback we gave while reviewing others

**One issue was raised (feasibility), on Clare Hooper's mirror project:** Austin emphasized that AI clothing try-on should accurately represent how garments fit the user's body rather than guess their appearance. No second issue was raised.

## Follow-up status

The received feedback, reviewer, October 26 review date and single outgoing issue are recorded. Owners should review the proposed November 18 targets and record evidence for the remaining physical, privacy and usability checks. Written design actions specify mechanisms, interfaces and fault behavior; physical/privacy/usability validation remains open. Both caster and balancing bases are being explored and must qualify separately.

D0 and D1 were not modified. Any later correction to either must name the affected file, issue, and rationale/action ID here and in D2.
