'''
Author: Austin Huff
Implements Gale-Shapley algorithm based on
student and company preference lists to match
students and companies
'''

n = 9

studentsPref = [[8,7,9,4,5,6,3,2,1],
                [8,7,4,3,1,9,2,6,5],
                [8,4,7,2,3,6,5,1,9],
                [4,8,3,2,7,9,5,1,6],
                [8,7,3,4,9,5,6,1,2],
                [8,4,7,9,3,2,1,6,5],
                [8,6,4,7,3,2,5,9,1],
                [1,8,6,4,9,2,5,3,7],
                [9,8,4,2,1,5,3,7,6]]

studentsTaken = [False for i in range(0,n)]

companyPref = [[6,5,2,1,4,8,7,9,3],
               [6,8,3,7,4,2,5,9,1],
               [7,1,8,5,3,2,9,6,4],
               [4,7,8,5,1,6,2,9,3],
               [3,1,8,4,2,7,6,5,9],
               [5,1,7,9,4,8,6,2,3],
               [5,7,6,8,9,4,1,2,3],
               [5,9,4,3,8,6,7,2,1],
               [8,1,9,6,2,5,7,3,4]]

companyTaken = [False for i in range(0,n)]

matchList = [-1 for i in range(0,n)] #students are indecies, values are company
iterations = 0
while -1 in matchList:
    iterations += 1
    for i in range(0, n):
        if studentsTaken[i] == False:
            currentStudentIndex = i
            currentStudentName = i+1
            break
    #print(currentStudent)

    currentCompanyIndex = int(studentsPref[currentStudentIndex][0]) - 1
    currentCompanyName = int(studentsPref[currentStudentIndex][0])
    
    if companyTaken[currentCompanyIndex] == False:
        # company doesnt currently have a student
       matchList[currentStudentIndex] = currentCompanyName
       studentsPref[currentStudentIndex].remove(currentCompanyName)
       studentsTaken[currentStudentIndex] = True
       companyTaken[currentCompanyIndex] = True
    else:
        # desired company has someone already
        studentPrimeName = matchList.index(currentCompanyName) + 1
        studentPrimeIndex = matchList.index(currentCompanyName) 
        if companyPref[currentCompanyIndex].index(studentPrimeName) < companyPref[currentCompanyIndex].index(currentStudentName):
            # company prefers prime student
            # current student remains free & remove company from students list
            studentsPref[currentStudentIndex].remove(currentCompanyName)
        else:
            # company prefers new student
            # prime is free and current is matched
            matchList[studentPrimeIndex] = -1
            studentsTaken[studentPrimeIndex] = False
            #studentsPref[studentPrimeIndex].remove(currentCompanyName)
            matchList[currentStudentIndex] = currentCompanyName
            studentsTaken[currentStudentIndex] = True
            studentsPref[currentStudentIndex].remove(currentCompanyName)

names = ["Ben","Joel","Brandon","Aron","Austin","Jordan","Josh","Andrew","Daniel"]
companies = ["VenTrac","Mentor","Qualcomm","NASA","Wycliffe","Epic","Intel","Google","EMU"]

print(matchList)
print("Student, Company")
for i in range(0,n):
    print(names[i] + ', ' + companies[matchList[i]-1])
print("Iterations = " + str(iterations))

