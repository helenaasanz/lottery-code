import random

for k in range(7):
     print("Lotto Numbers: ", random.randint(1, 49))

answer = set()
sampleSize = 49
answerSize = 0

while answerSize < sampleSize:
    r = random.randint(0,49)
    if r not in answer:
        answerSize += 1
        answer.add(r)