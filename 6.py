#task 0
def input_t0():
    return input('Enter string: ').split(input('Enter separator: '))    
def result_t0(l):
    return list(map(lambda word: str(len(word))+word,l))

def result_test():
    assert result_t0(['one','two','four'])==['3one','3two','4four']    

result_test()
print(result_t0(input_t0()))

# def input_test(l):
#     assert input_t0() is list
# input_test(input_t0())

#task 1
limit=int(input('Enter a limit of numbers: '))

from math import sqrt

def result_t1(limit):
    list_t1 = range(2, limit)
    for step in range(2, int(sqrt(limit+1))):
        list_t1 = list(filter(lambda x: x == step or x % step, list_t1))
    return list_t1

def test_t1():
    assert result_t1(8)==[2,3,5,7]

test_t1()
print(result_t1(limit))                   