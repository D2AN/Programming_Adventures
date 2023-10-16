import os
import subprocess
import shutil

# GitHub repozitorijos savininko vardas ir repozitorijos pavadinimas
owner = "NIKASURG"
repo_name = "D2AN"

# Katalogas, kuriame atsisiųsti repozitoriją
appdata_folder = os.path.expanduser(f"~\\AppData\\Roaming\\PAadventures")

# Sukurkite `AppData` katalogą, jei jis neegzistuoja
os.makedirs(appdata_folder, exist_ok=True)

# Git komanda norint atsisiųsti repozitoriją
git_clone_command = f"git clone https://github.com/{owner}/{repo_name}.git {appdata_folder}"

# Atsisiųskite repozitoriją naudodami Git komandą
subprocess.run(git_clone_command, shell=True)

# Nurodykite exe failo pavadinimą
exe_name = "PAdventures.lnk"

# Nurodykite kelią į exe failą
exe_path = os.path.join(appdata_folder, exe_name)

# Tikriname, ar exe failas yra
if os.path.exists(exe_path):
    print(f"{exe_name} failas suinstaliuotas.")

    # Katalogas, kuriame yra darbalaukio nuorodos
    desktop_folder = os.path.expanduser(f"~\\Desktop")

    # Kelias į darbalaukio nuorodą
    desktop_link_path = os.path.join(desktop_folder, exe_name)

    # Perkelkite nuorodą į darbalaukį
    shutil.move(exe_path, desktop_link_path)

    print(f"{exe_name} nuoroda perkelta į darbalaukį.")
else:
    print(f"{exe_name} failas nerastas. Kelias: {exe_path}")