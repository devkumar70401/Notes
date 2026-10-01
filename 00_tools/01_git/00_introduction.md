# Introduction To Git

## Setting up git in a folder

```bash
git init # to initialise the git in the directory
nano .gitignore # creating a .gitignore file to ignore several files from tracking
git status # check untracked files
git add .  # stage files
git commit -m "Initial commit" # Creating first commit

# Connect to a remote repository (e.g., Github)

git remote add origin https://github.com/devkumar70401/notes.git

git push -u origin main
```

## Pushing work on github 

```bash

git status  # Check what has changed

git add .  # stage the changes (all changes in the folder)

git commit -m "update notes on machine learning"

git push
```


