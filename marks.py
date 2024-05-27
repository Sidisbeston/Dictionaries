import random

marks = []
low_marks = []
med_marks = []
high_marks = []
for x in range(20):
  marks.append(random.randint(0, 100))

for x in marks:
  if x <= 30:
    low_marks.append(low_marks)
  if x > 30 and x <= 69:
    med_marks.append(x)
  if x >= 70:
    high_marks.append(x)
  

print(low_marks)
print(med_marks)
print(high_marks)