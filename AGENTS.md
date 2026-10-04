# Repository Guidelines

## HPCC64 public identity

The public site represents **HPCC64 Lab as a human–AI research and engineering system**.

The public wording is **not fixed to one slogan or sentence**. It must preserve the semantic invariant: HPCC64 is a human–AI symbiotic research and engineering system in which a human principal retains purpose, authority, and accountability while an AI cognitive agent extends research, analysis, synthesis, design, implementation, and verification within an authorized scope.

Acceptable public phrasing may vary by context and design. Do not require or mechanically restore any specific slogan if the same meaning is expressed clearly.

The operating model is:

- **Human principal:** defines purpose, values, priorities, hard constraints, consequential decisions, publication authority, and final accountability.
- **AI cognitive agent:** performs research, analysis, synthesis, design, implementation, verification, and evidence management within the authorized scope.
- **Additional agents, models, tools, and execution environments:** temporary bounded capabilities, not a permanent virtual staff or autonomous organization.

Do not present AI as an independent principal, legal person, or publication authority.

## Canonical landing-page structure

The homepage must remain compact, coherent, and public-facing. It is not a CV, internal project directory, research notebook, or chronology of private work.

Use this section order:

1. **What HPCC64 is** — short explanation of the lab and the Human · Purpose · Cognition · Control identity.
2. **Human–machine symbiosis** — clear separation of human-principal and AI-agent responsibilities.
3. **Research directions** — describe public problem domains in general terms and explain why they matter.
4. **Methodologies and relationships** — explain the principal methods and how they connect.
5. **Practical application** — describe problem classes and use cases without exposing unpublished project names.
6. **CTA / contact** — GitHub, X, and email.

### Public-scope rule

Do **not** expose names of unpublished, experimental, private, or pre-discovery projects merely to illustrate current work.

Describe practical research through problem classes such as:

- business discovery and staged investment;
- service and operating-model design;
- institutional and regulatory navigation;
- complex socio-technical change.

Similarly, describe social-system research in general terms such as actors, incentives, power, formal rules, operational mechanisms, feedback loops, friction, and representation-versus-reality gaps. Do not publish internal project/repository names unless they have an explicit public publication decision.

## Public methodologies

The site may explain the following named methodologies because they are part of the HPCC64 public intellectual framework:

- **IT Compliance Assessment** — establishes Required State: obligations, mandatory controls, capabilities, and hard constraints.
- **Technology Due Diligence** — establishes evidenced Current State: architecture, dependencies, lifecycle, operating capability, economics, gaps, and uncertainty.
- **RGTA / RGVE + MTQR** — RGTA is the technology-domain predecessor of the developing Risk-Guided Value Engineering methodology; MTQR means Money · Time · Quality · Risk / Uncertainty.
- **PASGR-7** — decision mechanism for uncertain multi-actor problems. Do not invent a new acronym expansion. The historically recovered named sequence is Problem → Architecture → Scenarios → Grading → Recombination → Review → Run.
- **EXEC** — execution layer paired with PASGR-7; turns a selected direction into bounded, observable action with evidence, success/failure logic, error handling, escalation, and reassessment.
- **Knowledge Fabric** — evidence/provenance/reproducibility layer spanning the decision loop.

Treat RGVE, PASGR-7, and EXEC as developing methodologies/systems. Do not present any of them as frozen, fully validated, or universally applicable specifications.

## Visual constraints

Keep the public surface deliberately minimal:

- static HTML/CSS;
- no application framework;
- no JavaScript unless a concrete interaction requires it;
- white background;
- black typography;
- red used sparingly for the `64` identity;
- ordinary readable headings rather than oversized slogan typography;
- emphasis through semantic **bold** / *italic* text rather than giant display copy;
- comfortable reading width and whitespace;
- semantic HTML and accessible list/heading structure;
- responsive layout without horizontal overflow.

Do not introduce generic AI, cloud, cyber, neural-network, shield, or futuristic stock imagery.

## Canonical semantic identity

**HPCC64 = Human · Purpose · Cognition · Control**

**64 = six system domains × four decision criteria**

Six system domains:

1. Value & Outcomes
2. Actors & Capabilities
3. Processes & Operating Model
4. Evidence, Data & Knowledge
5. Cognition, Decisions & Automation
6. Technology, Infrastructure & Dependencies

Decision criteria:

1. Money
2. Time
3. Quality
4. Risk / Uncertainty

## Contribution provenance

For material public-content changes, record concept origin, material reframing, research/analysis, implementation, review/validation, baseline approval, and publication authorization when those events differ.

Keep authority separate from completed action. Git commit identity alone is not intellectual provenance.

## Project Structure & Module Organization

This repository is intentionally minimal. `index.html` is the static-site entry point, `README.md` holds the durable public project description, `AGENTS.md` governs maintenance, and `LICENSE` defines reuse terms.

## Build, Test, and Development Commands

- `python3 -m http.server 8000` to preview the site locally.
- `git diff` to confirm the repository stays small and intentional.
- Validate internal anchors, keyboard navigation, responsive rendering, and public links before merge.

## Coding Style & Naming Conventions

Use semantic HTML and concise Markdown. Prefer lowercase file names and kebab-case assets if the site expands.

## Testing Guidelines

For site work, validate desktop/mobile rendering, navigation, link behavior, accessibility semantics, and absence of unintended private/internal names before opening or merging a PR.

## Commit & Pull Request Guidelines

Use concise conventional commit subjects. Material changes go through PR + review. Codex review is required before merge.

## Scope Guardrails

Keep this repository focused on the HPCC64 public website and related public documentation. Do not use it as a catalogue of internal research repositories or unpublished projects.
