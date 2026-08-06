from pathlib import Path

WORKSPACE = Path(__file__).parent.parent / "workspace"

def search_code(repo_id: str, query: str) -> str:
    """Search a keyword across every file in a cloned repository."""
    
    repo_path = (WORKSPACE / repo_id).resolve()
    
    if not repo_path.is_dir():
        raise ValueError("Repository not found.")
    
    matches = []
    
    for file in repo_path.rglob("*"):
        
        if not file.is_file():
            continue
        
        try:
            lines = file.read_text(
                encoding="utf-8",
                errors="replace",
            ).splitlines()
            
        except OSError:
            continue
        
        for line_number , line in enumerate(lines, start=1):
            if query.lower() in line.lower():
                
                matches.append(
                    {
                        "file": str(file.relative_to(repo_path)),
                                        "line": line_number,
                                        "text": line.strip(),
                    }
                )
                
        return {
            "repo_id": repo_id,
            "query": query,
            "matches": matches,
        }