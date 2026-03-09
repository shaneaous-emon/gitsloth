import questionary


def choose_commit(commits: list[str]) -> str:
    """
    Prompt the user to select a commit message from a list.

    Args:
        commits: A list of commit message suggestions.

    Returns:
        The selected commit message.
    """
    return questionary.select(
        "Proposed commit messages:", choices=commits, qmark=""
    ).ask()
