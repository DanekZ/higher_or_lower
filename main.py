from utilities import get_personal_data,display_person,checking_choice, check_answer
from art import logo, vs, thanks


# prepare data
game_over = False
still_playing = True
compare_A = get_personal_data()
count_true = 0

#keep playing
while still_playing:
    #game over
    while not game_over:
        # get data B
        compare_B = get_personal_data()
        while compare_B == compare_A:
            compare_B = get_personal_data()

        # compare A
        print(logo)
        print(display_person(compare_A, "Compare A"))

        # compare B
        print(vs)
        print(display_person(compare_B, "Compare B"))

        while True:
            answer = input("Who has more followers? Type 'A' or 'B': ").upper()
            check = checking_choice(answer)
            if check:
                break
            else:
                print("Invalid input. Please input either 'A' or 'B'. value")


        is_true_answer = check_answer(answer, compare_A['follower_count'], compare_B['follower_count'])
        if is_true_answer:
            count_true += 1
            compare_A = compare_B
            print(f"you're right, your score now is {count_true}")
        else:
            game_over = True
            print("Wrong! Better luck next time!")

    print(f"game over, you score is {count_true}")
    while True:
        is_still_play = input("Want play again? y/n: ").lower()
        if is_still_play not in ["y","yes","n","no"]:
            print("Invalid input. Please input either 'y' or 'n'. value")
        else:
            if is_still_play in ["y", "yes"]:
                still_playing = True
                count_true = 0
                compare_A = get_personal_data()
                game_over = False
                break
            elif is_still_play in ["n", "no"]:
                still_playing = False
                break

print(thanks)