#!/bin/bash

# How to Upload a Project to GitHub (from VS Code Terminal)

# Initialize git in the project
git init

# Add all files to staging
git add .

# Commit the files
git commit -m "Initial commit"

# Rename branch to main
git branch -M main

# Connect local repo to GitHub repo
git remote add origin https://github.com/DeveshNathJha/FastApi.git

# Push project to GitHub
git push -u origin main

# Confirmation message
echo "Project successfully pushed to GitHub!"

# Run --bash gitupload.sh