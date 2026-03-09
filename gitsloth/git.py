import subprocess
from gitsloth.exceptions import NotARepositoryError


def is_git_repository() -> bool:
    """
    Check whether the current directory is inside a Git repository.

    Returns:
        True if inside a Git repository, otherwise False.
    """
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_staged_diff() -> str:
    """
    Retrieve the diff of staged changes.

    Returns:
        A string containing the staged diff.
        Returns an empty string if no changes are staged.
    """
    result = subprocess.run(
        ["git", "diff", "--cached"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def create_commit(message: str) -> None:
    """
    Create a Git commit with the provided message.

    Args:
        message: The commit message to use.

    Raises:
        subprocess.CalledProcessError: If the git commit command fails.
    """
    result = subprocess.run(
        ["git", "commit", "-m", message],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        print(f"Commit failed:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, "git commit")

    print("Commit created successfully!")
    print(result.stdout)
