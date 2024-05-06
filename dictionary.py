sports = {
  "cricket": 11,
  "football": 11,
  "tennis": 4,
  "basketball": 5
}


sports["tennis"] = 2
sports["badminton"] = 4
del[sports["football"]]
print(sports)
if "baseball" in sports:
  print("yes")
else:
  print("no")

if 10 in sports.values():
  print("yes")
else:
  print("no")

for i in sports.values():
  print(i)