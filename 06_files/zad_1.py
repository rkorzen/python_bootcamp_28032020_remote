import sys

print(sys.argv)
f_name = sys.argv[1]
print("Bedę pracować z plikiem: ", f_name)

# 1. utworzenie pliku z zawartoscia:
# with open("test.txt", 'w') as f:
#     f.write("To jest pierwsza linia\n")
#     f.write("Druga linia\n")
#     f.write("trzecia linia\n")

# odczytaj i ponumeruj linie:

with open(f_name) as f:
    text = f.read()
    text = text.splitlines()
    for i, line in enumerate(text, start=1):
        print(f"{i}: {line}")
