# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_for_loops.asp

# IIT Student ID: 20220260
# UoW ID: w1953182 / 19531829
# Date:  11.11.2022

# Declaring variables
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
progression_outcome = 0


# Part 1
# To check range and integer
def creditChecker(output):
    while True:
        try:
            credit = int(input(output))
            if credit not in range(0, 121, 20):
                print("Out of range\n")
                continue
        except ValueError:
            print("Integer required\n")
            continue
        break
    return credit


# Deciding the progression outcome
def studentValidation():
    while True:
        pass_credits = creditChecker("Please enter your credits at pass: ")
        defer_credits = creditChecker("Please enter your credits at defer: ")
        fail_credits = creditChecker("Please enter your credits at fail: ")
        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect\n")
            continue
        break
    if pass_credits == 120:
        progression_outcome = "Progress\n"

    elif pass_credits == 100:
        progression_outcome = "Progress (module trailer)\n"

    elif fail_credits == 80 or fail_credits == 100 or fail_credits == 120:
        progression_outcome = "Exclude\n"

    else:
        progression_outcome = "Do not Progress-module retriever\n"
    print(progression_outcome)


# Deciding the progression outcome
def staffValidation():
    global progress, module_trailer, module_retriever, exclude, progression_outcome

    while True:
        pass_credits = creditChecker("Enter your total PASS credits: ")
        defer_credits = creditChecker("Enter your total DEFER credits: ")
        fail_credits = creditChecker("Enter your total FAIL credits: ")
        if pass_credits + defer_credits + fail_credits != 120:
            print("Total incorrect\n")
            continue
        break
    if pass_credits == 120:
        progression_outcome = "Progress"
        progress += 1

    elif pass_credits == 100:
        progression_outcome = "Progress (module trailer)"
        module_trailer += 1

    elif fail_credits == 100 or fail_credits == 80 or fail_credits == 120:
        progression_outcome = "Exclude"
        exclude += 1

    else:
        progression_outcome = "Module retriever"
        module_retriever += 1

    print(progression_outcome)


def histogram(progression, progression_count):
    print(f"{progression} {progression_count}", ":", "*" * progression_count)


# To quite staff or enter another data
def staffOption():
    option = input("\nWould you like to enter another set of data?\n"
                   "Enter 'y' for yes or 'q' to quit and view results: ")
    if option.lower() == 'y':
        print("")
        staffStart()

    elif option.lower() == 'q':
        print("")
        print('-' * 65)
        print("Histogram\n")
        histogram("Progress ", progress)
        histogram("Trailer  ", module_trailer)
        histogram("Retriever", module_retriever)
        histogram("Excluded ", exclude)
        print("")
        print(f"{progress + module_trailer + module_retriever + exclude}"" outcomes in total.")
        print("-" * 65)

    else:
        print("Invalid Input")
        staffOption()


# Beginning of the Staff version
def staffStart():
    while True:
        staffValidation()
        staffOption()
        break


# Beginning of the program
def main():
    while True:
        user = input("Enter '1' to open student version\n"
                     "Enter '2' to open staff version\n"
                     "Enter '3' to quit program\n"
                     "Enter your option: ")
        # For Student version
        if user == '1':
            print("-" * 65)
            print("Student Version\n")
            studentValidation()

        # For stuff version
        elif user == "2":
            print("-" * 65)
            print("staff version with histogram\n")
            staffStart()

        # To quit the whole program
        elif user == "3":
            break

        else:
            print("Invalid input\n")


# Beginning of the program
main()
