from github import Github
import os
from dotenv import load_dotenv

load_dotenv()
github_token = os.getenv("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")

g = Github(github_token)

def get_user_info():
    try:
        user = g.get_user()
        return user.login
    except Exception as e:
        print(f"Error: {e}")
        return None