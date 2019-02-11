# nums=[]
# for i in range(6):
#     nums.append(input('number:'))

# while i>=0:
#     print(nums[i])
#     i-=1


# print(nums[::-1])


#1

nums=[]
for i in range(10):
    nums.append(int(input('number:')))
max_of_nums=max(nums)
# nums.remove(max_of_nums)
#print(nums,'deleted max - ', max_of_nums)

for i in range(10):
    if nums[i]==max_of_nums:
        index_max=i

new_nums=nums[:index_max]+nums[index_max+1:]

print(new_nums, ' - without max')
print(nums[index_max], ' - max element')



#2
sec_str='Hello!Anthony!Have!A!Good!Day!'
sec_str_up=sec_str.upper()[:len(sec_str)-1]
sec_list=sec_str_up.split('!')
print(sec_list)

#3
sec_list.sort()
for i in range(len(sec_list)):
        print(sec_list[i])

#4
letter=input('enter your letter: ')
print(letter)

#if ('Ms.' or 'Mrs.' or 'Miss') in letter:
if letter[:9].find('Ms')!=-1 or letter[:9].find('Mrs')!=-1 or letter[:9].find('Miss')!=-1:
        print('Female')
elif 'Mr' in letter[:9]:
        print('Male')
else:
        print('Cannot to be checked')


#5
first_str=input('first string: ')
second_str=input('second string: ')
if second_str in first_str:
        print('Yes,  it\'s a substring')
else:
        print('No, it isn\'t substring')        



    
