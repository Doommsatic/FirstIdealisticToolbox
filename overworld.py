with open("map.txt") as file:
  area=file.read()
for character in range(len(area)):
  print(area[character])