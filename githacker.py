from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import random
from git import Repo, Actor
def commit_position(x: int, y: int):
    origin = datetime.now() - relativedelta(years=1) + relativedelta(days=1)
    origin = origin + relativedelta(days=y)
    origin = origin + relativedelta(days=x*7)
    return origin.strftime('%Y-%m-%d %H:%M:%S')
    
def commit(repo, file_path, x, y):
   # Check for changes
    if repo.is_dirty():
        # Add specific file
        repo.git.add(file_path)
        commit_date = commit_position(x, y)
        
        # Define author with specific timestamp
        author = Actor("Osaf Ali ", "kingsayed02@gmail.com")
        author_time = int(time.mktime(time.strptime(commit_date, '%Y-%m-%d %H:%M:%S')))
        author_tz = "+0100"  # timezone offset

        # Commit with specific timestamp
        repo.index.commit(f"Commited on: {commit_date}", author=author, author_date=f"{author_time} {author_tz}")
        print(f"Commited on: {commit_date}")
    else:
        print("No changes to commit") 
        
def change_file_content(file_path):
    with open(file_path, "w") as file:
        file.write(str(datetime.now()))

def add_yearly_commits(repo, FILE_PATH):
    for x in range(0, 52):
        for y in range(0, 7):
            change_file_content(FILE_PATH)
            commit(repo, FILE_PATH, x, y)
    repo.git.push()
            
def add_random_commits(repo, FILE_PATH, no_of_commits):
    for i in range(no_of_commits):
        x = random.randint(15, 52)
        y = random.randint(0, 7)
        change_file_content(FILE_PATH)
        commit(repo, FILE_PATH, x, y)
    repo.git.push()
PATH = ""
FILE_PATH = "date.txt"

# Initializing the repo
repo = Repo(PATH)

add_random_commits(repo, FILE_PATH, 60)



    
