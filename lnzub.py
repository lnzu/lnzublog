import sys,os,time,pprint

if os.path.exists('./posts.db'):
    os.remove('./posts.db')

sys.path.append("./_utils/")
from _utils import Config as CF
from _utils import DBHelper as DB
from _utils import FileHelper as FH
from _utils import Template as TP

def Generate():
    
    start = int(abs(time.time()*1000))
    try:
        FH.outPutDB()
        
        FH.initPathAndSource()
        
        TP.createHtmlPost()
        
        TP.createHomeIndex()
        
        
    except Exception as e:
        print('发生已一些错误如下\n')
        print(e)
    finally:
        end = int(abs(time.time()*1000))
        print(f'耗时{(end - start)/1000}s')
    

Generate()

#print('bf')





