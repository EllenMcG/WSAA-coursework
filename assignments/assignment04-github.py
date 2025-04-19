# Assignment 4 (Github) - Write a program in python (`assignment04-github.py`) 
# that will read a file from a repository (in this example, `sample_text.txt` was used). 
# The program should then replace all the instances of the text "Andrew" with your name (Ellen) and 
# push to Github.  

from config import apikeys as cfg
import requests

apikey = cfg["github_key"]
