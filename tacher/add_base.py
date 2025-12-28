i = 1
with open(r"Эвристика_class.list", "a") as file:
    while 1:
        i = i + 1
        file.write(str("0") + '\n')
        if i == 40152:
            break

print("done")