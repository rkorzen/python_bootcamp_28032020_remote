text = "HELLO STRANGER!"

i = 1
first = []
second = []
#text = text.replace(" ", "")
for letter in text:
    if i % 2 == 0:
        second.append(letter)
    else:
        first.append(letter)
    i += 1

if " " in first:
    first.remove(" ")
if " " in second:
    second.remove(" ")

first_text = " ".join(first)
second_text = " ".join(second)

print(first_text)
print(second_text)

assert first_text == "H L O S R N E !"
assert second_text == "E L T A G R"
