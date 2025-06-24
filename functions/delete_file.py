import os
from google.genai import types  # type: ignore

def delete_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot delete file "{file_path}" as it is outside the permitted working directory'
    try:
        os.remove(abs_file_path)
        return f'Successfully deleted file "{file_path}"'
    except FileNotFoundError:
        return f'Error: File "{file_path}" does not exist'
    except Exception as e:
        return f"Error: deleting file: {e}"

schema_delete_file = types.FunctionDeclaration(
    name="delete_file",
    description="Deletes a file within the working directory. If the file does not exist, it        returns an error message.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to delete, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)