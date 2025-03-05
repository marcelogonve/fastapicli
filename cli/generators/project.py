import os
import re
import typer

def load_structure(file_path):
    structure = {"folders": [], "files": {}}
    current_section = None
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line.startswith("folders:"):
                current_section = "folders"
                continue
            if line.startswith("files:"):
                current_section = "files"
                continue
            if not line or current_section is None:
                continue

            if current_section == "folders":
                structure["folders"].append(line.lstrip("- ").strip())
            elif current_section == "files":
                key, value = re.split(r":\s*", line, maxsplit=1)
                structure["files"][key.strip()] = value.strip()

    return structure

def create_project_structure(
    project_name,
    directory,
    db_type,
    user_docker,
    use_git,
    package_manager
):
    project_path = os.path.join(directory, project_name)
    structure = load_structure(os.path.join(os.path.dirname(__file__), "templates/structure.md"))