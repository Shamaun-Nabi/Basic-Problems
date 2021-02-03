def generateCommonChoices(filename1,filename2):
    file1=open(filename1)
    file2=open(filename2)
    friend1_lines=file1.readlines()
    friend2_lines=file2.readlines()
    
#remove new line from friend 1
    for i in range(len(friend1_lines)-1):
        friend1_lines[i]=friend1_lines[i][:-1]

#remove new line from friend 2
    for i in range(len(friend2_lines)-1):
        friend2_lines[i]=friend2_lines[i][:-1]

    friend1_as_set=set(friend1_lines)
    friend2_as_set=set(friend2_lines)

    if (friend1_as_set & friend2_as_set):
        commonRides=(friend1_as_set & friend2_as_set)
    else:
        print("no common")
    return list(commonRides)                                                         
