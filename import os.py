import os
import requests
import zipfile

# Nurodykite GitHub repozitorijos ZIP archyvo URL
repo_url = "https://github.com/NIKASURG/D2AN/raw/D2AN/PAadventures.zip"

# Katalogas, kuriame atsisiųsti ZIP archyvą
appdata_folder = os.path.expanduser(f"~\\AppData\\Roaming\\PAadventures")

# Sukurkite `AppData` katalogą, jei jis neegzistuoja
os.makedirs(appdata_folder, exist_ok=True)

# Atsisiųskite ZIP archyvą
response = requests.get(repo_url)
if response.status_code == 200:
    zip_file_path = os.path.join(appdata_folder, "PAadventures.zip")
    with open(zip_file_path, "wb") as f:
        f.write(response.content)

    # Išpakuokite ZIP archyvą į `AppData` katalogą
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(appdata_folder)

    os.remove(zip_file_path)  # Ištrinti ZIP archyvą po išpakavimo
else:
    print(f"Klaida atsiunčiant ZIP archyvą. HTTP statusas: {response.status_code}")
