import os
from google.genai import types  # type: ignore

def write_directory(working_directory, dir_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_dir_path = os.path.abspath(os.path.join(working_directory, dir_path))
    if not abs_dir_path.startswith(abs_working_dir):
        return f'Error: Cannot create directory "{dir_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(abs_dir_path, exist_ok=True)
        return f'Successfully created directory "{dir_path}"'
    except Exception as e:
        return f"Error: creating directory: {e}"
    
schema_write_directory = types.FunctionDeclaration(
    name="write_directory",
    description="Creates a directory within the working directory. If the directory already exists, it does nothing.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the directory to create, relative to the working directory.",
            ),
        },
        required=["dir_path"],
    ),
)