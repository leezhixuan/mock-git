import os

from MgitRepository import MgitRepository
from utils import repo_dir, repo_file, repo_default_config

def init(args):
    """
    Initializes a MGit repository
    Syntax: mgit init [path]
    """
    repo_create(args.path)

def repo_create(path):
    "Creates a new repository at the file path"

    repo = MgitRepository(path, True)

    if os.path.exists(repo.workTreeDir):
        if not os.path.isdir(repo.workTreeDir):
            raise Exception(f"{path} is not a directory.")
            

        if os.listdir(repo.workTreeDir):
            raise Exception(f"{path} is not empty.")
    
    else:
        os.makedirs(repo.workTreeDir)

    assert(repo_dir(repo, "branches", mkdir=True))
    assert(repo_dir(repo, "objects", mkdir=True))
    assert(repo_dir(repo, "refs", "tags", mkdir=True))
    assert(repo_dir(repo, "refs", "heads", mkdir=True))

    with open(repo_file(repo, "description"), "w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

    with open(repo_file(repo, "HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    with open(repo_file(repo, "config"), "w") as f:
        config = repo_default_config()
        config.write(f)

    return repo
