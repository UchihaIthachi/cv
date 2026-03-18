#!/bin/bash
set -e

PROFILES=("general" "backend" "devops" "fullstack" "web3" "full")

for profile in "${PROFILES[@]}"; do
    echo "--------------------------------------------------"
    echo "Building $profile..."
    echo "--------------------------------------------------"
    bash scripts/build_local.sh "$profile"
done

echo "All profiles built successfully!"
