from time import sleep

print("-----------Grade Calculator------------")
print("                                  ")
print("                                  ")
print("----------------------------------------------------")
print("Core Subjects: \nMath\nScience\nL.A\nGeography")
print("---                                                    ")
print("Electives: \nEverything else")
print("----------------------------------------------------")
print("Note: There should be only 10 when the number of core are added. (Per Semester)")
print("----------------------------------------------------")
print("Note: Order of subjects you put in doesn't matter, just put all of them.")
print("----------------------------------------------------")
print(" ")
print(" ")
print("Loading...")
print(" ")
print(" ")
sleep(5)


def calculation(grade):
    grade = int(grade)
    grade = float(grade)

    if grade >= 93:
        calculation.grade = 4.0

    elif grade >= 90:
        calculation.grade = 3.7

    elif grade >= 87:
        calculation.grade = 3.3

    elif grade >= 83:
        calculation.grade = 3.0

    elif grade >= 80:
        calculation.grade = 2.7

    elif grade >= 77:
        calculation.grade = 2.3

    elif grade >= 73:
        calculation.grade = 2.0

    elif grade >= 70:
        calculation.grade = 1.7

    elif grade >= 67:
        calculation.grade = 1.3

    elif grade >= 63:
        calculation.grade = 1.0

    elif grade >= 60:
        calculation.grade = 0.7

    else:
        calculation.grade = 0


core_sub1 = input(
    "Put in your grade of core subject number one. (Don't put the percentage sign.)\nCore #1: "
)

calculation(core_sub1)

core_sub1 = calculation.grade

print("----------------------------------------------")
print("           ")
core_sub2 = input(
    "Put in your grade of core subject number two. (Don't put the percentage sign.)\nCore #2: "
)

calculation(core_sub2)

core_sub2 = calculation.grade
print("----------------------------------------------")
print("           ")
core_sub3 = input(
    "Put in your grade of core subject number three. (Don't put the percentage sign.)\nCore #3: "
)

calculation(core_sub3)

core_sub3 = calculation.grade
print("----------------------------------------------")
print("           ")
core_sub4 = input(
    "Put in your grade of core subject number four. (Don't put the percentage sign.)\nCore #4: "
)

calculation(core_sub4)

core_sub4 = calculation.grade


print("----------------------------------------------")
print("           ")
print("Next part are the ELECTIVES.")
print("           ")
print("           ")

elect1 = input(
    "Put in your grade of elective subject number one. (Don't put the percentage sign.)\nElective #1: "
)

calculation(elect1)

elect1 = calculation.grade
print("----------------------------------------------")
print("           ")

elect2 = input(
    "Put in your grade of elective subject number two. (Don't put the percentage sign.)\nElective #2: "
)

calculation(elect2)

elect2 = calculation.grade
print("----------------------------------------------")
print("           ")

elect3 = input(
    "Put in your grade of elective subject number three. (Don't put the percentage sign.)\nElective #3: "
)

calculation(elect3)

elect3 = calculation.grade
print("----------------------------------------------")
print("           ")

elect4 = input(
    "Put in your grade of elective subject number four. (Don't put the percentage sign.)\nElective #4: "
)

calculation(elect4)

elect4 = calculation.grade
print("----------------------------------------------")
print("           ")

elect5 = input(
    "Put in your grade of elective subject number five. (Don't put the percentage sign.)\nElective #5: "
)

calculation(elect5)

elect5 = calculation.grade
print("----------------------------------------------")
print("           ")

elect6 = input(
    "Put in your grade of elective subject number six. (Don't put the percentage sign.)\nElective #6: "
)

calculation(elect6)

elect6 = calculation.grade
print("----------------------------------------------")
print("           ")
print("           ")
print("           ")
print("||||||||||||||||||||||||||||||||||||||||||||||||")
final_core = (core_sub1 + core_sub2 + core_sub3 + core_sub4) * 0.5
final_elect = (elect1 + elect2 + elect3 + elect4 + elect5 + elect6) * 0.25
final_grade = (final_core + final_elect) / 3.5
print("                                                ")
print("Your grade is\n")
print(final_grade)
print("                                                ")
print("||||||||||||||||||||||||||||||||||||||||||||||||")
print("           ")
print("           ")
print("           ")
print("Hope you have a great day!")
