import shutil
import os
import time
from pathlib import Path


WATCH_FOLDER = Path(r"C:\Users\MR Soltions\Desktop\Dropzone") 
VAULT_NEEDS_ACTION = Path(r"C:\Users\MR Soltions\Desktop\AI_Employee_Vault\Needs_Action")


if not WATCH_FOLDER.exists(): 
    os.makedirs(WATCH_FOLDER)
    print(f"Folder create kar dia gaya hai: {WATCH_FOLDER}")

if not VAULT_NEEDS_ACTION.exists():
    os.makedirs(VAULT_NEEDS_ACTION)

print(f"--- AI Employee Watcher Shuru ---")
print(f"Monitoring: {WATCH_FOLDER}")

while True:
    try:
        # Folder check kar raha hai
        for file in WATCH_FOLDER.iterdir():
            if file.is_file():
                print(f"Nayi file mili: {file.name}")
                
                # 1. File ko Vault mein move karega
                shutil.move(str(file), str(VAULT_NEEDS_ACTION / file.name))
                
                # 2. Metadata file (.md) banayega Obsidian ke liye
                meta_path = VAULT_NEEDS_ACTION / f"FILE_{file.name}.md"
                with open(meta_path, "w") as f:
                    f.write(f"---\ntype: file_drop\nstatus: pending\ndate: {time.ctime()}\n---\n\n")
                    f.write(f"## New File Detected\n\nAI Employee, please process this file: **{file.name}**")
                
                print(f"Done: File aur Metadata Vault mein bhej di gayi hain.")
                
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(5) # Har 5 second baad check karega




