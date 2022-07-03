import re
line = "MAIL FROM: <alice@crepes.fr>"
match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
print(match.group(0))