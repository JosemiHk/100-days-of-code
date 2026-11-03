# 100-day roadmap

Start target: 2026-11-03 (Lima). If practiced on 100 consecutive calendar days, day 100 is 2027-02-10. These are proposed sessions, not a claim of a streak. Allow 45–90 minutes per session; split work when needed. Day numbers are planning slots; entries use the actual work date. Days with dependency on external feedback can be replaced by useful local verification.

The saved job sample supports SQL, APIs, testing, documentation and automation. The backend stack is selected on day 31; do not expand into several frameworks for badges. Keep product work cohesive and reuse existing repositories when that adds more value.

## Days 1–10: Foundation and evidence

- [ ] Day 001: Run the bootstrap tests and explain each validation rule.
- [ ] Day 002: Reproduce a rejected future entry and document the failure.
- [ ] Day 003: Create a genuine local evidence note and record session 1 only if understood.
- [ ] Day 004: Define one automation problem and acceptance criteria.
- [ ] Day 005: Collect a synthetic input dataset and document its schema.
- [ ] Day 006: Write malformed-input fixtures.
- [ ] Day 007: Implement CSV field validation.
- [ ] Day 008: Test encodings and missing columns.
- [ ] Day 009: Review the diff and document limitations.
- [ ] Day 010: Demonstrate the tool from a clean checkout.

## Days 11–20: Python automation

- [ ] Day 011: Define a CSV cleanup contract.
- [ ] Day 012: Implement whitespace normalization without changing identifiers.
- [ ] Day 013: Add explicit date parsing and errors.
- [ ] Day 014: Detect duplicate records using a documented key.
- [ ] Day 015: Generate a deterministic validation report.
- [ ] Day 016: Add a command-line interface with useful exit codes.
- [ ] Day 017: Test Unicode and empty inputs.
- [ ] Day 018: Measure runtime on generated sample data.
- [ ] Day 019: Document input privacy and failure handling.
- [ ] Day 020: Publish a reproducible automation case study.

## Days 21–30: SQL and data quality

- [ ] Day 021: Design a relational schema for synthetic service requests.
- [ ] Day 022: Write schema creation and seed scripts.
- [ ] Day 023: Add constraints for invalid states.
- [ ] Day 024: Write joins for operational reporting.
- [ ] Day 025: Compare aggregate queries with expected results.
- [ ] Day 026: Demonstrate a transaction rollback.
- [ ] Day 027: Reproduce and fix a duplicate-insert defect.
- [ ] Day 028: Use a query plan to evaluate one index.
- [ ] Day 029: Document tradeoffs and migration procedure.
- [ ] Day 030: Demonstrate data quality checks end to end.

## Days 31–40: Backend domain design

- [ ] Day 031: Choose one backend stack and explain why.
- [ ] Day 032: Define service-request use cases and out-of-scope features.
- [ ] Day 033: Model domain states and allowed transitions.
- [ ] Day 034: Implement one creation operation.
- [ ] Day 035: Validate required fields and invalid transitions.
- [ ] Day 036: Add persistence with parameterized queries.
- [ ] Day 037: Implement read operations and pagination contract.
- [ ] Day 038: Test not-found and conflict behavior.
- [ ] Day 039: Document module boundaries.
- [ ] Day 040: Review and merge a coherent backend slice.

## Days 41–50: REST integration

- [ ] Day 041: Specify request and response examples.
- [ ] Day 042: Expose the creation endpoint.
- [ ] Day 043: Expose list and detail endpoints.
- [ ] Day 044: Implement consistent error responses.
- [ ] Day 045: Test malformed payloads and unsupported values.
- [ ] Day 046: Add an integration test against temporary data.
- [ ] Day 047: Define timeout and retry behavior for one external dependency.
- [ ] Day 048: Test failures with a fake dependency rather than live credentials.
- [ ] Day 049: Document API usage and curl examples.
- [ ] Day 050: Demonstrate API and persistence together.

## Days 51–60: Frontend integration

