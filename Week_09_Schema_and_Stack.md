# In-Home Assistive Robot

**Week 9 Schema and Technology Stack | November 11, 2026**  
Gavin Lamphier - Industrial Design; Liam Patel - Mechanical Engineering; Austin Heiss - Computer Science

This document consolidates D1's call schema and stack with D2's interface refinements and the Senior Design prototype evidence. It is a current reconstruction, not a claim that a Week 9 submission or production database already existed. Austin owns software/data; Gavin checks resident/caregiver meaning and accessibility; Liam checks sensing/platform records. Their component reviews remain to be recorded.

## Schema and purpose

The D1 relational model has four entities. Robot and Caregiver have a many-to-many relationship through Pairing; one Pairing owns zero or more CallAttempts. Each attempt belongs to exactly one robot/caregiver pair. Pairing is call eligibility, while current resident CALL/FOLLOW consent remains local and volatile. [D1 section 2 and entity diagram](Design_Diagrams/D1_Detailed_Design.pdf).

| Entity / field | Type | Key, nullability and rule | Purpose |
| --- | --- | --- | --- |
| Robot.robot_id | Text | PK; 1-64 allowed ASCII ID characters | Enrolled robot identity |
| Robot.last_seen_utc | UTC text or null | Latest accepted heartbeat; RFC 3339 | Display online age, not location |
| Robot.last_sequence | Integer or null | 0..2^63-1; increasing within authenticated session | Reject repeated/out-of-order heartbeats |
| Caregiver.caregiver_id | Text | PK; identity-provider subject | Account identity without local password |
| Caregiver.display_name | Text | 1-80 characters | Show named caller before acceptance |
| Pairing.robot_id | Text | Composite PK; FK to Robot | Associate account with robot |
| Pairing.caregiver_id | Text | Composite PK; FK to Caregiver | Associate robot with account |
| Pairing.active | Boolean | True/false; inactive denies new call access | Revoke eligibility without erasing old calls |
| CallAttempt.call_id | UUID text | PK; canonical UUID | Identify one attempt |
| CallAttempt.robot_id | Text | Composite FK with caregiver_id to Pairing | Preserve owner robot |
| CallAttempt.caregiver_id | Text | Composite FK with robot_id to Pairing | Preserve owner account |
| CallAttempt.request_id | UUID text or null | Unique with caregiver_id when supplied | Deduplicate retried start |
| CallAttempt.status | Enum text | ringing, connected, declined, no_answer, offline, ended, failed | Truthful communication outcome |
| CallAttempt.created_utc | UTC text | Required RFC 3339 | Attempt creation |
| CallAttempt.accepted_utc | UTC text or null | Null until resident acceptance | Distinguish acceptance from transport connection |
| CallAttempt.ended_utc | UTC text or null | Null until closure | Terminal outcome time |

## Integrity and lifecycle

Index calls on `(robot_id, created_utc)`; keep `(caregiver_id, request_id)` unique. A partial unique index on robot_id for ringing/connected calls admits only one active attempt per robot. Start/end/outcome transitions are transactional. A repeated request returns the original result; a retry ID reused with different input is a conflict. Decline and other terminal outcomes never become connected after a delayed event. On restart, active attempts close as failed and the robot remains offline until a fresh authenticated session/heartbeat.

Only the call service opens the SQLite file. Audio/video, access tokens, passwords, masks, medical information and resident trajectories do not belong in this schema. The proposed 30-day call history requires a tested purge and backup policy; an inactive pair is pruned only after dependent records are removed. Engineering configuration is a separate versioned local record, and seven-day diagnostic metadata is a separate bounded store. [Privacy inventory and deletion limits](Ethics_Statement.md).

## Consent and transient contracts

D2 Context binds boot UUID, call UUID, epoch and sequence. CallLease adds audio/video scopes, local expiry and environment revision; FOLLOW and target selection have a separate epoch. Sensor/frame buffers, masks, SDP/ICE and media remain bounded volatile data. No stored pairing, call record or model result restores permission after reboot/revoke. D1's optical-depth TrackRecord remains offline with motion_authorized=false; D2 RobotTargetV2 requires a qualified producer in calibrated robot coordinates, which has not been established. [D2 section 2](Design_Diagrams/D2_Detailed_Design.pdf).

<!-- pagebreak -->

## Technology stack

The table distinguishes **observed** local source, **reported** Space artifacts, **proposed** D1/D2 integrations and **research alternatives**. These categories prevent a prototype runtime version from becoming an invented production version. A version marked unpinned must be fixed in manifests/lockfiles before integration or release.

