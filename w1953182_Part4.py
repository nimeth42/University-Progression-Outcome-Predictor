# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_for_loops.asp

# IIT Student ID: 20220260
# UoW ID: w1953182   / 19531829
# Date:  11.11.2022

# Declaring variables
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
# part 2 List variable
add_list = []
# Part 3 Text file
report_path = "Textfile.txt"
# Part 4 Dictionary variable
add_dict = {}
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
    global progress, module_trailer, module_retriever, exclude, add_list, progression_outcome, add_dict

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

    # Part 2 adding to a list
    add_list.append([progression_outcome, pass_credits, defer_credits, fail_credits])

    # Part 3 Giving details to text file
    text_file = open(report_path, "a")
    text_file.write(f"{progression_outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n")
    text_file.close()

    add_dict[id_number] = progression_outcome, pass_credits, defer_credits, fail_credits


def histogram(progression, progression_count):
    print(f"{progression} {progression_count}", ":", "*" * progression_count)


# To quite staff or to enter  another data
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

        # Part 2 Continue adding content to the list
        print("Progression Outcome List\n")
        for extension in add_list:
            list = (f"{extension[0]} - {extension[1]}, {extension[2]}, {extension[3]}")
            print(list)
        print("-" * 65)

        # Part 3 Displaying content of text file
        print("Text file read\n")
        text_file = open(report_path, "r")
        print(text_file.read())
        print("-" * 65)

        # Part 4
        print("Progression outcome with Dictionary")
        for key in add_dict.keys():
            outcome_dict = add_dict[key]
            print(f"{key} : {outcome_dict[0]} - {outcome_dict[1]}, {outcome_dict[2]}, {outcome_dict[3]}")
        print('-' * 65)

    else:
        print("Invalid Input")
        staffOption()


# Beginning of the Staff version
def staffStart():
    while True:
        idCheck()
        staffValidation()
        staffOption()
        break


def idCheck():
    global id_number
    id_number = str(input("Enter student Id Number: "))
    lenth = len(id_number)
    if lenth != 8:
        print("Enter a valid Id Number")
        idCheck()


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
            # Part 3
            text_file = open(report_path, "w")
            text_file.close()

            print("-" * 65)
            print("Staff version with histogram\n")
            # Part 4 checking the ID
            staffStart()

        # To quit the whole program
        elif user == "3":
            break

        else:
            print("Invalid input\n")


# Beginning of the program
main()
