# python/helpers/file_system_manager.py
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, TypedDict, Literal, Union

# Get the Phoenix agent work directory from environment variable
PHOENIX_AGENT_WORK_DIR = Path(os.getenv("PHOENIX_AGENT_WORK_DIR", "/tmp/phoenix_work_dir")).resolve()

class FileBrowserItem(TypedDict):
    name: str
    type: Literal["file", "directory", "error"]
    path: str  # Relative path from PHOENIX_AGENT_WORK_DIR
    size: Optional[int]  # In bytes, for files only
    last_modified: Optional[str]  # ISO format string
    error_message: Optional[str]  # For error items

def ensure_work_dir_exists():
    """Ensure the work directory exists, create if it doesn't."""
    try:
        PHOENIX_AGENT_WORK_DIR.mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"FileSystemManager ERROR: Could not create work directory {PHOENIX_AGENT_WORK_DIR}: {e}")
        return False

def list_directory_contents(requested_path_str: str = "") -> Dict[str, Union[str, List[FileBrowserItem], None]]:
    """
    Lists contents of a directory within the PHOENIX_AGENT_WORK_DIR.
    Ensures path is safe and within the allowed base directory.
    
    Args:
        requested_path_str: Relative path from PHOENIX_AGENT_WORK_DIR root
        
    Returns:
        Dict with keys: 'path', 'items', 'error'
    """
    try:
        # Ensure work directory exists
        if not ensure_work_dir_exists():
            return {
                "error": "Work directory could not be created or accessed.",
                "path": requested_path_str,
                "items": []
            }
        
        # Normalize and resolve the requested path relative to the base work directory
        # Remove leading slash if present (treat as relative to work dir root)
        if requested_path_str.startswith('/'):
            requested_path_str = requested_path_str.lstrip('/')
        
        # Handle empty path or "." as root
        if not requested_path_str or requested_path_str == ".":
            requested_path_str = ""
            
        current_path = (PHOENIX_AGENT_WORK_DIR / requested_path_str).resolve()

        # Security Check: Ensure the resolved path is still within PHOENIX_AGENT_WORK_DIR
        if not str(current_path).startswith(str(PHOENIX_AGENT_WORK_DIR)):
            return {
                "error": "Access denied: Path is outside the allowed working directory.",
                "path": requested_path_str,
                "items": []
            }

        if not current_path.exists():
            return {
                "error": "Path does not exist.",
                "path": requested_path_str,
                "items": []
            }
            
        if not current_path.is_dir():
            return {
                "error": "Path is not a directory.",
                "path": requested_path_str,
                "items": []
            }

        items: List[FileBrowserItem] = []
        
        for entry in current_path.iterdir():
            try:
                item_type = "directory" if entry.is_dir() else "file"
                # Relative path from PHOENIX_AGENT_WORK_DIR for client-side navigation
                relative_path = str(entry.relative_to(PHOENIX_AGENT_WORK_DIR)).replace("\\", "/")
                
                item_data: FileBrowserItem = {
                    "name": entry.name,
                    "type": item_type,
                    "path": relative_path,
                    "size": entry.stat().st_size if item_type == "file" else None,
                    "last_modified": datetime.fromtimestamp(entry.stat().st_mtime).isoformat(),
                    "error_message": None
                }
                items.append(item_data)
                
            except Exception as e:  # Catch permission errors for individual files
                print(f"FileBrowser: Error processing entry {entry.name}: {e}")
                items.append({
                    "name": entry.name,
                    "type": "error",
                    "path": str(entry.relative_to(PHOENIX_AGENT_WORK_DIR)).replace("\\", "/"),
                    "size": None,
                    "last_modified": None,
                    "error_message": str(e)
                })

        # Sort: directories first, then files, all alphabetically
        items.sort(key=lambda x: (x["type"] == "file", x["name"].lower()))
        
        # Path to return to client should be relative to PHOENIX_AGENT_WORK_DIR root
        display_path = "/" + str(current_path.relative_to(PHOENIX_AGENT_WORK_DIR)).replace("\\", "/") if current_path != PHOENIX_AGENT_WORK_DIR else "/"
        if display_path == "/.":
            display_path = "/"

        return {
            "path": display_path,
            "items": items,
            "error": None
        }

    except Exception as e:
        print(f"FileBrowser: General error listing directory '{requested_path_str}': {e}")
        return {
            "error": f"Error listing directory: {str(e)}",
            "path": requested_path_str,
            "items": []
        }

def get_work_dir_info() -> Dict[str, str]:
    """Get information about the work directory."""
    return {
        "work_dir_path": str(PHOENIX_AGENT_WORK_DIR),
        "exists": str(PHOENIX_AGENT_WORK_DIR.exists()),
        "is_directory": str(PHOENIX_AGENT_WORK_DIR.is_dir()) if PHOENIX_AGENT_WORK_DIR.exists() else "False"
    }
