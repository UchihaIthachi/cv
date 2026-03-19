# Highly Scalable LaTeX CV & Resume Framework

This repository uses a highly structured, view-driven LaTeX framework to manage both **multi-page standard CVs** and **strict 1-page ATS resumes** across **multiple professional profiles** (e.g., Backend, DevOps, Web3, Fullstack) from a Single Source of Truth.

## Directory Architecture

The repository is built on a strict separation of concerns:

- **`documents/`**: The compilable entry points.
  - `cv/`: Multi-page, detailed ATS CVs (e.g., `backend.tex`, `devops.tex`).
  - `resume/`: Strict 1-page resumes. These are thin wrapper files that dynamically pull in specific views.
- **`content/`**: The Single Source of Truth (SSOT). All actual text, project descriptions, and experience bullet points live here.
  - Variations are preserved in subdirectories like `content/projects/short/`, `content/projects/middle/`, and `content/experience/tailored/`. This allows different profiles to pull different lengths or focuses of the same project/role without duplicating the source text.
- **`views/`**: Profile-specific aggregations. These files contain NO raw text; they simply `\input{}` the appropriate files from `content/` to build a tailored section (e.g., `views/projects/backend_projects_resume.tex`).
- **`config/`**: Styling and LaTeX configuration.
  - `preambles/`: Document class and package imports (`cv_preamble.tex`, `resume_preamble.tex`).
  - `macros/`: Custom LaTeX commands (`shared_macros.tex`, `resume_macros.tex`).
  - `themes/`: Font, color, and spacing configurations (if any).

## Dependencies

To compile this project, you need a working TeX Live installation with `xelatex`. The following packages are required:

- `texlive-xetex`
- `texlive-fonts-extra`
- `texlive-latex-extra`

On a Debian-based system (like Ubuntu), you can install them with:

```bash
sudo apt-get update
sudo apt-get install -y texlive-xetex texlive-fonts-extra texlive-latex-extra
```

## Building the PDFs

You can build the PDFs manually using the provided shell scripts in the `scripts/` directory:

1. **Build All Multi-Page CVs**:
   ```bash
   bash scripts/build_all.sh
   ```
   Outputs will be placed in the `output/` directory (e.g., `output/backend.pdf`).

2. **Build All 1-Page Resumes**:
   ```bash
   bash scripts/build_resumes.sh
   ```
   Outputs will be placed in the `output/` directory (e.g., `output/Harshana_Fernando_backend_Resume.pdf`).

3. **Build a Specific CV Profile**:
   ```bash
   bash scripts/build_local.sh backend
   ```

## Continuous Integration (GitHub Actions)

This project is set up with a GitHub Action (`.github/workflows/build-pdf.yml`) that automatically builds both the CVs and the 1-page resumes for all 6 profiles (Backend, DevOps, Fullstack, Full, General, Web3).

- **On push to `main`**: All PDFs are rebuilt.
- **On push of a `v*` tag**: A GitHub Release is created containing all generated PDF artifacts.
- **Deployment**: The generated PDFs are also deployed to GitHub Pages for easy public access.

## Adding a New Profile

To add a new profile (e.g., `frontend`):
1. Create the necessary views in `views/` (e.g., `views/experience/frontend_experience_resume.tex`, `views/projects/frontend_projects_resume.tex`). These should `\input{}` files from `content/`.
2. Create thin entry files in `documents/cv/frontend.tex` and `documents/resume/frontend.tex`.
3. Add `"frontend"` to the `matrix.profile` array in `.github/workflows/build-pdf.yml` and the `PROFILES` array in the build scripts.