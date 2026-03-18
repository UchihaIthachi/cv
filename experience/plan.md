# Plan to Create 6 Profile Resumes

This plan outlines the steps to generate 6 strict, ATS-optimized, 1-page resumes based on your existing 6 CV profiles, adhering to your specific formatting rules.

## 1. Typography & Styling Configuration (`theme_resume.tex` / `preamble.tex`)
- Configure the primary font to **Arial** using `fontspec`.
- Set strict font sizes:
  - **Name:** 18pt, Bold.
  - **Section Headings:** 10pt, ALL CAPS, Bold.
  - **Content & Body Text:** 9pt.
  - **Personal Info:** 9pt.
- Configure page margins to be between **0.5 and 1 inch** using the `geometry` package.
- Enforce standard round bullets (`\textbullet`) for all itemized lists, explicitly removing any dashes or emojis.
- Ensure all graphics, fancy design elements, and complex layouts are stripped out.

## 2. Header Redesign (`sections/header.tex` or new `sections/header_resume.tex`)
- Format the Name to be exactly 18pt and Bold.
- Format the Personal Info to be 9pt.
- Ensure Email and LinkedIn are clickable links (`\href`) with plain text (no fancy icons).

## 3. Content Formatting & 1-Page Enforcement
- Update `macros.tex` (e.g., `\CVExperienceEntry`) to ensure Work Experience contains strictly bullet points and **zero paragraphs**.
- Audit the master content included in the 6 profiles (`backend`, `devops`, `full`, `fullstack`, `general`, `web3`).
- Create shortened view files (e.g., `projects_<profile>_resume.tex`, `experience_<profile>_resume.tex`) if necessary to guarantee each of the 6 profiles fits **strictly on 1 page**.

## 4. Build System & Naming Convention Updates
- Modify the build scripts (or create `scripts/build_resumes.sh`) to support the new format.
- Update the output renaming logic so the generated files strictly follow the naming convention: `FirstName_LastName_<Profile>_Resume.pdf` (e.g., `John_Doe_Backend_Resume.pdf`).
- Ensure the build artifacts are strictly PDFs.

## 5. Pre-commit Steps
- Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done (e.g., verify page lengths are exactly 1 page, verify fonts are correctly applied, verify ATS-readability).
