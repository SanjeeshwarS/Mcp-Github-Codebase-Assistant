from pathlib import Path

WORKSPACE = Path(__file__).parent / "workspace"

IGNORED_FOLDERS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
}

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
    repo_path = WORKSPACE / repo_id
    
    if not repo_path.exists():
        raise ValueError("Repositor Not Found")
    
    return {
        "repo_id": repo_id,
        "structure": build_tree(repo_path)
    }
   