# Assignment 4 (Github) - Write a program in python (`assignment04-github.py`) 
# that will read a file from a repository (in this example, `sample_text.txt` was used). 
# The program should then replace all the instances of the text "Andrew" with your name (Ellen) and 
# push to Github.  

from config import apikeys as cfg
from github import Github
import base64

apikey = cfg["github_key"]
repo_name = "EllenMcG/WSAA-coursework"
file_path = "assignments/sample_text.txt"
commit_message = "Updated sample_text.txt: Replaced 'Andrew' with 'Ellen' for assignment 04"

g = Github(apikey)

try:
    repo = g.get_repo(repo_name)

    file = repo.get_contents(file_path)
    file_content = base64.b64decode(file.content).decode("utf-8")

    updated_content = file_content.replace("Andrew", "Ellen")

    repo.update_file(
        path=file_path,
        message=commit_message,
        content=updated_content,
        sha=file.sha,
    )
    print("File updated and changes pushed to GitHub successfully!")

except Exception as e:
    print(f"An error occurred: {e}")