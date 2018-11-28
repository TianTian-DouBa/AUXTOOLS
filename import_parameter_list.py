'''
从TB的paramter list中读入参数列表
'''

from struct import pack, unpack
import os.path
from XF_common.XF_SERIALIZING import serializing
from XF_common.XF_LOG_MANAGE import *
from XF_common.XF_STATIC import Pen_Profile

'''
i1 = 256
b_i1 = pack('i',i1)
rslt_i1 = unpack('i',b_i1)

print('i1:{}   b_i1:{}   rslt_i1:{}'.format(i1,b_i1,rslt_i1))
'''
def read_tb_parameter():
    """从TB的paramter list中读入参数列表
    return:<string>"""
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

def dump_avail_pens(csv_path=r'.\packed\Historian List.csv'):
    """将csv文件available historian trends导出成object
    -return:<list> [pen_profile1,pen_profile2,...]
    -csv_path:<str> e.g. r'.\packed\Historian List.csv'
    """
    if not os.path.isfile(csv_path):
        log_args = [csv_path]
        add_log(20, 'file not found. --"{0[0]}"', log_args)
        return
    avail_pens = []
    line = 1
    with open(csv_path,'r', encoding='utf8') as f:
        while True:
            steam = f.readline()
            if not steam:
                break
            if line == 1:
                line += 1
                continue
            pen = Pen_Profile()
            pen.pen_csv_to_list(steam)
            avail_pens.append(pen)
            line += 1
    dump_path = r'.\apens.dtp'
    serializing(avail_pens,dump_path)
    log_args = [dump_path]
    add_log(30, 'fn: dump_avail_pens() dumped to "{0[0]}"', log_args)

if __name__ == '__main__':
    '''
    FILE_PATH = r'.\packed\SETUP.fsd'
    for i in read_tb_parameter():
        print(i)
    '''
    '''
    FILE_PATH = r'.\packed\Historian List.csv'
    avail_pens = []
    line = 1
    with open(FILE_PATH,'r', encoding='utf8') as f:
        while True:
            steam = f.readline()
            #print("{}: {}".format(line,steam))
            if not steam:
                break
            if line == 1:
                line += 1
                continue
            pen = Pen_Profile()
            pen.pen_csv_to_list(steam)
            avail_pens.append(pen)
            line += 1

    for i in avail_pens:
        print(i.en_description, i.ch_description)
    '''
    dump_avail_pens()
