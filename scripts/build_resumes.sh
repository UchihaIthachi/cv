#!/bin/bash
# scripts/build_resumes.sh

mkdir -p output

PROFILES=("backend" "devops" "full" "fullstack" "general" "web3")
FIRST_NAME="Harshana"
LAST_NAME="Fernando"

for PROFILE in "${PROFILES[@]}"; do
    echo "Building $PROFILE resume..."
    cd documents/resume
    xelatex -output-directory=../../output -jobname="${FIRST_NAME}_${LAST_NAME}_${PROFILE}_Resume" "${PROFILE}.tex"
    cd ../..
done
