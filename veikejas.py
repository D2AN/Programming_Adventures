import re

# Funkcija skirta atskirti skaičius nuo teksto ir grąžinti juos kaip eilutės ir skaičiaus sąrašą
def separateNumbersText(text):
    # Išskiriame visus skaičius, kurie turi bent vieną skaitmenį
    numbers = re.findall(r'\d+', text)
    
    # Pašaliname iš teksto visus skaitmenis ir kitus simbolius, išskyrus tuos, kurie yra tarpuose
    text_without_numbers = re.sub(r'\d+', '', text)
    
    return numbers, text_without_numbers.strip()

# Testavimo kodas
text = "jump(50)"
numbers, text_without_numbers = separateNumbersText(text)

print(numbers[0])
print(text_without_numbers)