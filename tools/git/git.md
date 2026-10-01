# Introduction to Git

---
## Setting up git 
First install git on your system.

### Setting your identity

```bash
git config --global user.name "devkumar70401"
git config --gloabl user.email "devkumar70401@gmail.com"
```

### Setting your editor

```bash
git config --global core.editor vi
```

### Your default branch name

To set main as the default branch name do 
```bash
git config --global init.defaultbranch main
```

### Checking your settings

```bash
git config --list
```

---
## Getting help

```bash
git help <verb>
# or
git <verb> --help
# or
man git-<verb>
```

seeing a quick refresher 

```bash
git <verb> -h 
# like 
git add -h 
git config -h 
```

---
## Getting a git repository

1. You can take a local directory that is currently not under version control, and turn it into a git repository, or
2. You can clone an existing git repository  from elsewhere 

### Initializing a Repository in an Existing Directory

```bash

cd /home/user/my_project

git init # command for initialising git in any directory 
```






