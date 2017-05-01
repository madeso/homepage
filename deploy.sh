#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

# Build the project.
hugo # if using a theme, replace by `hugo -t <yourtheme>`

find public -type f -name "*.html" -exec tidy -f errors.txt -m -utf8 -i {} \;

# Go To Public folder
cd public
# Add changes to git.
git add -A

# Commit changes.
msg="Rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

# Come Back
cd ..

# Add and commit submodule
git add -A
git commit -m "$msg"
