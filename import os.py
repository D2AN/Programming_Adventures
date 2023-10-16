import os
import requests
import zipfile
import shutil

# GitHub repozitorijos savininko vardas ir repozitorijos pavadinimas
owner = "NIKASURG"
repo_name = "D2AN"

# Katalogas, kuriame atsisiųsti repozitoriją
appdata_folder = os.path.expanduser(f"~\\AppData\\Roaming\\PAadventures")

# Sukurkite `AppData` katalogą, jei jis neegzistuoja
os.makedirs(appdata_folder, exist_ok=True)

# Nuoroda į repozitorijos ZIP archyvą naudojant GitHub API
github_api_url = f"https://api.github.com/repos/{owner}/{repo_name}/zipball/D2AN"

# Nurodykite ZIP failo pavadinimą
zip_file_name = f"{owner}-{repo_name}-D2AN.zip"

# Atsisiųskite ZIP archyvą
response = requests.get(github_api_url)
if response.status_code == 200:
    zip_file_path = os.path.join(appdata_folder, zip_file_name)
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)
    print(f"ZIP archyvas atsisiųstas: {zip_file_path}")

    # Išskleiskite ZIP archyvą į katalogą
    extract_folder = os.path.join(appdata_folder, f"{owner}-{repo_name}-D2AN")
    os.makedirs(extract_folder, exist_ok=True)

    # Išskleiskite ZIP archyvą
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    # Nurodykite exe failo pavadinimą
    exe_name = "PAdventures.lnk"

    # Nurodykite kelią į exe failą
    exe_path = os.path.join(extract_folder, f"{owner}-{repo_name}-D2AN-main", exe_name)

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
else:
    print(f"Nepavyko atsisiųsti ZIP archyvo. HTTP statusas: {response.status_code}")
