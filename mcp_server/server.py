from fastmcp import FastMCP
from repository_service import clone_public_repository
from parser_service import get_folder_structure
from file_reader_service import read_file

mcp = FastMCP("Github Codebase Assistant")

@mcp.tool
def clone_repository(repo_url: str) -> dict:
    """Clone a public GitHub repository and return its repo_id"""
    
    try:
        return clone_public_repository(repo_url)
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not clone the repository."}
    
@mcp.tool
def get_repository_structure(repo_id: str) -> dict:
    """Return the folder structure of a cloned repository."""
    
    try:
        return get_folder_structure(repo_id)
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not retrieve the repository structure."}
    
@mcp.tool
def read_repositor_file(repo_id: str, file_path: str) -> dict:
    """Read a file from a cloned repository."""

    try:
        return read_file(repo_id, file_path)  
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not read this file."}
    
if __name__ == "__main__":
    mcp.run(transport="stdio")
    
