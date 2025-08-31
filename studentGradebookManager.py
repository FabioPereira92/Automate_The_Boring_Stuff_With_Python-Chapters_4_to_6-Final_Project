# This program is a Student Gradebook Manager that let's the user add and remove students
# add and remove grades to a student, check student average and respective global grade
# check class average grade and check the student list.

print('\nSTUDENT GRADEBOOK MANAGER\n')

import sys
gradebook = {}

while True:
    
    print('Main menu'.center(23))
    print('''\n1. Add student
2. Remove student
3. Add grade to student
4. Remove grade from student
5. Show student average
6. Show class average
7. List all students
8. Exit\n''')
    
    action = input()
    
    if action == '1' or action == '1.' or action == '1. Add student':
        while True:
            print('Enter student name:')
            student = input().title() #Making student name case insensitive
            gradebook.setdefault(student, []) #Adding student

            #Code to return to the Main menu
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
            
    elif action == '2' or action == '2.' or action == '2. Remove student':
        while True:
            print('Enter student name:')
            student = input().title() #Making student name case insensitive
            try:
                del gradebook[student] #Removing student
            except KeyError:
                print("There isn't any " + student + " in the gradebook!")

            #Code to return to the Main menu
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
                   
    elif action == '3' or action == '3.' or action == '3. Add grade to student':
        while True:
            print('Enter student name:')
            student = input().title() #Making student name case insensitive
            gradebook.setdefault(student, [])
            while True:
                print('Enter grade:')
                try:
                    grade = int(input())
                    if grade < 0 or grade > 100: #Grade input validation
                        print('Only grades between 0 and 100 are allowed!')
                        continue
                    break
                except ValueError: #Grade input validation
                    print('Grade must be an integer!')
                    continue
                
            gradebook[student].append(grade) #Adding grade to student

            #Code to return to the Main menu
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
            
    elif action == '4' or action == '4.' or action == '4. Remove grade from student':
        while True:
            print('Enter student name:')
            student = input().title() #Making student name case insensitive
            while True:
                print('Enter grade:')
                try:
                    grade = int(input())
                    if grade < 0 or grade > 100: #Grade input validation
                        print('Only grades between 0 and 100 are allowed!')
                        continue
                    break
                except ValueError: #Grade input validation
                    print('Grade must be an integer!')
                    continue

            try:
                gradebook[student].remove(grade) #Removing grade from student
            except KeyError:
                print("There isn't any " + student + " in the gradebook!")
            except ValueError:
                print(student + " doesn't have that grade!")

            #Code to return to the Main menu    
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
        
    elif action == '5' or action == '5.' or action == '5. Show student average':
        while True:
            print('Enter student name:')
            student = input().title() #Making student name case insensitive
            gradebook.setdefault(student, [])
            s = 0
            for v in gradebook[student]:
                s = s + v #Summing all grades of the student
            try:
                average = s/len(gradebook[student]) #Calculating the average
                #Attributing grades based on the average
                if average > 80 and average <= 100:
                    grade = 'A'
                elif average > 60 and average <= 80:
                    grade = 'B'
                elif average > 40 and average <= 60:
                    grade = 'C'
                elif average > 20 and average <= 40:
                    grade = 'D'
                else:
                    grade = 'E'
                print(student + "'s average: " + str(average))
                print('Grade: ' + grade)
            except ZeroDivisionError:
                print(student + " doesn't have any grades in the Gradebook yet!")

            #Code to return to the Main menu          
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break

    elif action == '6' or action == '6.' or action == '6. Show class average':
        while True:
            s = 0
            length = 0
            for k, v in gradebook.items():
                for i in v:
                    s = s + i #Summing all students grades
                length = length + len(v) #Finding the total number of grades
            try:
                classAverage = s/length #Calculating class average
                print('Class average: ' + str(classAverage))
            except ZeroDivisionError:
                print("The Gradebook doesn't have any grades yet!")

            #Code to return to the Main menu
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
        
    elif action == '7' or action == '7.' or action == '7. List all students':
        while True:
            students = list(gradebook.keys())
            students.sort() #Sorting students alphabetically
            for i in students:
                print(i)

            #Code to return to the Main menu
            print("Press 'r' to return to Main menu or anything else to continue:")
            decision = input()
            if decision == 'r' or decision == 'R':
                break
            
    #Code to close the program        
    elif action == '8' or action == '8.' or action == '8. Exit':
        print('Goodbye!')
        sys.exit()

    #Menu item validation    
    else:
        print('Enter a valid menu item\n') 
