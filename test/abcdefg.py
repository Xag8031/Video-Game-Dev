points = []
with open("points.txt","r", encoding="utf-8") as file_data:
    points.append(file_data.read().split("\n"))
print(points)