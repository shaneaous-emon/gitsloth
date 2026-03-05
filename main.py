# Importing libraries
import subprocess
import sys


# Checks whether the current working directory is inside a Git repository
def is_git_repository() -> bool:
    """
    Returns True if the current directory is inside a Git working tree,
    otherwise returns False.
    """
    try:
        # Run a Git command that succeeds only if we are inside a repository.
        # If the command fails, subprocess will raise CalledProcessError
        # because check=True is set.
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            stdout=subprocess.PIPE,  # Suppress standard output
            stderr=subprocess.PIPE,  # Suppress error output
        )
        return True

    except subprocess.CalledProcessError:
        # The command failed, meaning we are not inside a Git repository
        return False


# Main entry point of the application
def main() -> None:
    if not is_git_repository():
        print("Not inside a Git repository...")
        sys.exit(1)
    print("Git repository detected!")
    sys.exit(0)


# Execute the application only when the script is run directly,
# not when it is imported as a module.
if __name__ == "__main__":
    main()
