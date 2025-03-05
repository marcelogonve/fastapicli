# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from InquirerPy import prompt
import typer
from cli.config import messages

app = typer.Typer()

@app.command()
def new():
    typer.echo(messages["welcome"])

    project_name = prompt([{
        "type": "input",
        "message": messages["project_name"],
        "name": "project_name"
    }])["project_name"]

    directory = prompt([{
        "type": "input",
        "message": messages["directory"],
        "name": "directory",
        "default": "."
    }])["directory"]

    db_type = prompt([{
        "type": "list",
        "message": messages["database"],
        "name": "db_type",
        "choices": ["postgres", "mysql", "sqlite", "mongodb"],
        "default": "postgres"
    }])["db_type"]

    use_docker = prompt([{
        "type": "confirm",
        "message": messages["docker"],
        "name": "use_docker",
        "default": True
    }])["use_docker"]

    use_git = prompt([{
        "type": "confirm",
        "message": messages["git"],
        "name": "use_git",
        "default": True
    }])["use_git"]

    package_manager = prompt([{
        "type": "list",
        "message": messages["package_manager"],
        "name": "package_manager",
        "choices": ["pip", "pipenv", "poetry"],
        "default": "pip"
    }])["package_manager"]

    typer.echo("\n" + messages["summary"])
    typer.echo(f"   - {messages['project_name']}: {project_name}")
    typer.echo(f"   - {messages['directory']}: {directory}")
    typer.echo(f"   - {messages['database']}: {db_type}")
    typer.echo(f"   - {messages['docker']}: {messages['ok'] if use_docker else 'No'}")
    typer.echo(f"   - {messages['git']}: {messages['ok'] if use_git else 'No'}")
    typer.echo(f"   - {messages['package_manager']}: {package_manager}")

    confirm = prompt([{
        "type": "confirm",
        "message": messages["confirm_creation"],
        "name": "confirm",
        "default": True
    }])["confirm"]

    if confirm:
        typer.echo(messages["success"])
        # Aquí puedes agregar la lógica para crear el proyecto
    else:
        typer.echo(messages["canceled"])

if __name__ == "__main__":
    app()
