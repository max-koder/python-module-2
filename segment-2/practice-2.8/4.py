text = input()

data = set()
word = ""
for i in range (len(text)):
    if text[i] != " ":
        word += text[i]
    else:
        data.add(word)
        word = ""
data.add(word)
word = ""

print(len(data))