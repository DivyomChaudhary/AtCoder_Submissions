old_str = input("")
flagged = "QWERTYUIOPSDFGHJKLZXCVBNM"
new_str = ""
for s in old_str:
    if s in flagged:
        new_str += "."
    else:
        new_str += s
print(new_str)