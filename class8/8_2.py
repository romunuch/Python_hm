with (open('/home/romunuch/univer/python/class8/Students.txt','r')) as f:
    students=[]
    bad_st=[]
    for line in f.readlines():
        students.append(line.split())
    average=0
    for stud in students:
        average+=int(stud[2])
        if int(stud[2])<3:
            bad_st.append(stud)
    print(f'Average mark of group - {average/len(students)}\nStudents with unsatysfactory mark:')
    for i in bad_st:
        print(f'\t{i[0]} {i[1]} : {i[2]}')    

   
