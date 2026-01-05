#Setup Script to Prevent Merge Conflicts

import os
import subprocess
import sys

def run_command(command, description):
    print(f"--- {description} ---")
    try:
        subprocess.check_call(command, shell=True)
        print(f"Done: {description}")
    except subprocess.CalledProcessError:
        print(f"Failed: {description}")
        sys.exit(1)
        
def main():
    #Install dependencies
    run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing dependencies")
    
    #Install version control tools
    run_command("nbstripout --install", "Installing nbstripout for notebook version control")
    
    #Create necessary directories
    create_directories()
    
    print("Setup completed successfully")
    
def create_directories():
    folders = ["notebooks", "scripts", "notebooks/data"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Ensured directory exists: {folder}")

if __name__ == "__main__":
    main()