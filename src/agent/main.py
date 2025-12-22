import shutil
from pathlib import Path


def move_file(filename: str):
    downloads = Path.home() / "OneDrive" / "Desktop"
    documents = Path.home() / "OneDrive" / "Documents"

    source = downloads / filename
    destination = documents / filename

    if not source.exists():
        return f"ERROR: {filename} not found in Downloads."

    shutil.move(str(source), str(destination))
    return f"SUCCESS: {filename} moved to Documents."


def agent(user_input: str):
    """
    Very simple agent logic:
    - Extract filename
    - Call move_file tool
    """

    # naive extraction (good enough for MVP)
    words = user_input.split()
    filename = next((w for w in words if w.endswith(".xlsx")), None)

    if not filename:
        return "ERROR: No Excel file specified."

    result = move_file(filename)
    return result


if __name__ == "__main__":
    user_request = "Move my budget.xlsx from Downloads to Documents"
    response = agent(user_request)
    print(response)
