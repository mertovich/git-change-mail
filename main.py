# The main py file should be in a parent directory of the folder where the repositories are located
import os
folder = os.listdir("the folder where your repositories are located")
 
list= []
for fileName in folder:
        list.append(fileName)

path = os.getcwd()

for i in list:
    os.chdir("path+"+i)
    print(os.getcwd())
    os.system("""
                #!/bin/sh
                git filter-branch --env-filter '
                OLD_EMAIL="" # replace this with the old email
                CORRECT_NAME="" # replace this with the correct name
                CORRECT_EMAIL="" # replace this with the correct email
                if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
                then
                    export GIT_COMMITTER_NAME="$CORRECT_NAME"
                    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
                fi
                if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
                then
                    export GIT_AUTHOR_NAME="$CORRECT_NAME"
                    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
                fi
                ' --tag-name-filter cat -- --branches --tags
                """)
    os.system("git push --force --tags origin 'refs/heads/*'")