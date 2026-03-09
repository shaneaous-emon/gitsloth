import sys
import argparse
from halo import Halo
import questionary

from gitsloth.git import is_git_repository, get_staged_diff, create_commit
from gitsloth.ai import generate_commit_messages, estimate_token_count
from gitsloth.ui import choose_commit
from gitsloth.exceptions import (
    NotARepositoryError,
    NoStagedChangesError,
    TokenLimitExceededError,
)

MAX_TOKEN_ESTIMATE = 6_000


def parse_args() -> argparse.Namespace:
    """
    Parse CLI arguments.

    Returns:
        The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate AI-powered Git commit messages."
    )

    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser(
        "list", help="Generate multiple commit suggestions"
    )
    list_parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=5,
        help="Number of commit suggestions to generate",
    )

    return parser.parse_args()


def main() -> None:
    """
    CLI entry point for the AI commit generator.

    Workflow:
        1. Ensure the current directory is a Git repository.
        2. Retrieve staged changes.
        3. Generate commit message suggestions using OpenAI.
        4. Allow the user to select or confirm a message.
        5. Create the Git commit.
    """
    try:
        args = parse_args()

        if not is_git_repository():
            raise NotARepositoryError("Not inside a Git repository.")

        diff = get_staged_diff()

        if not diff:
            raise NoStagedChangesError("No staged changes found.")

        if estimate_token_count(diff) > MAX_TOKEN_ESTIMATE:
            raise TokenLimitExceededError("Diff exceeds the maximum token estimate.")

        n = args.num if args.command == "list" else 1

        with Halo(text="Generating commit messages...", spinner="dots"):
            commits = generate_commit_messages(diff, n)

        if args.command == "list":
            message = choose_commit(commits)
        else:
            message = commits[0]
            print(message)

        if not questionary.confirm("Commit with this message?", qmark="").ask():
            print("Commit aborted.")
            sys.exit(0)

        create_commit(message)

    except (NotARepositoryError, NoStagedChangesError, TokenLimitExceededError) as e:
        print(f"Error: {e}")
        sys.exit(1)
