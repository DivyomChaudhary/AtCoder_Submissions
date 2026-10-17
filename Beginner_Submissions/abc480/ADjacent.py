mat = []
for i in range(2):
    row = input("")
    mat.append(row)

answer = ""
for i in range(2):
    if (mat[0][i] == 'A' and mat[1][i] == 'D') or (mat[0][i] == 'D' and mat[1][i] == 'A') or (mat[i][0] == 'A' and mat[i][1] == 'D') or (mat[i][0] == 'D' and mat[i][1] == 'A'):
        answer = "Yes"
    else:
        if answer == "No" or answer == "":
            answer = "No"
        else:
            answer = "Yes"
print(answer)