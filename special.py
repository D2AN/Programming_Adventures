import subprocess

# Komanda, kuri bus vykdoma CMD
command = 'curl parrot.live'

try:
    # Paleidžiame CMD su curl komanda
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f'Komandos vykdymo klaida: {e}')
except Exception as e:
    print(f'Klaida: {e}')