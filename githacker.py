from datetime import datetime
from git import Repo, Actor
import time

PATH = ""
with open("date.txt", "w") as file:
    # write the current date and time to the file
    file.write(str(datetime.now()))

# Initialize a Repo object
repo = Repo(PATH)

# # Check for changes
# Check for changes
if repo.is_dirty():
    # Add specific file
    repo.git.add('date.txt')
    commit_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Define author with specific timestamp
    author = Actor("Osaf Ali ", "kingsayed02@gmail.com")
    author_time = int(time.mktime(time.strptime(commit_date, '%Y-%m-%d %H:%M:%S')))
    author_tz = "+0100"  # timezone offset

    # Commit with specific timestamp
    repo.index.commit(f"Commited on: {commit_date}", author=author, author_date=f"{author_time} {author_tz}")
else:
    print("No changes to commit")
