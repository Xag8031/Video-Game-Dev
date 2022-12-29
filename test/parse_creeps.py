txt = []
with open("code.creeps", "r") as f:
    for line in f:
        if line.startswith(";"):
            print("Comment")
            
        else:
            print("Code")
            line = line.replace("\n", "")
            txt.append(line)
for pronter in txt:
    print(pronter)