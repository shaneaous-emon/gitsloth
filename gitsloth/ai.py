import os
import openai

COMMIT_PROMPT_TEMPLATE: str = """
You are an expert software engineer that writes precise commit messages
following the Conventional Commits specification.

Generate {n} different commit messages for the following changes.

Rules:

1. Use the Conventional Commits format:
   <type>(optional scope): <short summary>

2. Allowed types:
   feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert

3. The summary must:
   - Be lowercase
   - Use imperative mood (e.g., "add", "fix")
   - Not end with a period
   - Be concise (max 72 characters)

4. If the change is breaking:
   - Add an exclamation mark after the type/scope (e.g., feat!:)
   - Add a "BREAKING CHANGE:" footer

5. Include a body separated by a blank line if additional context is needed.

Return ONLY the commit messages as a numbered list.

Changes:
{diff}
"""


def estimate_token_count(text: str) -> int:
    """
    Roughly estimate the number of tokens in a string.

    This approximation assumes ~4 characters per token.

    Args:
        text: The input text.

    Returns:
        Estimated token count.
    """
    return len(text) // 4


def generate_commit_messages(diff: str, n: int) -> list[str]:
    """
    Generate multiple Conventional Commit messages from a Git diff.

    Args:
        diff: The staged git diff.
        n: Number of commit suggestions to generate.

    Returns:
        A list containing up to `n` commit message suggestions.

    Raises:
        EnvironmentError: If the OPENAI_API_KEY is not set.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

    client = openai.OpenAI(api_key=api_key)
    prompt = COMMIT_PROMPT_TEMPLATE.format(diff=diff, n=n)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "You generate high quality git commit messages.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    response_text = response.choices[0].message.content.replace("```", "").strip()

    commits = []

    for line in response_text.split("\n"):
        line = line.strip()

        if not line:
            continue

        if "." in line:
            line = line.split(".", 1)[1].strip()

        commits.append(line)

    return commits[:n]
