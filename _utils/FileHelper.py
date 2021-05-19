import os,shutil,re
import Config as CF
import DBHelper as DB
import mistune as mt
from lnzupy import fileos
    
def __copyThemeSource():
    now = CF.getThemePath()+'source/'
    to = './public/source/'
    fileos.copyPathChildToPath(now,to)

def __copySourceToPublic():
    now = './source/'
    to = './public/source/'
    fileos.copyPathChildToPath(now,to)

def __mkdirCategery(list):
    for i in list:
        p = f'./public/{i}'
        if os.path.exists(p) == False:
            os.makedirs(p)
            
def initPathAndSource():
    fileos.initPath('./posts/')
    __copyThemeSource()
    __mkdirCategery(DB.queryCategery())
    __copySourceToPublic()

def __getFilsToPath(path):
    li = []
    for root,dirs,files in os.walk(path):
        for i in files:
            li.append(os.path.join(path,i))
        return li
    
def writeFileToPath(str,path):
    with open(path,'w',encoding='utf-8') as f:
        f.write(str)
        f.flush()
        f.close()
        
def readFileToStr(path):
    with open(path,'r',encoding='utf-8') as f:
        st = f.read()
        f.close()
        return st
        
def outPutDB():
    files = __getFilsToPath('./posts/')
    
    count = 0
    
    for i in files:
        count+=1
        print(f'正在处理 {i}')
        s = readFileToStr(i)
        
        post_config = CF.getPostConfig(s)
        
        title = post_config['title']
        author = post_config['author']
        categery = post_config['categery']
        link =CF.getDomain() + categery + '/' +title+ '.html' 
        create_time = post_config['create_time']
        
        post_source = re.sub(r'\+{3,8}\n(.*\n){0,}\+{3,8}\n','',s,re.M)
        content = mt.markdown(post_source)
        
        
        update_time = int(os.path.getmtime(i)*1000)
        DB.insert(title,author,categery,link,create_time,update_time,content)
        
    print(f'本次处理了 {count} 个文章')
    
    
    
    

    
    
    

