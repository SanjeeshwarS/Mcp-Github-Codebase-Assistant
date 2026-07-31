from pathlib import Path

WORKSPACE = Path(__file__).parent / "workspace"

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
    
