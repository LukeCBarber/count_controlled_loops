print("GRADEBOOK PROGRAM")
print()

valid_input = False
while valid_input == False:
    total_class = int(input("How many students are in your class? "))
    if total_class < 0:
        print("Invalid number of students; please try again.")
        valid_input = False
    else:
        print()
        valid_input = True
        
    
valid_input = False
while valid_input == False:
    total_tests = int(input("How many tests in this class? "))
    if total_tests < 0:
        print("Invalid number of tests; please try again.")
        valid_input = False
    else:
        print()
        valid_input = True
        
print("ok, let's begin . . .")
print()


student = 0
test = 0
score = 0
total_score_avg = 0
total_avg= 0
for student in range(total_class):
    student +=1
    print("- Student",student,"-")
    total_score = 0
    for test in range(total_tests):
        test+=1
        valid_input = False
        while valid_input == False:
            question = "Enter a score for test " + str(test) +":"
            score = int(input(question))
            if score > 0:
                test+=1
                total_score += score
                valid_input = True
            else:
                print("Invalid score, please try again.")
                valid_input = False
    avg_score = format(total_score/total_tests, ",.2f")
    total_avg += total_score/total_tests
    print("Average score for student ", student,": ",avg_score, sep='')
    print()
total_score_avg = format(total_avg/total_class,",.2f")
print()
print("The average score for all students is",total_score_avg)
    
