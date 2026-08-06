from pathlib import Path

WORKSPACE = Path(__file__).parent.parent / "workspace"

IGNORED_FOLDERS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

#for reading and parsing repos

def build_tree(path: Path):
    tree = {}
    
    for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        
        if item.name in IGNORED_FOLDERS:
            continue
        
        if item.is_dir():
            tree[item.name] = build_tree(item)
        else:
            tree[item.name] = None
            
    return tree

def get_folder_structure(repo_id: str) -> dict:
    repo_path = (WORKSPACE / repo_id).resolve()
    
    if not repo_path.exists():
        raise ValueError("Repositor Not Found")
    
    return {
        "repo_id": repo_id,
        "structure": build_tree(repo_path)
    }
    
#read_file
def read_file(repo_id: str, file_path: str) -> dict:
    """Read a file from a cloned repository."""
    
    repo_path = (WORKSPACE / repo_id).resolve()
    
    if not repo_path.is_dir():
        raise ValueError("Repository Not Found.")
    
    target_file = (repo_path / file_path ).resolve()
    
    if repo_path not in target_file.parents and target_file != repo_path:
        raise ValueError("Invalid file path.")

    if not target_file.exists():
        raise ValueError("File Not Found.")
    
    if not target_file.is_file():
        raise ValueError("The given path is not a file.")
    
    try:
        content = target_file.read_text(
            encoding="utf-8",
            errors="replace",
        )
    except OSError as error:
        raise ValueError(f"Could not read the file: {error}")
    
    return {
        "repo_id": repo_id,
        "file_path": file_path,
        "content": content,
    }
    
