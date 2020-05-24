import re

napis = "552-30312-345  123-34312-345 123-312-345 "

kod_pocztowy_pattern = re.compile("\d{2}-\d{3}")
data_pattern = re.compile("\d{2} \w{3} \d{4}")
email_pattern = re.compile("[\w\.\-]+@(?:\w+\.)+\w+")

with open("input.txt") as f:
    text = f.read()

print(kod_pocztowy_pattern.findall(text))
print(data_pattern.findall(text))
print(email_pattern.findall(text))
