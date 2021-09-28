file = open("scores.csv", "r")
data = []
for line in file:
  line = line.strip()
  data.append(line)
file.close()
x = 1
low = data[1]
high = data[1]
while x < len(data):
  if int(data[x]) < int(low):
    low = data[x]
  elif int(data[x]) > int(high):
    high = data[x]
  x = x + 1
print(f"The lowest score is {low}")
print(f"The highest score is {high}")