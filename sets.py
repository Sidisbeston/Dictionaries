'''
A = {99, 76, 50, 43, 21, 11}
B = {12, 34, 82, 1, 99, 50}

A.add(100)
A.remove(99)
A.discard(500)
print(A)
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
'''

alphabets = set("qwertyuiopasdfghjklzxcvbnm")
count = 0
sent = input("Enter a sentence: ")
pangram = set(sent)
if pangram.issubset(alphabets):
  print("It is a pangram")
else:
  print("It is not a pangram")
