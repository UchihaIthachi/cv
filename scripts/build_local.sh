#!/bin/bash
set -e

PROFILE=${1:-general}

mkdir -p output
cd documents/cv
xelatex -output-directory=../../output -jobname="${PROFILE}" "${PROFILE}.tex"
cd ../..
