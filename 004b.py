curr_year = 2020

first_name = input("Podaj imie: ")
last_name = input("Podaj nazwisko: ")
b_year = int(input("Podaj rok urodzenia: "))
profession = input("Podaj zawód: ")

# b_year = int(b_year)
age = curr_year - b_year

result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}
=============================
rok urodzenia:      {b_year}
zawód:              {profession.lower()}
emerytura możliwa? 
"""

print(result)