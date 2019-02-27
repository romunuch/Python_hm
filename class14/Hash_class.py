import hashlib
import argparse

manifest_path='/home/romunuch/univer/python/class14/manifest/manifest.txt'

class FileHash:
    def __init__(self, path):
        self.path=path

    def readfile(self):
        with (open(self.path, 'r')) as f:
            content=f.readline()
        return content

    def calchash(self):
        hash=hashlib.md5(self.readfile().encode('utf-8'))
        return self.path, hash.hexdigest()           



class Manifest:
    def __init__(self, path):
        self.path=path

    def write_to(self, content):
        with (open(self.path, 'w')) as mfst:
            for somefile in content:
                mfst.write(f'{somefile[0]}:{somefile[1]}\n')
                print(f'checksum for {somefile[0]} calculated')        
    
    def check(self):
        with (open(self.path, 'r')) as mfst:
            checklist=[line.split(':') for line in mfst.readlines()]

        for somefile in checklist:
            with (open(somefile[0],'r')) as smf:
                content=smf.readline()
                hash=hashlib.md5(content.encode('utf-8'))
                if hash.hexdigest() == somefile[1][:-1]:
                    print(f'{somefile[0]}: OK\n')
                else:
                    print(f'{somefile[0]}: FAILED\n')

          
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--calc', nargs='+', dest='files')
    parser.add_argument('--check', dest='manifest')

    pars = parser.parse_args()
    
    if pars.files:
        manifest=Manifest(manifest_path)
        content=[]
        for f in pars.files:
            f_hash=FileHash(f)
            content.append(f_hash.calchash())
        manifest.write_to(content)

    if pars.manifest:
        m_check=Manifest(pars.manifest)
        m_check.check()



