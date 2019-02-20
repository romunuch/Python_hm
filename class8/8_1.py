with (open('/home/romunuch/univer/python/class8/django_setup.py','r')) as f:
    line_count=0

    print(f'There are {sum(1 for line in f)} strings at this file:')
    f.seek(0)
    letters=set('ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz')    
    for i,line in enumerate(f.readlines()):
        # print(f'{list(filter(lambda x:line.,line.split(' ')))}
        if set(line) & letters:
            tmp_list=line.split()
        else:
            tmp_list=[]
        # tmp_list=[line.split() for line in f.readlines() if set(line)&letters]     
        print(f'\tString-{i+1}: Words - {len(tmp_list)}; Symbols - {len(line)}')