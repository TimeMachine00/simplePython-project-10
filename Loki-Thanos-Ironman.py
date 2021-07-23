import random

print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("check you are loki or thanos or the Iron man at the end ; welcome to Loki-thanos-iron man")

n = int(input("enter your favourite two digit number"))
for i in range(1, n+1):
# for i in random.randint([1,n]):
    if i % 3 == 0 and i % 5 == 0:
        print("I am The Iron man")

    elif i % 3 == 0:
        print("I am the Loki")

    elif i % 5 == 0:
        print('I am the Thanos')
    else:
        print(i)

print()
but1 = print(input("press enter for bye"))