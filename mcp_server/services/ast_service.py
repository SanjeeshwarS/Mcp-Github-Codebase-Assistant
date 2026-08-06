import ast
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent / "workspace"

def find_function(repo_id: str, function_name: str) -> dict:
    repo_path = (WORKSPACE / repo_id).resolve()

    if not repo_path.is_dir():
        raise ValueError("Repository not found.")

    matches = []

    for file in repo_path.rglob("*.py"):
        try:
            source = file.read_text(
                encoding="utf-8",
                errors="replace",
            )
        except OSError:
            continue

        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == function_name:
                    matches.append(
                        {
                            "file": str(file.relative_to(repo_path)),
                            "line": node.lineno,
                        }
                    )
    return {
        "repo_id": repo_id,
        "function_name": function_name,
        "matches": matches,
    }
        

def find_class(repo_id: str, class_name: str) -> dict:
    """Find where a Python class is defined in a cloned repository."""
   
    repo_path = (WORKSPACE / repo_id).resolve()
    
    if not repo_path.is_dir():
        raise ValueError("Repository not found.")
    
    matches = []
    
    for file in repo_path.rglob("*.py"):
        try:
            source = file.read_text(
                encoding="utf-8",
                errors="replace",
            )
        except OSError:
            continue
        
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if node.name == class_name:
                    matches.append(
                        {
                            "file": str(file.relative_to(repo_path)),
                            "lineno": node.lineno
                        }
                    )
    return {
        "repo_id": repo_id,
        "class_name": class_name,
        "matches": matches
    }