import configparser
import os

def repo_path(repo, *path):
    " Compute path under repo's gitDir."
    return os.path.join(repo.gitDir, *path)


def repo_file(repo, *path, mkdir=False):
    """Same as repo_path, but create dirname(*path) if absent. 
    repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
    .git/refs/remotes/origin."""

    if repo_dir(repo, *path[:-1], mkdir=mkdir):
        return repo_path(repo, *path)

def repo_dir(repo, *path, mkdir=False):
    """Same as repo_path, but mkdir *path if absent if mkdir."""

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception(f"{path} not a directory.")

    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None

def repo_default_config():
    """
    Config file is an INI-like file with a single section [core] and 3 fields:
    1. repositoryformatversion = 0, the version of the  mgitDir format. 0 = initial format. = the same with extensions.
    2. filemode = false, to disable tracking of file mode changes in the work tree
    3. bare = false, to indicae that this repositoru has a worktree.
    """
    configParser = configparser.ConfigParser()

    configParser.add_section("core")
    configParser.set("core", "repositoryformatversion", "0")
    configParser.set("core", "filemode", "false")
    configParser.set("core", "bare", "false")

    return configParser
    