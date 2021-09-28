print("Enter the first letter of the name:")
letter = input().upper()
file = open("names.csv", "r")
data = []
for line in file:
  if line[0].upper() == letter:
    data.append(line)
x = 0
while x < len(data):
  print(data[x].strip())
  x = x + 1