result = None
sin = []
str1=""

print('Application for determining college student ip values')

# Enter semester
semester = input('You are in semester : ')

print(f'Enter the value input in the semester {semester}')

# selected semester conditioning
match semester:
    case '1':
        subjects = ["Programing", "Lab_work_in_programming", "Logic_for_Computer_Science", "Elementary_Linear_Algebra",
                    "Calculus_1", "Basic_Chemistry_1", "Basic_Physics_1", "Scientific_Writing_and_Ethics", "Religion"]

        # Loop through each subject to read input values and create variables with the same name as the subject
        for subject in subjects:
            grade = int(input(f"{subject} grade: "))
            sks = int(input(f"{subject} sks: "))

            # Create a variable with the same name as the subject
            globals()[subject] = grade
            globals()[f"Sks{subject}"] = sks

        result = '1'
        sm1 = ['Programming\t\t\t\t\t', 'Lab work in Programming\t\t', 'Logic for Computer Scienc\t\t',
               'Logic for Computer Scienc\t\t', 'Calculus 1\t\t\t\t\t', 'Basic Chemistry 1\t\t\t\t', 'Basic Physics 1\t\t\t\t',
               'Scientific Writing and Ethics\t', 'Religion\t\t\t\t\t\t']


        def convert_to_gpa(score):
            if score >= 90:
                return 4.0
            elif score >= 85:
                return 3.75
            elif score >= 80:
                return 3.5
            elif score >= 75:
                return 3.25
            elif score >= 70:
                return 3.0
            elif score >= 65:
                return 2.75
            elif score >= 60:
                return 2.5
            elif score >= 55:
                return 2.25
            elif score >= 50:
                return 2.0
            elif score >= 45:
                return 1.75
            elif score >= 40:
                return 1.5
            elif score >= 35:
                return 1.25
            elif score >= 30:
                return 1.0
            else:
                return 0.0

            # Convert the grades


        Programing = convert_to_gpa(Programing)
        Lab_work_in_programming = convert_to_gpa(Lab_work_in_programming)
        Logic_for_Computer_Science = convert_to_gpa(Logic_for_Computer_Science)
        Elementary_Linear_Algebra = convert_to_gpa(Elementary_Linear_Algebra)
        Calculus_1 = convert_to_gpa(Calculus_1)
        Basic_Chemistry_1 = convert_to_gpa(Basic_Chemistry_1)
        Basic_Physics_1 = convert_to_gpa(Basic_Physics_1)
        Scientific_Writing_and_Ethics = convert_to_gpa(Scientific_Writing_and_Ethics)
        Religion = convert_to_gpa(Religion)

        grade = [Programing, Lab_work_in_programming, Logic_for_Computer_Science, Elementary_Linear_Algebra, Calculus_1,
                 Basic_Chemistry_1, Basic_Physics_1, Scientific_Writing_and_Ethics, Religion]
        sks = [SksPrograming, SksLab_work_in_programming, SksLogic_for_Computer_Science, SksElementary_Linear_Algebra,
               SksCalculus_1, SksBasic_Chemistry_1, SksBasic_Physics_1, SksScientific_Writing_and_Ethics, SksReligion]
        AllcountScoreandSks = 0
        countSks = 0

        # Iterate over the grades and credits
        for i in range(len(grade)):
            AllcountScoreandSks += grade[i] * sks[i]
            countSks += sks[i]

        # Calculate the GPA
        ip = AllcountScoreandSks / countSks

print('The result of determining the ip value')

match result:
    case '1':
        print('|------------------ semester 1 -----------------|')
        print('| Courses \t\t\t\t\t\t | SKS \t| Score |')




        for i in  range(len(sm1)):
            sin = [str(sm1[i]),sks[i],grade[i]]

            print(f'| {sm1[i]} | {sks[i]}\t| {grade[i]} \t|')

        print('|-----------------------------------------------|')
        print(f'Congrats Your IP is {ip}')
