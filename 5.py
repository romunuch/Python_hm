# def calc(*args):
#     result=args[0]+args[1]
#     if len(args)>=3:          
#         pr=1    
#         for i in args[2:]:    
#             pr*=i
#         if min(args[2:])!=0:
#             min(args[2:])
#             result+=pr/min(args[2:])
#         else:
#             result=0 
#     return result

# def print_result(result):
#     if result!=0:
#         print(f'Result is - {result}')
#     else:    
#         print(f'result = {result}, Error:dividing by 0')

# print_result(calc(1,2,3,4,5))

# #task 0
# def find_element(*args):
#     result=[0,args[0]]
#     j=0
#     while j<len(args):
#         tmp_count=0
#         for v in args:
#             if v==args[j]:
#                 tmp_count+=1
#         if result[0]<tmp_count:
#             result=[tmp_count, args[j]]
#         elif result[0]==tmp_count and result[1]!=args[j]:
#             result.append(args[j])   
#         j+=1                        
#     return result

# def print_element(anyresult):
#     if len(anyresult[1:])==1:
#         print(f'Most common element is {anyresult[1]}, it was found {anyresult[0]} times')
#     else:
#         print(f'Most common elements are {set(anyresult[1:])}, they were found {anyresult[0]} times')    

# print_element(find_element((1,2),2,(1,2),1,(1,2),3,3,2,3))

#task 1
A=[[1,2,3],[4,5,6],[7,8,9]]

def average(m):
    n=len(m)
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=m[i][j]
    return sum/n**2

print(average(A))
from functools import reduce
# print(lambda A,sum:sum/len(A)**2 for i in A: for j in i:sum+=i[j])
sum=(reduce(lambda x,y:x+y,A)/len(A)**2)
print(sum)

# #task 2
# A=[[1.5,2,3.4,10],[4,5.8,6,11.1],[7,8.7,9,12.2]]
# p1=input('enter float p1 - ')
# p2=input('enter float p2 - ')

# def task2(m,p1,p2):
#     elem=0
#     for i in range(3):
#         for j in range(4):
#             if float(m[i][j])>=float(p1) and float(m[i][j])<=float(p2):
#                 elem+=1
#     return elem
# print (f'Number of matrix elements, that >={p1} and <={p2}: {task2(A,p1,p2)}')

# #task 4
# A=[[-1,-2,-3],[4,5,6],[7,8,9]]
# # A=[[1,2,-3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


# def find_plus(m):
#     n=len(m)
#     result=0
#     for i in range(n):
#         for j in range(n):
#             if i<j:
#                 if m[i][j]>=0:
#                     result+=1
#     return result                

# print(f'Number of plus elements, that are above the main diagonal - {find_plus(A)}')

# #task 3
# group=[{'name'='Roman', 'surname'='Trus', 'gender'='M', 'age'='20'},{'name'='Kirill', 'surname'='Chaichits', 'gender'='M', 'age'='25'},{'name'='Igor', 'surname'='Ksednikov', 'gender'='M', 'age'='25'},{'name'='Denis', 'surname'='Kuliomin', 'gender'='M', 'age'='30'},{'name'='Vyacheslav', 'surname'='Kraskovsky', 'gender'='M', 'age'='30'}]

# def input_info():
    



        
        
        