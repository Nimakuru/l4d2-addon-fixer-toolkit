import os
import vpk
import subprocess
import shutil

def main():
    # --- SETTINGS ---
    # The folder containing the broken VPK files (Target folder from the Scanner script)
    target_folder = r"C:\L4D2_Repair"
    
    # Full path to the official L4D2 vpk.exe tool
    vpk_exe_path = r"D:\SteamLibrary\steamapps\common\Left 4 Dead 2\bin\vpk.exe"

    # Default content for the missing addoninfo.txt
    addon_content = """"AddonInfo"
{
	addonTitle			"Temporary-Title"
	addonVersion			"1.0"
	addonAuthor			"Python Script"
	addonDescription		"Missing addoninfo file has been added. You can edit info via VPKEdit program."
}"""

    print("Repair process starting...\n" + "-"*40)

    for file_name in os.listdir(target_folder):
        if file_name.endswith(".vpk") and not file_name.endswith("_000.vpk"):
            vpk_path = os.path.join(target_folder, file_name)
            mod_name = file_name.replace(".vpk", "")
            temp_folder = os.path.join(target_folder, mod_name)
            
            print(f"Processing [{file_name}]...")
            
            try:
                # Create a temporary extraction folder
                if not os.path.exists(temp_folder):
                    os.makedirs(temp_folder)
                    
                # Extract all files from the VPK
                pak = vpk.open(vpk_path)
                for file_path in pak:
                    full_target_path = os.path.join(temp_folder, file_path)
                    os.makedirs(os.path.dirname(full_target_path), exist_ok=True)
                    
                    file_data = pak.get_file(file_path).read()
                    
                    with open(full_target_path, 'wb') as f:
                        f.write(file_data)
                        
                # Create the missing addoninfo.txt file
                with open(os.path.join(temp_folder, "addoninfo.txt"), "w", encoding="utf-8") as f:
                    f.write(addon_content)
                    
                # Repack the folder using the official vpk.exe tool
                subprocess.run([vpk_exe_path, temp_folder], check=True)
                
                # Clean up the temporary folder after successful packing
                shutil.rmtree(temp_folder)
                
                print("  -> SUCCESS! Repacked in original format.\n")
                
            except Exception as e:
                print(f"  -> !!! ERROR: {e}\n")

    print("-" * 40)
    print("Process completed! All mods are now compliant with L4D2 standards.")

if __name__ == "__main__":
    main()