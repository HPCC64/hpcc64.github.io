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

### Canonical landing-page form

The homepage is a **single long causal narrative** in clear Common English. It is not:

- a CV or personal biography;
- a consulting-services catalogue;
- a generic AI startup page;
- a grid-first project directory;
- a list of repositories.

The narrative arc should remain recognizable:

1. resilience / mission-critical IT;
2. architecture and whole-system reasoning;
3. Required State → Current State → Target State;
4. RGTA → RGVE + MTQR;
5. Knowledge Fabric;
6. human–machine symbiosis;
7. bounded agency / identity;
8. HPCC64 convergence — Human · Purpose · Cognition · Control;
9. Why 64? — six system domains × four decision criteria;
10. what we work on now;
11. what we have produced;
12. closing.

Treat **RGVE** as foundational but still developing. Do not present it as a frozen or fully validated specification. Describe **RGTA** as the technology-domain predecessor/application and **MTQR** as the Money · Time · Quality · Risk / Uncertainty evaluation coordinate system rather than as the whole method.

Foundational work currently includes **Knowledge Fabric**, **PASGR-7 + EXEC**, and **RGVE**. Applied research environments include **Nomad Compass**, **Analog East**, and **Premium Mobility**. Do not expose private repository URLs or imply that private repositories are publicly accessible.

### Visual constraints

Keep the public surface deliberately minimal and GitHub-native:

- static HTML/CSS;
- no application framework;
- no JavaScript unless a concrete interaction requires it;
- white background;
- black typography;
- red used sparingly, primarily for the `64` identity;
- strong typographic hierarchy and generous whitespace;
- semantic HTML and accessible heading order;
- responsive layout without horizontal overflow.

The canonical semantic identity is:

**HPCC64 = Human · Purpose · Cognition · Control**

and

**64 = six system domains × four decision criteria**

Do not introduce generic AI, cloud, cyber, neural-network, shield, or futuristic stock imagery.

### Contribution provenance

For material public-content changes, record concept origin, later material reframing, research/analysis, draft/implementation, review/validation, baseline approval, and publication authorization when those events differ. Record named external actors/sources and bind review, baseline-approval, and publication-authorization events to their own immutable revisions/digests. Keep authority separate from completed action. Git commit identity alone is not intellectual provenance.

Historical dates, achievements, and maturity claims are public claims. Preserve accepted project history and explicit owner direction; do not invent chronology or claim completion where the underlying work remains developing.

## Project Structure & Module Organization
This repository is intentionally minimal. `index.html` is the current static-site entry point, `README.md` holds the durable public-facing project description, `AGENTS.md` governs maintenance, and `LICENSE` defines reuse terms. No separate asset tree, template system, or build pipeline is currently committed. Keep the root clean and add new directories only when they establish a clear website structure such as `assets/`, `css/`, `js/`, or `pages/`.

## Build, Test, and Development Commands
There is no build pipeline yet. For the current state of the repo, the useful checks are:

- `sed -n '1,200p' README.md` or your editor preview to review copy changes.
- `python3 -m http.server 8000` to preview the current `index.html` locally.
- `git diff` to confirm the repository stays small and intentional.

If the site grows beyond a few static files, document the new local workflow here when the tooling is introduced.

## Coding Style & Naming Conventions
Use clear, concise Markdown for repository documentation and semantic HTML for the site. Prefer simple directory names, lowercase file names, and kebab-case for assets if assets are later introduced. Keep the narrative aligned with the canonical historical/research arc above rather than reverting to a services-first consulting page.

## Testing Guidelines
For README-only changes, proofread for accuracy, tone, and broken Markdown. For future site work, manually validate desktop and mobile rendering, navigation, and link behavior in a browser before opening a PR. Add automated checks only when there is enough code to justify them.

## Commit & Pull Request Guidelines
Recent history uses conventional prefixes such as `feat:` and `docs:` plus standard merge commits from GitHub PRs. Continue using concise imperative subjects. PRs should explain the user-visible change, call out any new site structure, and include screenshots whenever visual content is introduced.

## Scope Guardrails
This repo should stay focused on the HPCC64 Lab public website and related documentation. Avoid committing local tooling, generated files, or unrelated experiments.
