chosen_num = 10
guess_num = int(input("inform a number between 1 and 20: "))

while guess_num != chosen_num:
    print("wrong! try again.")

    guess_num = int(input("inform a number between 1 and 20: "))
    print("correct number, congratulations!")

counter = 0

while counter < 5:
    print(counter)
    counter = counter + 1
