# In-Home Assistive Robot

**Design Constraints and ABET Concerns | Assignment #7 | November 11, 2026**  
Gavin Lamphier - Industrial Design; Liam Patel - Mechanical Engineering; Austin Heiss - Computer Science

This essay records the current project position for the Fall presentation and Final Design Report section 5. It is reconstructed now from the team's D0-D2 design and Senior Design research, rather than backdated as an earlier submission. The four named concerns in the ethics assignment are retained exactly; Economic, Environmental and Sustainability, Health and Safety, and Social and Political complete the eight-area working outline. The original Assignment #7 heading/rubric text was not supplied, so its exact labels still need comparison.

Our initial assessed design is a resident-controlled call with optional, explicitly requested following on one supervised indoor route. The resident can decline or end a call and independently stop following. The November 9 direction excludes robot arms. A passive carrier, adjustable display, reminders and home controls remain separate investigations; the stationary reminder prototype is evidence of software work, not approval to expand the mobile requirement baseline. [Senior Design overview](https://chatgpt.com/space/page_1fb1e8ba871081918852073408726806), [D2](Design_Diagrams/D2_Detailed_Design.pdf).

## Economic

The relevant cost is a maintainable complete system, including controls, sensing, protective power hardware, fabrication, recurring services and repair. A low motor or board price does not establish that the robot is affordable. The parts research compares an articulated Beni-style platform with a statically supported two-drive-wheel/caster alternative. The articulated option carries additional drive, balancing, power and impact-validation work; the simpler alternative gives up stairs and Beni-like agility. These are parallel trade studies, not a selected bill of materials. No approved final budget or purchasing decision is recorded.

For the first demonstration, an existing computer and fixed screen can reduce new purchases while the team measures the actual call/perception load. Nearby or hosted inference adds network dependence and operating costs, so it cannot replace local Stop/Privacy or the control watchdog. Compare a complete, quoted configuration with available funds and a separately stated contingency. Include API/relay traffic and replacement parts before claiming that a particular architecture saves money. [Parts and cost study](https://chatgpt.com/space/page_1c8ef7a27a9c819191665c88417497bf), [compute comparison](https://chatgpt.com/space/page_8492fea412c88191896bbdbe7c139adb).

## Environmental and Sustainability

Compute, screen, continuous balancing and any offboard inference consume energy even when the robot is not traveling. Their combined battery-side load, thermal behavior and useful runtime remain to be measured on an assembled configuration. The team therefore cannot infer runtime from a processor power rating or battery watt-hours alone. A fixed, supported platform and a smaller measured compute workload are comparison cases, not assumed equivalent replacements for the mobility concept.

Liam's custom platform should provide service access to the battery, wiring, display and wearing parts so a failed module does not require discarding the whole robot. Parts selection must account for compatible charging/protection, connector strain relief, material use and eventual battery/electronics disposal. Reusing an existing computer and testing fit with reversible mockups can reduce waste before fabrication. These are implementation criteria; no lifecycle assessment, recycling arrangement or measured energy saving has been completed.

## Health and Safety

The robot can obstruct a doorway, trip a person, contact a foot or mobility aid, tip when touched, or fail to stop after losing its target. A powered balancing base may fall if torque is simply removed. D2 therefore separates a controlled stop, maintained stabilization and fault isolation in a support fixture; the caster candidate has its own rolling/braking qualification. Neither profile inherits the other's evidence. Bathrooms, wet floors and stairs remain outside the initial route and camera view.

Motion defaults disabled until the actual geometry, feedback, independent clearance, guards and stopping envelope are qualified. The 0.2 m/s absolute cap is a design limit, not demonstrated safe operation. A candidate lower cap must satisfy the measured loss-to-braking envelope; command zeroing is separate from settling within 25 mm and below 5 mm/s for one second within ten seconds. Simulation and a passing media demo do not establish these physical results. Liam owns physical evidence with Austin's controller/adapters; Gavin checks visibility, parking, reach and usable local controls. [D2 motion/platform and PR-01-PR-03](Design_Diagrams/D2_Detailed_Design.pdf).

<!-- pagebreak -->

## Ethical

A caregiver's convenience does not override the resident's control over observation or movement. The concrete boundary is separate CALL and FOLLOW permission, a named incoming caller, explicit acceptance, a selected person, reachable Stop/Privacy, and no automatic resumption after revocation or reconnect. Full Privacy also closes tracking capture; stopping only the outgoing call stream would leave an unjustified camera consumer. A visitor must not become the replacement target after an occlusion.

These choices apply ACM 1.2/1.6 through harm prevention and task-limited collection, and NSPE's public-welfare principle through withholding unqualified movement. Unanswered calls and reminder responses remain communication/self-report outcomes. Help research distinguishes a request, delivery, acknowledgment and actual assistance without promising emergency response. Supported decision-making or substitute consent needs separate review; a caregiver account cannot establish that authority. [Ethics statement](Ethics_Statement.md), [help/privacy research](https://chatgpt.com/space/page_7cd1dec9321881918733da8707d66e77).

## Legal

The team has selected MIT for team-owned source code. This does not relicense third-party code, model weights, datasets, fonts, SDKs or provider services. The dependency/asset inventory and NOTICE identify base licenses and open provenance. An unidentified public video or model checkpoint cannot be described as cleared for redistribution. The self-hosted SAM materials use custom terms, while a hosted SAM request is governed by separate service terms; neither should be labeled MIT because the surrounding application is MIT.

Obtain applicable university/recruitment permissions and accessible informed consent before participant work. Keep household recordings, diagnosis, real contacts and medication details out of synthetic bench tasks. No medical, accessibility, privacy-law or product certification is claimed. Any later deployment needs review of its actual users, location, processing and intended claims. [MIT license](LICENSE), [licensing and attribution](Ethics_Statement.md), [usability protocol](https://chatgpt.com/space/page_962b1f1841b88191997cd128dee77cee).

## Security

The loopback Node call bench uses trusted fixture roles, not authenticated remote caregivers. Host/Origin checks, body bounds and browser policy help constrain that bench but do not turn it into the proposed deployed design. The production contract requires OIDC/PKCE, scoped caregiver/robot identities, active pairing, HTTPS/WSS, encrypted media and secrets outside source control. Neither a bearer token nor a maintainer role grants resident capture or movement consent.

The repository-history audit searches local refs and reflogs and reports no unresolved secret candidates within its stated limits. It is separate from endpoint, revocation, TLS and stored-data testing. Token lifetime, rate limits, backup/deletion mechanisms and deployed key provisioning remain unverified and must be resolved before real-user deployment. Offboard results keep their original local capture identity and expiry; an open stream or a new remote timestamp cannot renew stale observation authority. [Security evidence](evidence/Security_Audit_2026-11-11.json), [runtime research](https://chatgpt.com/space/page_7f00ad6b2bb08191b36b80c1efc7dbe6).

## Diversity and Cultural

The resident must be able to choose an input and understand what the robot is doing without owning a smartphone or recalling a voice phrase. D2 specifies plainly labeled controls, scalable text, non-color-only status, VoiceOver support for the caregiver app, and a reachable alternative Stop/Privacy input when the low display is inaccessible. A pixel target-size criterion does not establish safe reach, force or physical visibility.

The usability kit asks about usual aids, text size, language, hearing/vision, reach, breaks and a chosen supporter. Record assistance separately; the caregiver should not answer for the resident. A small formative cohort cannot establish universal usability. Later voice/help work must test accents, speech impairment, quiet speech, multiple speakers and television. Evaluate tracking across bodies, clothing, mobility aids and lighting; one successful mask cannot establish equal performance. [Usability kit](https://chatgpt.com/space/page_962b1f1841b88191997cd128dee77cee).

## Social and Political

The product must offer enough benefit over a fixed phone/tablet or accessible call control to justify introducing a moving device, maintenance and household observation. The intended audience is not defined solely by age or disability; the first resident, task and home arrangement still need validation. The research compares a mobile call with fixed alternatives and keeps remote contact from becoming a substitute for promised human assistance.

An account owner's agreement does not cover every visitor, partner or paid helper. Demonstrations need visible capture status, prior agreement and a route protecting private spaces. Internet access, device cost, language and caregiver availability also affect access. Show offline/unavailable explicitly; do not imply continued assistance or monitoring without the required service/operator.

**Consistency and authorship.** [Ethics_Statement.md](Ethics_Statement.md) expands the same four named concerns; [Week 9](Week_09_Schema_and_Stack.md) preserves the schema/stack baseline. Austin confirms team ownership of architecture/model/priorities/rationale. AI assistance is disclosed; member analysis review and individual signatures remain pending.
