# LaTeX Resume

This is a LaTeX project for a resume.

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

## Building the PDF

To build the PDF, run the following command twice:

```bash
xelatex main.tex
```

The first run will generate the auxiliary files, and the second run will ensure that all cross-references are correct. The output will be `main.pdf`.

## Notes

- The original `preamble.tex` had some commands that were incompatible with `xelatex`. These have been commented out.
- The original document used some icons from the "Font Awesome Pro" set, which is not available in the standard TeX Live distribution. These icons have been replaced with free alternatives.
  - `\faMapMarkerAlt` was replaced with `\faHome`.
  - `\faExternalLink` was replaced with `\faLink`.
- There was a syntax error in `experience/isa_internship.tex` which has been fixed.

## Continuous Integration

This project is set up with a GitHub Action that automatically builds the PDF.

- On every push to the `main` branch, the PDF is rebuilt and committed to the repository.
- When a new tag starting with `v` (e.g., `v1.0`, `v1.1`) is pushed, a new GitHub Release is created with the PDF attached.

The `GITHUB_TOKEN` is automatically created by GitHub Actions and has the necessary permissions for creating releases. No further setup is required for this.
