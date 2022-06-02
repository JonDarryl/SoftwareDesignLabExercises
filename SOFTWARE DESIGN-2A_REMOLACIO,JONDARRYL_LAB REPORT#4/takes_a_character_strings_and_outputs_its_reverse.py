def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end='')

string = "desserts"
print(string)
reverse(string)

string1 = "diaper"
print("\n"+string1)
reverse(string1)
