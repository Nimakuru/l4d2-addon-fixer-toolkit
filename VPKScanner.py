import os

print("--- Welcome to L4D2 VPK Scanner Tool ---")

# Get the file path from the user and remove leading and trailing spaces (.strip)
addons_path = input("Please select where L4D2 addons were located:\n> ").strip()

# Loop until the user enters a valid folder (Error Handling)
while not os.path.exists(addons_path):
    print("\n[ERROR] The folder you entered could not be found! You may have copied the path incorrectly.")
    addons_path = input("Please paste the folder path again:\n> ").strip()

print(f"\n[SUCCESSFUL] Folder found: {addons_path}")
print("Starting to Scanning\n")

import shutil
import vpk

def main():
    # --- SETTINGS ---
    # Create the target directory if it doesn't exist
    target_folder = r"C:\L4D2_Repair"
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    print(f"Scanning started... Missing VPKs will be copied to '{target_folder}'.")
    print("-" * 50)

    copied_count = 0

    for file_name in os.listdir(addons_path):
        if file_name.endswith(".vpk"):
            vpk_path = os.path.join(addons_path, file_name)
            
            try:
                # Open VPK and check if 'addoninfo.txt' exists inside
                pak = vpk.open(vpk_path)
                is_found = any("addoninfo.txt" in d.lower() for d in pak)
                
                # If missing, copy to the target folder for manual repair
                if not is_found:
                    target_path = os.path.join(target_folder, file_name)
                    shutil.copy2(vpk_path, target_path) 
                    copied_count += 1
                    
                    print(f"[COPIED] -> {file_name}")
                    
            except Exception as e:
                print(f"!!! [ERROR] -> Could not process {file_name}: {e}")

    print("-" * 50)
    print(f"Process completed! A total of {copied_count} mods were copied to '{target_folder}'.")
    print("You can now check the mods with VPKedit program and use repair tool to add .txt files.")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
