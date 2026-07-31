import re
import subprocess
from pathlib import Path

GITHUB_URL_PATTERN = re.compile(
    r"^https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+?)(?:\.git)?/?$"
)

WORKSPACE = Path(__file__).parent / "workspace"

def clone_public_repository(repo_url: str) -> dict:
    """Clone a public Github repoistory with only its latest commit."""
    match=GITHUB_URL_PATTERN.fullmatch(repo_url.strip())
    
    if not match:
        raise ValueError(
            "Use a public URL like https://github.com/owner/repository"
        )
        
    owner = match.group("owner")
    repo = match.group("repo")
    repo_id = f"{owner.lower()}--{repo.lower()}"
    
    WORKSPACE.mkdir(exist_ok=True)
    target_path = WORKSPACE / repo_id
    
    if target_path.exists():
        return {
            "repo_id": repo_id,
            "message": "Repository already exists locally.",
        }
    
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            repo_url,
            str(target_path)
        ],
            check=True,
            capture_output=True,
            text=True,
    )
    
    
    return {
        "repo_id": repo_id,
        "message": "Repository cloned successfully.",
    }