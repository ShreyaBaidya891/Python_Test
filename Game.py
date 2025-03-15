import random

# choices : list[int] = [random.randint(0,10) for _ in range(5)]
choices : list[int] = [[] for _ in range(5)]
for i in range(5):
    randm_num = random.randint(0,10)
    choices[i].append(randm_num)
score = 0

input_arr : list[int] = []
for i in range(5):
    guess_num = int(input("Enter a number : "))
    input_arr.append(guess_num)
    if choices[i] == guess_num:
        score += 10
    else:
        print("Try again !!")

print(f"Your final score is {score}")
print(input_arr)

