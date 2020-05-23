
# try:
#     f = open("data/logs.txt", encoding="CP1251")
#     print(f.read())
#     1/0
# except:
#     1/0
# finally:
#     print("Zamykam plik")
#     f.close()

# with open("data/logs.txt") as f:
#     with open("data/pan_tadeusz.txt") as pan_t:
#         print(len(pan_t.read()))
#     print(f.read())

# with open("xxx.txt", "w") as f:
#     f.write("Ala ma kota.\n kot ma Alę\n asas\n")

with open("xxx.txt") as infile:
    #przygorowanie danychg
    out = []
    for line in infile:
        out.append(line.upper())

with open("xxx2.txt", "w") as outfile:
    outfile.write("\n".join(out))
