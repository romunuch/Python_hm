from time import time

file_n=input('File name --> ')
file_name=file_n+'_'+str(time())+'.txt'


_file=open(file_name, 'a')

def write_smt():
    line=input('New line --> ')
    if line=='':
        return
    else:   
        _file.write(f'USER-------{str(time())}-------{line}\n')
        write_smt()
write_smt()
_file.close() 
       




