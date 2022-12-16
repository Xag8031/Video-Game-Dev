open_file = open("./code.creeps", "r")
txt = open_file.read()
txt = txt.split("\n")
for line in txt:
    if line.startswith(";"):
        print("Comment")
        txt.remove(line)
    else:
        print("Code")
for pronter in txt:
    print(pronter)