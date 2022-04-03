# Github Command Lines

`-- Git Version --`
- git --version

`-- Git config for your name and email --`
- git config --global user.name "Sahil"
- git config --global user.email "xyz@gmail.com"

`If you want to check whether it is updated or not.`
- git config --global user.name

`-- Git initialize --`
- git init

`-- Git status --` <-- will tell you what changes did you made in this directory till now
- git status

`-- Git add <filename> --` <-- `<filename>` will move to the staged. If you replace `<filename>` with . (dot), all the files will put to staged.
- git add `<filename>`

`-- Git commit --` <-- only the staged file will commit. If it is modified while file being staged, make sure to add again otherwise it will not commit it.
- git commit -m "Message"

`-- Git Log --` <-- will give you the history of the commitment made by current branch
- git log

`-- Git checkout <hashcode>--` <-- take you the track back and check the files as well as content of commitment
- git checkout `<hashcode>`
- git checkout master <-- if you want to return to the main or latest commitment

- git checkout `<branchname>` <-- will move to this branchname

`-- Git branch --`
- git branch `<branchname>` <-- to create branch name
- git branch <-- to see the list of branch locally

- git checkout -b `<branchname>` <-- it will first create branch branchname and then will checkout this branchname

-- Git merge --
let say branch names are: `dev` and `sahil/multiply`

dev
                                     
|-> sahil/multiply

- Current branch (sahil/multiply): After creating multiply.py, added to staged and commit with message. <-- think of this as finished a new feature
- When you checkout in dev, they do not know what sub-branch did it. After modification or new feature made it, we want to bring these features into parent branch.
- To do that, first go the parent branch,
current branch (dev): git merge <branchname>
Ex:- git merge sahil/multiply  <-- this will update feature to parent branch


`-- .gitignore` file <-- make a list of files or folders that should be ignored while commiting

`-- To add remote URL(HTTP) --`
- git remote add temp_name URL

`-- To add remote URL(SSH) --`
- git remote set-url temp_name URL

`-- List of remote --`
- git remove -v

`-- Git push --` <-- To put all files in remote Github repository
- git push -u `<temp_name>` `<which_branchname_to_put_all_files_in_respository>`
- git push -u origin master

`-- Fork --` <-- This will bring copy of files/folders into your respository.
- git clone `<HTTP>` <-- to get into local system
- After minor changes, added to stages and then commit and push in repository.
- Click Contributor to send pull request
- `Contributor` will go to pull request and check/approval and will updated in contributor\'s repository
