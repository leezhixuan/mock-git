import configparser
import os

from utils import repo_file

class MgitRepository:
    "An MGit Repository"

    workTreeDir = None # path
    mGitDir = None # path
    config = None

    def __init__(self, path, force=False):
        self.workTreeDir = path
        self.workTreeDir = os.path.join(path, ".git")
        
        if not (force or os.path.isdir(self.gitDir)):
            raise Exception(f"{path} is not a MGit repository")

        
        self.config = configparser.ConfigParser()
        cf = repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])

        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            version = int(self.config.get("core", "repositoryformatversion"))
            
            if version != 0:
                raise Exception(f"Unsupported repositoryformatversion: {version}")


    
