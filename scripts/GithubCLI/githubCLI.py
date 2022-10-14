from github import Github
from rich.console import Console
from rich.table import Table
import typer
from rich import print
from rich.panel import Panel
from rich.console import Group
import random

app = typer.Typer()
console = Console()

# Create your token from https://github.com/settings/tokens/new
# Select repo and user scope
g = Github("ADD_YOUR_OWN")


@app.command()
def showall():
    print("\n\n")
    user = g.get_user()
    table = Table("Repo Name", "URL", "Stars", "Open Issues", )
    for repo in user.get_repos():
        r = lambda: random.randint(0, 255)
        color = str('#%02X%02X%02X' % (r(), r(), r()))
        table.add_row("[bold " + color + "]" + repo.name, "[bold " + color + "]" + repo.url,
                      "[bold " + color + "]" + str(repo.stargazers_count),
                      "[bold " + color + "]" + str(repo.open_issues_count),
                      )
    group = Group(
        table,
    )
    print(Panel(group, title="[bold underline purple]All Repos of " + user.name))
    print("\n\n")


@app.command()
def showproject(name: str):
    repo = g.get_user().get_repo(name=name)
    print("\n\n")
    table = Table("Name", "Contributions")
    for contributor in repo.get_contributors():
        r = lambda: random.randint(0, 255)
        color = str('#%02X%02X%02X' % (r(), r(), r()))
        table.add_row("[bold " + color + "]" + contributor.name,
                      "[bold " + color + "]" + str(contributor.contributions))
    group = Group(
        "[bold green]Owner:[/bold green] " + "[bold]" + repo.owner.name + "[/bold]\n"
                                                                          "[bold blue]URL:[/bold blue] " + "[bold]" + repo.url + "[/bold]\n"
                                                                                                                                 "[bold #ecc73c]Stars:[/bold #ecc73c] " + "[bold]" + str(
            repo.stargazers_count) + "[/bold]",
        "[bold blue]Forks:[/bold blue] " + "[bold]" + str(repo.forks_count) + "[/bold]",
        "[bold #6a5b64]Watchers:[/bold #6a5b64] " + "[bold]" + str(repo.watchers_count) + "[/bold]",
        "[bold red]Issues:[/bold red] " + "[bold]" + str(repo.open_issues_count) + "[/bold]",
        table,
    )
    print(Panel(group, title="[bold underline purple]Details of " + repo.name))
    print("\n\n")


if __name__ == "__main__":
    app()
