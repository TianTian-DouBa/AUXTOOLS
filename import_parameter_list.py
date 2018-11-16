from struct import pack, unpack

FILE_PATH = r'.\SETUP.fsd'

'''
i1 = 256
b_i1 = pack('i',i1)
rslt_i1 = unpack('i',b_i1)

print('i1:{}   b_i1:{}   rslt_i1:{}'.format(i1,b_i1,rslt_i1))
'''
def read_parameter():
    with open(FILE_PATH,'rb') as f:
        slice = '--init--'
        result = []
        while True:
            f.seek(16,1)
            slice = f.read(32)
            if (slice == b'') or (slice == None):
                return result
            _t = slice.decode('ascii').strip('~').replace('|','')
            result.append(_t)

   
for i in read_parameter():
    print(i)
