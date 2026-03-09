class GitslothError(Exception):
    """Base exception for all Gitsloth errors."""


class NotARepositoryError(GitslothError):
    """Raised when the current directory is not a Git repository."""


class NoStagedChangesError(GitslothError):
    """Raised when there are no staged changes to commit."""


class TokenLimitExceededError(GitslothError):
    """Raised when the staged diff exceeds the maximum token estimate."""