- [ ] Day 051: Design an accessible request-list screen.
- [ ] Day 052: Implement loading and empty states.
- [ ] Day 053: Connect list screen to the API.
- [ ] Day 054: Implement a validated creation form.
- [ ] Day 055: Show actionable server errors.
- [ ] Day 056: Add detail and status views.
- [ ] Day 057: Test keyboard operation and labels.
- [ ] Day 058: Test a failed network request.
- [ ] Day 059: Document one usability decision.
- [ ] Day 060: Demonstrate the primary user journey.

## Days 61–70: Quality and delivery

- [ ] Day 061: Build from a clean environment.
- [ ] Day 062: Add automated checks for the backend slice.
- [ ] Day 063: Add automated checks for frontend behavior.
- [ ] Day 064: Document required configuration without secrets.
- [ ] Day 065: Create a local container setup if it simplifies reproduction.
- [ ] Day 066: Test startup and database readiness.
- [ ] Day 067: Add health checks with clear semantics.
- [ ] Day 068: Test deployment locally before choosing a cloud.
- [ ] Day 069: Compare cloud cost and limits before optional deployment.
- [ ] Day 070: Write an operations and rollback guide.

## Days 71–80: Existing project improvement

- [ ] Day 071: Select an existing repository and reproduce a specific problem.
- [ ] Day 072: Write a regression test for the selected behavior.
- [ ] Day 073: Implement the smallest coherent fix.
- [ ] Day 074: Verify the fix against old and new cases.
- [ ] Day 075: Inspect tracked generated files and propose cleanup.
- [ ] Day 076: Improve setup instructions from actual commands.
- [ ] Day 077: Document one architecture decision in that project.
- [ ] Day 078: Measure one relevant behavior before and after.
- [ ] Day 079: Seek a real review only from an available consenting collaborator.
- [ ] Day 080: Merge when checks and genuine review requirements are satisfied.

## Days 81–90: Community and collaboration

- [ ] Day 081: Identify a maintained project you actually use.
- [ ] Day 082: Read its contribution guidelines and reproduce an issue locally.
- [ ] Day 083: Determine whether a small contribution is wanted.
- [ ] Day 084: Prepare a tested fix or a substantive documentation correction.
- [ ] Day 085: Open an external PR only if it meets maintainer expectations.
- [ ] Day 086: Respond to review with evidence when feedback arrives.
- [ ] Day 087: Find an unanswered technical discussion you can reproduce.
- [ ] Day 088: Draft and verify an answer; publish only when useful.
- [ ] Day 089: Pair on a real issue if a collaborator is available; otherwise improve tests.
- [ ] Day 090: Record what external feedback changed; do not claim acceptance prematurely.

## Days 91–100: Portfolio and interview

- [ ] Day 091: Select the strongest three deliverables and explain their relevance.
- [ ] Day 092: Write a case study with problem, constraints and result.
- [ ] Day 093: Verify every command in the case study.
- [ ] Day 094: Draw the implemented architecture and label limitations.
- [ ] Day 095: Explain a debugging incident in English.
- [ ] Day 096: Practice SQL and API design questions using your own code.
- [ ] Day 097: Have someone run the project or perform a fresh-environment review.
- [ ] Day 098: Resolve the most important reproduction issue.
- [ ] Day 099: Prepare a short demo and truthful CV project bullets.
- [ ] Day 100: Audit all evidence, publish a retrospective and choose the next project.

## Review gates and priority

| Gate | Result to inspect | Employability impact | Effort | Priority |
|---|---|---|---|---|
| 7 days | Real input validation, tests and explanations | High | Medium | P1 |
| 30 days | Reproducible Python and SQL deliverables | High | High | P1 |
| 90 days | Integrated application plus existing-project improvement | Very High | High | P1 |
| 100 days | Demonstrable case studies and technical defense | Very High | Medium | P1 |
| Optional achievements | Observe natural progress; never create quotas | Low | Low | P3 |

Badges are not acceptance criteria. External PR acceptance, discussion answers and stars are not guaranteed outcomes. No completion is recorded automatically.

