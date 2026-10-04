# Repository Guidelines

## HPCC64 Lab identity and public narrative

The public site represents **HPCC64 Lab as a human–machine cognitive system**.

Use the public-facing formulation:

> **A human and an AI, working as one lab.**

The operating model is:

- **Alex — human principal:** sets purpose, values, constraints, research direction, consequential decisions, and remains accountable.
- **Aris — persistent AI cognitive counterpart:** extends research, analysis, synthesis, design, and implementation within the authorized scope while preserving evidence, uncertainty, and provenance.
- **Additional agents, models, and tools:** dynamically invoked bounded capabilities, not a permanent staff or autonomous organization.

Do not present the AI as a legal person, independent publication authority, or autonomous principal. Human authority and accountability remain explicit.

### Public-content boundary

The owner's 2026-10-04 correction governs the current page and supersedes earlier instructions to enumerate internal research or applied project names.

Describe research on **complex social and business systems** only at the general problem level: coordination, responsibilities, information flows, dependencies, resource constraints, and reliable operation. Do not publish internal social/institutional research names, their specific theses, or internal project mappings.

Describe applied work through practical problems such as testing demand before investment, evaluating viability, and designing reliable services. Do not name unlaunched applied projects or imply that they are available products, established businesses, or completed validation programmes.

This restriction applies to all newly authored public surfaces in this repository: the page, metadata, README, agent instructions, comments, PR descriptions, and new provenance notes. Do not reproduce excluded names merely to explain their removal. Access to an internal source is not permission to publish it. Do not expose private repository URLs or private artifacts. Historical Git/PR records are not rewritten by an ordinary content correction.

### Canonical landing-page form

The homepage is a **connected narrative in clear Common English**. It is not a CV, consulting-services catalogue, generic AI startup page, project directory, or list of repositories.

Retain the causal arc without making every internal concept a separate public section:

1. resilience and mission-critical IT as background;
2. whole-system assessment and Required State → Current State → Target State;
3. comparison of feasible change through RGTA → developing RGVE and MTQR;
4. decision selection, controlled execution, and durable knowledge;
5. human–AI collaboration, bounded agency, and contribution traceability;
6. HPCC64 identity and the six-domain, four-criteria frame;
7. practical research questions, followed by produced work and a short closing.

Use explanatory paragraphs and transitions. Define a method before reusing its name; remove redundant mentions rather than filling the page with acronyms. Use short descriptive headings, **bold** for key distinctions, and *italics* for secondary emphasis. Avoid slogans and promotional claims.

Treat **RGVE** as foundational but still developing. Expand it as **Risk-Guided Value Engineering** and describe **RGTA — Risk-Guided Technology Advisory** as its technology-domain predecessor/application. **MTQR — Money, Time, Quality, and Risk / Uncertainty** is an evaluation coordinate system, not the whole method.

Explain **PASGR-7** as a developing seven-step decision method and **EXEC — Controlled Execution System** as its execution layer. The recovered original mnemonic is **Problem → Architecture → Scenarios → Grading → Recombination → Review → Run**. Identify this as historical naming, not a newly adopted fixed specification. Explain the practical distinction: PASGR-7 addresses what to do and why; EXEC defines responsibility, actions, inputs, deadlines, limits, observable results, and reassessment. Do not invent a letter-by-letter expansion for EXEC.

Describe **Knowledge Fabric** as a developing architecture with documented semantic/research work. Distinguish the goal of reconstructing reasoning from a proven production replay capability. Foundational work and working artifacts can be named within this scope; this is not permission to disclose other projects.

### Visual constraints

Keep the public surface deliberately minimal and GitHub-native:

- static HTML/CSS; no application framework or unnecessary dependencies;
- no JavaScript unless a concrete interaction requires it;
- white background, dark readable typography, and red used sparingly for the `64` wordmark;
- body text at 1rem, restrained heading scale (current h1: 1.75rem; h2: 1.25rem), and comfortable line spacing;
- no oversized hero headlines, oversized identity numerals, slogan panels, or display-sized closing statements;
- semantic HTML, accessible heading order, keyboard navigation, and visible focus;
- responsive layout without horizontal overflow; preserve list semantics when visual list markers are removed.

The canonical semantic identity is:

**HPCC64 = Human · Purpose · Cognition · Control**

**64 = six system domains and four decision criteria.** The digits name the frame; they are not an arithmetic product.

Do not introduce generic AI, cloud, cyber, neural-network, shield, or futuristic stock imagery.

### Contribution provenance

For material public-content changes, record concept origin, later material reframing, research/analysis, draft/implementation, review/validation, baseline approval, and publication authorization when those events differ. Record named external actors/sources and bind review, baseline-approval, and publication-authorization events to their own immutable revisions/digests. Keep authority separate from completed action. Git commit identity alone is not intellectual provenance.

Historical dates, achievements, and maturity claims are public claims. Preserve accepted project history and explicit owner direction; do not invent chronology or claim completion where the underlying work remains developing.

## Project Structure & Module Organization

This repository is intentionally minimal. `index.html` is the static-site entry point, `README.md` holds the public-facing project description, `AGENTS.md` governs maintenance, and `LICENSE` defines reuse terms. Keep the root clean. Add asset or page directories only when the website needs them, not for local tooling or test output.

## Build, Test, and Development Commands

The site has no build pipeline. Use `python3 -m http.server 8000` to preview it and `git diff` to review changes. For content changes, check the current public files against the owner's disclosure boundary and verify definitions and maturity language.

For visual changes, inspect desktop and mobile rendering, navigation, and link behavior in a browser. Test unique IDs, internal anchor targets, heading order, list semantics, visible focus, reduced motion, and horizontal overflow. Preserve existing public anchor targets where practical, including `#hpcc64`. Keep temporary browser tests and screenshots outside the repository; attach evidence to the review or task handoff.

## Coding Style & Naming Conventions

Use clear, concise Markdown and semantic HTML. Prefer lowercase, kebab-case names for any new assets. Keep the narrative coherent rather than reverting to a services-first or project-catalogue page. This website does not redefine the underlying methodologies.

## Commit & Pull Request Guidelines

Use concise conventional commit subjects. Make changes through a branch and PR, not directly on `main`. PRs should state the user-visible change, scope, actual checks, limitations, and contribution provenance. Obtain Codex review for the final revision and disposition findings before integration. Separate implementation, review, acceptance, authorization, merge, and live-deployment verification; do not describe one as evidence that the others occurred.

## Scope Guardrails

Keep this repository focused on the HPCC64 Lab public website and related documentation. Avoid committing local tooling, generated files, or unrelated experiments. A bounded copy/typography correction is not a new branding programme, a publication of internal projects, or a mandate to rewrite Git history.
