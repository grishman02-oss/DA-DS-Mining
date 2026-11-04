#Git is a VCS(Version Control System)
#git tracks our code

#1. Initialize the git => git init - only one time for a project
# U => Untracked files
# A => Added files
# M => Modified files

#2. Add files in git - git add file_name

# git add . => To add all files in a git at once
# commit the changes => git commit -m "message" a message should be clear
# connect the local folder with github repo:
# git remote add origin {ssh_key} (only one time for a project)
#for first push => git push -u origin branch_name
# -u => upstream => stores the current branch => main
# -u is used only for first push
# otherwise use git push origin {branch_name}
#now, for every next push, we donot need to give branch name, we can simply do git push
# now git push pushes the code into master branch because master was stored in upstream


#Branching
#Branching is the most important part of git
#Branching allows multiple collaborators to work on a project at the same time.





