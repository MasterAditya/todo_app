
from pathlib import Path

def setup_project():
    # Define the project structure
    # Directories end with a slash, files do not
    structure = [
        "todo_app/app/templates/index.html",
        "todo_app/app/main.py",
        "todo_app/app/models.py",
        "todo_app/app/database.py",
        "todo_app/app/schemas.py",
        "todo_app/requirements.txt",
        "todo_app/README.md",
    ]

    for item in structure:
        path = Path(item)
        
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the empty file
        path.touch(exist_ok=True)
        print(f"Created: {path}")

if __name__ == "__main__":
    setup_project()
    print("\nProject structure created successfully!")