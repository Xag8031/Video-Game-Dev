data = [14, 47, 15, 47, 15, 47, 47, 47, 15, 47, 47, 47, 47, 47, 15, 47, 47, 47, 47, 47,
        14, 47, 15, 47, 15, 47, 4, 47, 38, 35, 35, 35, 8, 47, 15, 47, 5, 35, 36, 47,
        14, 47, 15, 47, 15, 47, 15, 47, 47, 47, 47, 47, 15, 47, 15, 47, 15, 47, 47, 47,
        14, 47, 49, 35, 41, 47, 49, 35, 8, 47, 4, 47, 38, 9, 41, 47, 49, 35, 8, 47,
        14, 47, 15, 47, 47, 47, 15, 47, 15, 47, 15, 47, 47, 15, 47, 47, 15, 47, 15, 47,
        14, 47, 38, 35, 35, 35, 41, 47, 15, 47, 38, 35, 9, 42, 35, 35, 41, 47, 38, 35,
        14, 47, 47, 47, 47, 47, 47, 47, 15, 47, 47, 47, 15, 47, 47, 47, 47, 47, 47, 47,
        50, 35, 35, 35, 35, 35, 35, 47, 38, 35, 8, 47, 15, 47, 5, 35, 35, 35, 8, 47,
        14, 47, 47, 47, 47, 47, 47, 47, 47, 47, 15, 47, 15, 47, 15, 47, 47, 47, 15, 47,
        24, 35, 35, 35, 3, 47, 5, 35, 8, 47, 15, 47, 49, 35, 41, 47, 4, 47, 15, 47,
        47, 47, 47, 47, 14, 47, 15, 47, 15, 47, 15, 47, 15, 47, 47, 47, 15, 47, 15, 47,
        6, 35, 35, 35, 25, 47, 15, 47, 38, 35, 41, 47, 15, 47, 34, 35, 42, 35, 42, 35,
        14, 47, 47, 47, 47, 47, 15, 47, 47, 47, 47, 47, 15, 47, 47, 47, 47, 47, 47, 47,
        50, 35, 35, 35, 35, 35, 41, 47, 5, 35, 35, 35, 42, 35, 8, 47, 5, 35, 35, 35,
        14, 47, 47, 47, 47, 47, 47, 47, 15, 47, 47, 47, 47, 47, 15, 47, 15, 47, 47, 47,
        14, 47, 5, 35, 8, 47, 1, 35, 25, 47, 5, 35, 8, 47, 49, 35, 41, 47, 5, 35,
        14, 47, 15, 47, 15, 47, 15, 47, 47, 47, 15, 47, 15, 47, 15, 47, 47, 47, 15, 47,
        39, 35, 41, 47, 15, 47, 26, 47, 5, 35, 41, 47, 15, 47, 26, 47, 5, 35, 41, 47,
        47, 47, 47, 47, 15, 47, 47, 47, 15, 47, 47, 47, 15, 47, 47, 47, 15, 47, 47, 47,
        2, 2, 2, 2, 31, 2, 2, 2, 30, 47, 1, 2, 31, 2, 2, 2, 31, 2, 2, 2]
map = []
for i in data:
    if i != 47:
        map.append(0)
    else:
        map.append(1)
print(map)
map = [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
       0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1,
       0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
       0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1,
       0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 
       0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
       0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 
       0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1,
       1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
       0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1,
       0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
       0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1,
       0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 
       1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
