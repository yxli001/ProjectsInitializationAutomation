# Simple Project Initialization Automation Script
import sys
# run "pip3 install PyGithub" first in order to use this
from github import Github

projectName = sys.argv[1]
accessToken = "[your github access token]"


g = Github(accessToken)

user = g.get_user()

user.create_repo(projectName)
