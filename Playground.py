file = open("out.txt", "w")
s = "this"
print(s, "is a test", file=file)
file.close()