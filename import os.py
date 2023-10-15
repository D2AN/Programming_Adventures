import os
import subprocess

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