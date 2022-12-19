
# Application for determining college student ip values
# lets star
# variable hasil

def results():
      return result

# all variables
sin = []
str1=""

print('Application for determining college student ip values')

# menginputkan semester
semester = input('You are in semester : ')

print(f'Enter the value input in the semester {semester}')

# pengkondisian semester yang di pilih
match semester:
    case '1':
        Programing = int(input('Programming : '))
        Lab_work_in_programming = int(input('Lab work in Programming : '))
        Logic_for_Computer_Science = int(input('Logic for Computer Science : '))
        Elementary_Linear_Algebra = int(input('Elementary Linear Algebra : '))
        Calculus_1 = int(input('Calculus 1 : '))
        Basic_Chemistry_1 = int(input('Basic Chemistry 1 : '))
        Basic_Physics_1 = int(input('Basic Physics 1 : '))
        Scientific_Writing_and_Ethics = int(input('Scientific Writing and Ethics : '))
        Religion = int(input('Religion : '))

        result = '1'
        sm1= ['Programming\t\t\t\t\t','Lab work in Programming\t\t','Logic for Computer Scienc\t\t','Logic for Computer Scienc\t\t','Calculus 1\t\t\t\t\t','Basic Chemistry 1\t\t\t\t','Basic Physics 1\t\t\t\t','Scientific Writing and Ethics\t','Religion\t\t\t\t\t\t']
        sks = [2,4,2,3,2,1,3,4,2]


        if Programing & Lab_work_in_programming & Logic_for_Computer_Science & Elementary_Linear_Algebra & Calculus_1 & Basic_Chemistry_1 & Basic_Physics_1 & Scientific_Writing_and_Ethics & Religion:
             if  Programing > 90:

                 Programing = 4



        grade = [Programing,Lab_work_in_programming,Logic_for_Computer_Science,Elementary_Linear_Algebra,Calculus_1,Basic_Chemistry_1,Basic_Physics_1,Scientific_Writing_and_Ethics,Religion]

    case '2':
        Programing = input('Algorithms and Data Structures : ')
        English = input('English : ')
        Integral_and_Differential_Equations = input('Integral and Differential Equations : ')
        Discrete_Mathematics = input('Discrete Mathematics : ')
        Organization_and_Computer_Architecture = input('Organization and Computer Architecture : ')
        Introduction_to_Statistics = input('Introduction to Statistics : ')
        Lab_work_in_Algorithms_and_Data_Structures = input('Lab work in Algorithms and Data Structures : ')
        Digital_Systems = input('Digital Systems : ')
        Pancasila = input('Pancasila : ')

        result = '2'

    case '3':
        Analysis_of_Algorithm_and_Complexity = input('Analysis of Algorithm and Complexity : ')
        Database = input('Database : ')
        Computer_Network = input('Computer Network : ')
        Artificial_Intelligence = input('Artificial Intelligence : ')
        Database_Lab_work = input('Database Lab work : ')
        Computer_System_and_Network_Lab_work = input('Computer System and Network Lab work : ')
        Probability_and_Stochastic_Processes = input('Probability and Stochastic Processes : ')
        Operating_Systems = input('Operating Systems : ')
        Citizenship = input('Citizenship : ')

        result = '3'
    case '4':
        Philosophy_of_Computer_Science = input('Philosophy of Computer Science : ')
        Startup_Digital_Development = input('Startup Digital Development : ')
        Software_Engineering_Methods = input('Software Engineering Methods : ')
        Workshop_on_Implementing_Software_Design = input('Workshop on Implementing Software Design : ')
        Machine_Learning = input('Machine Learning : ')
        Languages_dan_Automata = input('Languages dan Automata : ')
        Numerical_Methods = input('Numerical Methods : ')
        Cryptography_and_Network_Security = input('Cryptography and Network Security : ')
        Elective_Courses_MBKM = input('Elective Courses / MBKM : ')

        result = '4'
    case '5':
        Seminar_Class = input('Seminar Class : ')
        Research_Method_of_Computer_Science = input('Research Method of Computer Science : ')
        Deep_Learning = input('Deep Learning : ')
        Software_Engineering_Project = input('Software Engineering Project : ')
        Elective_Courses_MBKM = input('Elective Courses / MBKM : ')

        result = '5'
    case '6':
        Community_Service_Program = input('Community Service Program : ')
        Elective_Courses_MBKM = input('Elective Courses / MBKM : ')

        result = '6'
    case '7':
        Undergraduate_Thesis_Proposal = input('Undergraduate Thesis Proposal : ')
        Elective_Courses_MBKM = input('Elective Courses / MBKM : ')

        result = '7'
    case '8':
        Undergraduate_Thesis = input('Undergraduate Thesis : ')

        result = '8'

    case _:
        print('NOT YET')


print('The result of determining the ip value')

# Menentukan grade nilai mahasiswa





match results():
    case '1':
        print('|---------------------------- semester 1 ---------------------------------|')
        print('| Courses \t\t\t\t\t\t | SKS \t | Score |')

        # Len  = len(sm1)
        #
        # for i in range(Len):
        #
        #
        #     print(f'| {sm1[i]} | {sks[i]} \t| ')

        # if grade[1] > 80:
        #     grade[1] = 4


        for i in  range(len(sm1)):
            sin = [str(sm1[i]),sks[i],grade[i]]

            print(f'| {sm1[i]} | {sks[i]} \t| {grade[i]}')



