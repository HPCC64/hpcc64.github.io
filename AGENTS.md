# Repository Guidelines

## Project Structure & Module Organization
This repository is currently minimal. `README.md` holds the public-facing project description, and `LICENSE` defines reuse terms. The repo is intended to host the HPCC64 Lab static website, but at the moment there are no site assets, templates, or build scripts committed. Keep the root clean and add new directories only when they establish a clear website structure such as `assets/`, `css/`, `js/`, or `pages/`.

## Build, Test, and Development Commands
There is no build pipeline yet. For the current state of the repo, the useful checks are:

- `sed -n '1,200p' README.md` or your editor preview to review copy changes.
- `python3 -m http.server 8000` once HTML files are added, to preview the site locally.
- `git diff` to confirm the repository stays small and intentional.

If the site grows beyond a few static files, document the new local workflow here when the tooling is introduced.

## Coding Style & Naming Conventions
Use clear, concise Markdown for repository documentation. If website files are added, prefer semantic HTML, simple directory names, lowercase file names, and kebab-case for assets such as `about-page.html` or `brand-guide.css`. Keep the project message professional and aligned with compliance, due diligence, and consulting themes already defined in the README.

## Testing Guidelines
For README-only changes, proofread for accuracy, tone, and broken Markdown. For future site work, manually validate desktop and mobile rendering, navigation, and link behavior in a browser before opening a PR. Add automated checks only when there is enough code to justify them.

## Commit & Pull Request Guidelines
Recent history uses conventional prefixes such as `feat:` and `docs:` plus standard merge commits from GitHub PRs. Continue using concise imperative subjects. PRs should explain the user-visible change, call out any new site structure, and include screenshots whenever visual content is introduced.

## Scope Guardrails
This repo should stay focused on the HPCC64 Lab public website and related documentation. Avoid committing local tooling, generated files, or unrelated experiments.
