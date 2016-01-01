#!/usr/bin/env python3
"""
Query GitHub for information about Software Carpentry's Git repositories at GitHub.

For information about GitHub API check
https://github.com/PyGithub/PyGithub and
https://developer.github.com/v3/.

To run as stand-alone, ::

    $ git.py token

To run as script, ::

        set_connection(token)
        generate_text()

"""
import sys
import github
# If you need to debug,
# uncomment the next line will help.
# github.enable_console_debug_logging()

GITHUB = None

REPOS = [
        "swcarpentry/website",  # For the future
        "swcarpentry/board",
        "swcarpentry/instructor-training",
        "swcarpentry/workshop-template",
        "swcarpentry/amy",
        "swcarpentry/communications",
        "swcarpentry/git-novice",
        "swcarpentry/hg-novice",
        "swcarpentry/hpc-novice",
        "swcarpentry/lesson-template",
        "swcarpentry/make-novice",
        "swcarpentry/matlab-novice-inflammation",
        "swcarpentry/python-intermediate",
        "swcarpentry/python-intermediate-mosquitoes",
        "swcarpentry/python-novice-inflammation",
        "swcarpentry/python-testing",
        "swcarpentry/r-novice-gapminder",
        "swcarpentry/r-novice-inflammation",
        "swcarpentry/shell-extras",
        "swcarpentry/shell-novice",
        "swcarpentry/sql-novice-survey",
        "swcarpentry/windows-installer",
        ]

def set_connection(token):
    """
    Set connection to GitHub.

    :param token: Token for GitHub API.
    """
    global GITHUB
    GITHUB = github.Github(token)

def get_data(repo_id):
    """
    Query GitHub.

    :param repo_id: unique ID of the repo
    :rtype: github.StatsContributor.StatsContributor
    """
    if GITHUB:
        repo = GITHUB.get_repo(repo_id)

        return repo.get_stats_contributors()

def pprint_statistics(data):
    """
    Pretty print statistics about data.

    :param data: github.StatsContributor.StatsContributor
    :rtype: list of strings
    """
    text = []
    contributors = []

    for contributor in data:
        number_of_commits = contributor.weeks[-1].c
        if number_of_commits > 0:
            contributors.append([
                "{} (@{})".format(contributor.author.name, contributor.author.login),
                number_of_commits,
                ])

    contributors.sort(key=lambda item: item[1], reverse=True)

    for contributor in contributors:
        text.append("| {} | {} |\n".format(
            contributor[0],
            contributor[1],
            ))

    return text

def generate_text():
    """
    Generate text
    """
    text = []
    for repo_id in REPOS:
        data = get_data(repo_id)
        stats = pprint_statistics(data)
        if stats:
            text.append("{}\n".format(repo_id))
            text.append("\n")
            text.extend(pprint_statistics(data))
            text.append("\n")

    return("".join(text))

def main():
    """
    Main function
    """
    if len(sys.argv) >= 2:
        set_connection(sys.argv[1])
        print(generate_text())
    else:
        print("Need to provide a token for GitHub")

if __name__ == "__main__":
    main()
