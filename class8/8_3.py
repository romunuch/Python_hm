
import time

def input_search():
    return set(input('Find keys: ').split())
start_time = time.time()
def search(data):
    # result=[]
    with (open('/home/romunuch/univer/python/class8/StudentsDB.txt','r')) as DB:
    #     for student in DB.readlines():
    #         if data <= set(student.split()) and data:
    #             result.append(student.split())
        result=[student.split() for student in DB.readlines() if data<=set(student.split()) and data]
    return result

result=search(set(['21']))
if result:
    for i in result:
        print(f'Name:  {i[0]}\t\tSurname:  {i[1]}\t\tAge:  {i[2]}\t\tGender:  {i[3]}')
else:
    print('No such students')        
print("--- %s seconds ---" % (time.time() - start_time))