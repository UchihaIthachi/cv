#!/bin/bash
# scripts/build_resumes.sh

mkdir -p output

PROFILES=("backend" "devops" "full" "fullstack" "general" "web3")
FIRST_NAME="Harshana"
LAST_NAME="Fernando"

for PROFILE in "${PROFILES[@]}"; do
    echo "Building $PROFILE resume..."
    xelatex -output-directory=output -jobname="${FIRST_NAME}_${LAST_NAME}_${PROFILE}_Resume" "\def\currentprofile{$PROFILE}\input{main_resume.tex}"
done
