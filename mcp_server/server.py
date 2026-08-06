from fastmcp import FastMCP
from services.repository_service import clone_public_repository
from services.parser_service import read_file, get_folder_structure
from services.ast_service import find_function , find_class
from services.search_service import search_code

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
def read_repository_file(repo_id: str, file_path: str) -> dict:
    """Read a file from a cloned repository."""

    try:
        return read_file(repo_id, file_path)  
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not read this file."}
    
@mcp.tool
def find_repository_function(repo_id: str,function_name: str) -> dict:
    """Find where a Python function is defined in a cloned repository."""

    try:
        return find_function(repo_id,function_name)
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not search for the function."}
    
@mcp.tool
def find_repository_class(repo_id:  str,class_name: str) -> dict:
    """Find where a Python class is defined in a cloned repository."""
    
    try:
        return find_class(repo_id,class_name)
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error": "Could not search for the class."}
    
@mcp.tool
def search_repository_code(repo_id: str,query: str) -> dict:
    """Search for the keyword across every file in a cloned repository."""
    
    try:
        return search_code(repo_id,query)
    except ValueError as error:
        return {"error": str(error)}
    except Exception:
        return {"error":"Could not search the repository"}


if __name__ == "__main__":
    mcp.run(transport="stdio")
    
