done = []

# Read the file, skip lines that start with a semicolon, and parse the commands
with open("code.creeps","r", encoding="utf-8") as file_data:
    for line in file_data:
        if line[0] != ";":
            command = line.strip()
            parts = command.split('(')
            name = parts[0]
            argument = parts[1][:-1]
            done.append([name, argument])
    
print(done)