| Layer | Technology / version evidence | Status and owner | Reason and boundary |
| --- | --- | --- | --- |
| Local call bench | Node; package 0.1.0; Node 23.7.0 in its README, engines >=22.5 | Observed local source; Austin | Native HTTP/SSE, crypto and optional node:sqlite; no npm dependencies declared. Loopback only. |
| Browser media/UI | Native WebRTC, HTML/CSS/JavaScript; exact Chrome build unrecorded here | Observed source; Austin/Gavin | Generated test media on one Mac; physical camera/mic, LAN and remote deployment unqualified. |
| One-shot reminders | Node 24.22.1 tested; native SQLite worker; extended package revision in Space | Reported separate artifact; Austin/Gavin | Exact-version resident approval, one future occurrence, explicit sharing and truthful self-report. Not a replacement for D1 call schema. |
| Robot application | Python, version unpinned | Proposed D1/D2; Austin | Typed local adapters and consent/control contracts; keep blocking work outside control deadlines. |
| Call API/signaling | FastAPI, Uvicorn, Pydantic; unpinned | Proposed D1; Austin | HTTP/WSS, strict validation and transactional outcome state machine. Not the current Node bench. |
| Database | SQLite, product version unpinned | Proposed call service; Austin | Single-server relational constraints; compare PostgreSQL only if measured scale requires it. |
| Identity | Keycloak + Authlib, unpinned | Proposed; Austin | OIDC/PKCE, issuer/audience/expiry/subject checks and scoped pairing. Fixture role labels are not this integration. |
| Caregiver companion | Swift/SwiftUI, SDK versions unpinned | Proposed; Austin/Gavin | Native system sign-in, Keychain refresh storage, scalable text/VoiceOver. No complete mobile call validation. |
| Baseline perception | PyTorch/TorchVision masks; NumPy optional; versions/weights unpinned | Offline experiments; Austin | Code license differs from weight/data rights. CPU timing does not establish onboard real-time performance. |
| SAM tracking direction | SAM3 family; direct Meta sam-3.1 route documented in research; exact selected provider/version unpinned | Research/integration candidate; Austin | Selected masks are not identity, depth or movement authority. Upload retention and result freshness need route-specific checks. |
| Simulation/reference | MuJoCo; Open Beni source/model/checkpoint references | Separate research artifacts; Austin/Liam | Reproduction and bounded experiments only; asset licenses and hashes must follow the exact artifact. No hardware release claim. |
| Motion platform | Dedicated local controller over bounded USB serial; board/firmware unselected | Proposed D2; Liam/Austin | Local watchdog, sequence/boot/expiry checks, feedback and separately qualified caster/balancing profiles. |
| Application compute | Existing computer for bench; Pi/Jetson/nearby-host comparisons | Alternatives, not purchase decisions | Choose from concurrent workload, encoding, thermal, mass and power measurements. |
| Hosting/network | Ubuntu VM, HTTPS/WSS, optional relay; provider/build unselected | Proposed; Austin | Authenticated outbound robot signaling; no insecure fallback. Loopback ICE rewriting cannot be reused on a LAN. |
| Middleware/inference runtimes | ROS 2, ONNX Runtime or MNN | Research alternatives only | Add only for a concrete integration need and measured compatibility. They are not adopted dependencies here. |

## Current evidence and next integration

The inspected local call package is at `/Users/austinheiss/Documents/BeniResearch/stationary_call_20261109`. Its README and manifests identify eight generated-media calls, a native-module-only package and an imported fixture authority. The [Space integration record](https://chatgpt.com/space/page_b31b04e23e38819192c67c4f3e8c14a8) separately reports the newer routine extension and its checks; that package was not represented as installed in this repository. Its call/routine authority, presence and durable routine records must not be silently merged into D1's call service model.

Continue with one canonical authority and a narrow robot adapter; preserve behavior across a later framework port. Local Stop/Privacy, capture ownership and deadline checks remain onboard. Offboard inference returns observations/proposals bound to original capture IDs, not raw motor commands. Synchronous optional terminal-call journaling on the Node event loop is a recorded gap; changing frameworks alone does not resolve it. [Runtime implementation research](https://chatgpt.com/space/page_7f00ad6b2bb08191b36b80c1efc7dbe6).

## Cross references and approval

The [ethics statement](Ethics_Statement.md), [NOTICE](NOTICE.md) and [constraints essay](Constraints_Essay.md) use this same baseline. Austin confirms team ownership of the architecture/model/priorities/rationale. This consolidation selects no new architecture or hardware; owner review, deployed settings and individual signatures remain separate evidence.
