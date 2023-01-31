#Gonna use random to generate the computers answers
import random


def get_reversed_dictionary(word):
    dic_choices = {
        "Rock" : 1,
        "Paper" : 2,
        "Scissors" : 3
    }
    return dic_choices[word]


def get_dictionary(num):
    dic_choices = {
        1 : "Rock",
        2 : "Paper",
        3 : "Scissors"
    }
    return dic_choices[num]


def get_cpu_choice():
    random_number = random.randint(1,3)
    return random_number


def get_user_input():
    try:
        their_answer = int(input("Pick an option: "))
    except ValueError:
        print("Please enter a number(1/2/3) not a letter")
        return get_user_input()
    if their_answer not in [1,2,3]:
        print("Please enter a valid choice, no other numbers will be accepted")
        return get_user_input()
    return their_answer


def decide_winner(cpu_choice, human_choice):
    cpu_num = get_reversed_dictionary(cpu_choice)
    human_answer = get_reversed_dictionary(human_choice)
    match cpu_choice:
        case 1:
            if human_choice == 2:
                return "You lost, unlucky fam"
            elif human_choice == 1:
                return "It's a tie, gg"
            else:
                return "You lucky boy, you won, gg"
        case 2:
            if human_choice == 3:
                return "You lost, unlucky fam"
            if human_choice == 2:
                return "It's a tie, gg"
            else:
                return "You lucky boy, you won, gg"
        case 3:
            if human_choice == 1:
                return "You lost, unlucky fam"
            if human_choice == 3:
                return "It's a tie, gg"
            else:
                return "You lucky boy, you won, gg"


def has_next():
    checker = input("Do you wanna play again(y/n): ").lower()
    if checker not in ['y', 'n']:
        print('Please enter valid input')
        return has_next()
    if checker == 'y':
        return True
    else:
        return False


def main():
    usr_input = get_dictionary(get_user_input())
    cpu_choice = get_dictionary(get_cpu_choice())
    get_winner = decide_winner(cpu_choice, usr_input)


if __name__ == "__main__":
    main()
    while has_next():
        main()
