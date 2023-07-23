#!/usr/bin/env bash
# Initialize repo
echo "# alx-backend" >> README.md
git init
git add README.md
git commit -m "Project init"
git branch -M master
git remote add origin git@github.com:alexUd01/alx-backend.git
git push -u origin master
