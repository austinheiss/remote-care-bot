# In-Home Assistive Robot

Gavin Lamphier - Industrial Design; Liam Patel - Mechanical Engineering; Austin Heiss - Computer Science.

## 1. Project

Resident-controlled video calls and requested following for an older or disabled adult at home. The first moving prototype requires supervised, bounded trials and a qualified physical platform. This repository currently holds design deliverables and document-build scripts, not a deployed application.

## 2. Requirements

- [User stories and use cases](User_Stories.md) / [PDF](User_Stories.pdf)
- [Assignment #7 constraints and ABET concerns](Constraints_Essay.md) / [PDF](Constraints_Essay.pdf)
- [Week 9 schema and technology stack](Week_09_Schema_and_Stack.md) / [PDF](Week_09_Schema_and_Stack.pdf)

The latter two documents are current reconstructions from the design baseline and Senior Design Space research, not backdated submissions. The original Assignment #7 rubric's exact eight labels remain to be compared with the working outline.

## 3. System design

- [D0 high-level design](Design_Diagrams/D0_High_Level_Design.pdf)
- [D1 data model, API and stack](Design_Diagrams/D1_Detailed_Design.pdf)
- [D2 component completion and peer review](Design_Diagrams/D2_Detailed_Design.pdf)
- [Consolidated report](Design_Diagrams/Design_Diagrams_Consolidated.pdf)

## 4. Validation and review

- [Peer review actions](Design_Diagrams/Peer_Review_Notes.md)
- [Reproducible local secret-history audit](tools/audit_ethics.py)
- [Redacted audit evidence](evidence/Security_Audit_2026-11-11.json)

## 5. Ethics and ABET concerns

- [Ethics statement](Ethics_Statement.md) / [PDF](Ethics_Statement.pdf)
- [Attribution and dependency sources](NOTICE.md)

Austin supplied the member-level AI disclosure and confirmed team ownership of the architecture, data model, priorities and rationale on November 11. Austin uses Codex and Claude; Liam uses ChatGPT; both manually review/edit outputs. Gavin is reported not to use AI for design/research. Component-owner reviews, personal signatures and missing artifact/version/provenance details remain to be recorded. The reconstructed constraints essay and Week 9 consolidation now cross-reference the same D1/D2 baseline. Security/deletion proposals remain distinct from completed tests. The Fall ABET Concerns Essay and Final Design Report section 5 should reuse the reviewed, signed version.

## 6. License and reproducible documents

Team-owned source code is licensed under [MIT](LICENSE), selected by Austin on November 11. This resolves D1's earlier open license decision. Third-party code, model weights, datasets, SDKs and assets retain their own terms; unknown versions and rights are not given release clearance by the MIT grant.

Build the ethics and companion PDFs from their Markdown sources using ReportLab and the pinned documentation dependencies in `tools/requirements-ethics.txt`:

```sh
python3 tools/build_ethics_pdf.py
python3 tools/audit_ethics.py
```

The build uses Times New Roman installed on the host and does not redistribute font files. PDF QA uses a separate Poppler executable. Build-tool versions and licenses are in the statement.
