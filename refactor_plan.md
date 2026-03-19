# Refactoring Plan: A Structured and Scalable Resume & CV Repository

This document outlines a detailed plan to refactor the current LaTeX resume repository based on the finalized structural approach. The goal is to establish a **highly structured**, **scalable** directory layout that clearly separates *content* (Single Source of Truth), *views* (profile-specific aggregations), *documents* (compilable entry points), and *configuration* (styling).

Crucially, this refactoring will **strictly preserve all existing information**. No content will be reduced, changed, or invented. The entire operation is a pure reorganization of files and update of LaTeX `\input{}` statements.

---

## 1. Revised Directory Structure (Full)

```text
.
├── documents/
│   ├── cv/                      # Multi-page ATS/Standard CVs (formerly `profiles/`)
│   │   ├── backend.tex
│   │   ├── devops.tex
│   │   ├── full.tex
│   │   ├── fullstack.tex
│   │   ├── general.tex
│   │   └── web3.tex
│   └── resume/                  # Strict 1-page Resumes (thin files, \input only)
│       ├── backend.tex
│       ├── devops.tex
│       ├── full.tex
│       ├── fullstack.tex
│       ├── general.tex
│       └── web3.tex
│
├── views/                       # \input chains, no raw text
│   ├── experience/
│   │   ├── backend_experience_resume.tex
│   │   ├── backend_experience_cv.tex
│   │   └── ...
│   ├── projects/
│   │   ├── backend_projects_resume.tex
│   │   └── ...
│   ├── skills/
│   │   ├── skills_backend_resume.tex
│   │   └── ...
│   └── summary/
│       ├── summary_backend.tex
│       └── ...
│
├── content/                     # SSOT, no layout logic
│   ├── experience/
│   │   ├── full/
│   │   ├── medium/
│   │   ├── short/
│   │   └── tailored/            # e.g. isa_internship_backend.tex
│   ├── projects/
│   │   ├── default/
│   │   ├── middle/
│   │   ├── short/
│   │   └── one-line/
│   ├── header.tex               # name + title line
│   ├── contact_details.tex      # email, phone, LinkedIn, GitHub
│   ├── skills_master.tex
│   ├── education.tex
│   ├── education_resume.tex
│   ├── certificates.tex
│   ├── referees.tex
│   └── writing.tex
│
├── config/
│   ├── themes/
│   │   ├── cv_style.tex
│   │   └── resume_style.tex
│   ├── macros/
│   │   ├── shared_macros.tex
│   │   └── resume_macros.tex
│   └── preambles/
│       ├── cv_preamble.tex
│       └── resume_preamble.tex
│
├── scripts/
│   ├── build_all.sh
│   ├── build_resumes.sh
│   ├── build_local.sh
│   ├── build_profile_both.sh
│   ├── rewrite_paths.py         # Dry-run path migration script
│   └── generate_index.py
│
├── arch/
├── output/
├── Makefile
└── README.md
```

---

## 2. Revised Execution Phases

**Phase 0 — Dry-run audit**
Before touching anything: run `find . -name "*.tex" | xargs grep -h '\\input{' | sort -u` to produce a complete list of every `\input{}` path in the repo. Save this as `input_audit_before.txt`. This is your ground truth for Phase 5 verification.

**Phase 1 — Directory scaffolding**
`mkdir` only. No file moves yet. Verify the tree with `tree -d`.

**Phase 2 — File moves**
Move files with `mv`, preserving variation subdirectories exactly. Create the thin entry files in `documents/resume/`. No content file is opened or edited. Log every move to `migration_log.txt`.

**Phase 3 — Path rewriting via script**
Create and run `scripts/rewrite_paths.py --dry-run` first — it prints every `\input{}` it would rewrite. Review the diff. Then run without `--dry-run` to apply. The script only touches `\input{...}` tokens.

**Phase 4 — Compilation verification**
Run `bash scripts/build_all.sh` and `bash scripts/build_resumes.sh`. Any `File not found` error in LaTeX output pinpoints the exact broken path. Fix and re-run until clean.

**Phase 5 — Diff review**
Run `find . -name "*.tex" | xargs grep -h '\\input{' | sort -u > input_audit_after.txt` and `diff input_audit_before.txt input_audit_after.txt`. The diff should show only path string changes — no lines that don't contain `\input{` should appear. Then `git diff --stat` to confirm only `.tex` files were modified and only `\input{}` lines changed within them.