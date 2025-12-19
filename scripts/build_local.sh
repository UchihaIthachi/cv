#!/bin/bash
set -e

echo "Updating package lists..."
sudo apt-get update

echo "Installing LaTeX dependencies..."
# Core XeTeX and fonts
sudo apt-get install -y texlive-xetex texlive-fonts-extra texlive-latex-extra

echo "Building PDF..."
mkdir -p output
# Build twice for references
xelatex -output-directory=output profiles/general.tex
xelatex -output-directory=output profiles/general.tex

echo "Build complete! PDF is in output/general.pdf"
