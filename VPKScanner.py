import os
import shutil
import vpk

def main():
    # --- SETTINGS ---
    # Update these paths according to your local system setup.
    addons_path = r"C:\Program Files (x86)\Steam\steamapps\common\Left 4 Dead 2\left4dead2\addons"
    target_folder = r"C:\L4D2_Repair"

    # Create the target directory if it doesn't exist
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