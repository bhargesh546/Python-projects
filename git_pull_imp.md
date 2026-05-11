# To merge another repository

## 1. Add the other repo as a remote
`git remote add external https://github.com/USER/OTHER-REPO-NAME.git`

## 2. Fetch the data
`git fetch external`

## 3. Pull the content into your current branch
(Use --allow-unrelated-histories because they don't share a common past)<br>

`git pull external main --allow-unrelated-histories`

## 4. Clean up
`git remote remove external`