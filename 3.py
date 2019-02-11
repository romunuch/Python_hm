# def enter():
#     def_str=input('your string: ')
#     def_num=input('your number: ')
#     return def_str, def_num

# def check(our_tuple):
#     numbers=set('0123456789')

#     if len(set(our_tuple[0]).intersection(numbers)):

#         if our_tuple[1] in our_tuple[0]:
#             print(f'{our_tuple[1]} is in this string')
#         else:
#             print(f'There is number in {our_tuple[0]}, but it is not {our_tuple[1]}')

#     else:
#         print('There is no numbers')

# check(enter())


# #task 0

# def input_numbers():
#     num_str=input('enter numbers(\',\' is a separator) - ')
#     num_to_find=input('number to find - ')
#     return num_str.split(','), num_to_find

# def find_number(input_tuple):
#     num_list=input_tuple[0]
#     count=0
#     for i in range(len(num_list)):
#         if num_list[i]==input_tuple[1]:
#             count+=1
#     if count>0:
#         print(f'Number {input_tuple[1]} is listed {count} times in {num_list}')
#     else:
#         print(f'There is no {input_tuple[1]} in list {num_list}')            

# find_number(input_numbers())

# #task 1 - без методов строк для этой задачи
# my_word=input('enter a word - ')


# def check_first(any_word):
#     first_s=ord(any_word[0])
#     if (first_s>=65 and first_s<91) or (first_s>=97 and first_s<123) or first_s==95:
#         return True
#     else:
#         return False


# def word_check(any_word):
#     bool_valid=True
#     if check_first(any_word):
#         for i in range(len(any_word)):
#             if (ord(any_word[i])>=65 and ord(any_word[i])<=90) or (ord(any_word[i])>=97 and ord(any_word[i])<=122) or (ord(any_word[i])>=48 and ord(any_word[i])<=57) or ord(any_word[i])==95:
#                 continue
#             else:
#                 bool_valid=False
#                 print('it is not an identifier')
#                 break
#         if bool_valid:
#             print('This word is an identifier')      
#     else:
#         print('it is not an identifier')

# word_check(my_word)              

# #task 2
# def input_text():
#     return input('enter the text:\n - ').split(' ')

# def find_vovels(any_text):
#     the_shortest=any_text[0]
#     for i in any_text:
#         if len(the_shortest)>len(i):
#             the_shortest=i
#     vovels=set('AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя')
#     if vovels & set(the_shortest):
#         print('These are vovels from the shortest word - ', vovels & set(the_shortest))
#     else:
#         print('There is no vovels')    

# find_vovels(input_text())    

# # task 3
# def input_strings():
#     return input('enter numbers(\',\' is a separator) - ').split(',')

# def find_the_longest_string(string_list):
#     the_longest=string_list[0]
#     l_index=[]
#     for i in range(len(string_list)):
#         if len(the_longest)<len(string_list[i]):
#             the_longest=string_list[i]
#             l_index=list(string_list.index(stringlist[i]))
#         elif len(the_longest)==len(string_list[i]) and the_longest==string_list[i]:#если правильно понял задание
#             l_index.append(i)
#     print(f'The longest string - {the_longest}\nIt is listed by numbers - {l_index}')

# find_the_longest_string(input_strings())

# # task 4
# P=float(input('Percent is (between 0 and 25)- '))*0.01
# money=1000.0
# month=0
# while money<=1100:
#     money+=money*P
#     month+=1
# else:
#     print(f'After {month} month this investment will be {money}')

# task 4_2
# P=float(input('Percent is (between 0 and 25)- '))*0.01
# money=1000.0
# month=0
# if P>0 and P<=0.25:
#     while money<=1100:
#         money+=money*P
#         month+=1
#     else:
#         print(f'After {month} month this investment will be {money}')
# else:
#     print('This percent is incorrect')        

# task 5
# list_five=input('Enter list(\',\' is a separator) - ').split(',')
# null_count=list_five.count('0')
# if null_count!=0:
#     for i in list_five:
#         if i=='0':
#             list_five.remove(i)
#     for i in range(null_count):
#         list_five.append('-1')
#     print(list_five)    
# else:
#     print(f'There is no \'0\' elements in list {list_five}')

# # task 6
# list_six=[int(x) for x in input('Enter list, only numbers(\',\' is a separator) - ').split(',')]
# bool_ok=False
# new_list=[]   
# for i in list_six:
#     if i<0:
#         new_list.append(i)
#         list_six.remove(i)
#         bool_ok=True

# if bool_ok:
#     new_list.extend(list_six)
#     print(f'Result - {new_list}')
# else:
#     print('There is no minus elements')

# # task 7
# string_s=input('Your string - ')
# symbol_s=input('Your symbol - ')
# new_string=''
# last=string_s.rfind(symbol_s)

# if last!=-1:
#     for i in string_s:
#         if i==symbol_s:
#             new_string+=i.upper() #возвращает копию, поэтому так
#         else:
#             new_string+=i

#     if (last+1)!=len(new_string):                
#         result_string=new_string[:last+1]    
#         print (f'Result - {result_string}')
#     else:
#         print(f'Result - {new_string}')    
# else:
#     print('Nothing to change')

# task 8
grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]
stop=1
while stop<len(grades):
    for i in range(len(grades)-stop):
        if (grades[i])[1]>(grades[i+1])[1]:
            (grades[i]),(grades[i+1])=(grades[i+1]), (grades[i])
    stop+=1    
for i in grades:
    print(f'Hello {i[0]}! Your grade is {i[1]}')
