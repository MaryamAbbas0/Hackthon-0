import os
import shutil
from pathlib import Path

# Paths Setup
VAULT_PATH = Path(r"C:\Users\MR Soltions\Desktop\AI_Employee_Vault")
NEEDS_ACTION = VAULT_PATH / "Needs_Action"
DONE_FOLDER = VAULT_PATH / "Done"

# Folders bana lo agar nahi hain
DONE_FOLDER.mkdir(exist_ok=True)

def sort_tasks():
    print("Checking for new tasks...")
    files = [f for f in NEEDS_ACTION.iterdir() if f.is_file()]
    
    if not files:
        print("Koi naya task nahi mila.")
        return

    for file in files:
        # Silver Tier Logic: Agar file ke naam mein 'Urgent' hai toh prioritize karo
        if "urgent" in file.name.lower():
            print(f"URGENT task mil gaya: {file.name}")
            
        else:
            print(f"Normal task process ho raha hai: {file.name}")
        
        # Kaam khatam hone ke baad file ko 'Done' mein move kar do
        shutil.move(str(file), str(DONE_FOLDER / file.name))
        print(f"Task '{file.name}' Done folder mein move ho gaya.")

    # Dashboard update for Silver Tier status
    with open(VAULT_PATH / "Dashboard.md", "a", encoding="utf-8") as f:
        f.write(f"\n- [Silver Skill]: Task Sorter ran and processed {len(files)} files.")

if __name__ == "__main__":
    sort_tasks()



