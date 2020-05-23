import sys

try:
    f_in_path = sys.argv[1]
    out_f_path = sys.argv[2]
except IndexError:
    f_in_path = "data/emails.txt"
    out_f_path = "output/cleaned_emails.txt"


emails = set()
with open(f_in_path) as f:
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            emails.add(line)

with open(out_f_path, "w") as f:
    for email in sorted(emails):
        f.write(email + "\n")
