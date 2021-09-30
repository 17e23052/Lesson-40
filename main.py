print("Enter a player name:")
name = input()
file = open("players.csv", "r")
data = []
for line in file:
  line = line.strip()
  line = line.split(",")
  data.append(line)
x = 0
score = 0
while x < len(data):
  if data[x][0] == name:
    score = data[x][1]
  x = x + 1
if score == 0:
  print("No value")
else:
  print(f"The last score from {name} was {score}")
file.close()