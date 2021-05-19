import jinja2
import FileHelper as FH
import Config as CF
import DBHelper as DB
import time
from jinja2 import Template as JinjiaTP

#
def creatPost(title):
    author = CF.getLZConfig()['site']['author']
    categery = CF.getLZConfig()['site']['default_categery']
    template = '''++++
title: "%s"
author: "%s"
categery: "%s"
create_time: %d
#请确保没每项都正确 create_time 为创建时生成的时间戳
++++

'''%(title, author,categery,int(time.time()*1000))
    
    with open(f'./posts/{title}.md','w',encoding='utf-8') as f:
        f.write(template)
        f.flush()
        f.close()
        
def outputIndex():

    m = DB.queryAll()
    
    return m

def createHtmlPost():
    
    temp = JinjiaTP(FH.readFileToStr(f'{CF.getThemePath()}layout/post.html'))
    posts_info = DB.queryAll()
    
    for i in posts_info:
        
        
        title = i[1]
        author = i[2]
        categery = i[3]
        link = i[4]
        create_time = i[5]
        update_time = i[6]
        content = i[7]
        
        ret = temp.render(title=title,author=author,categery=categery,link=link,create_time=create_time,update_time=update_time,content=content,url_for=CF.getDomain())
        
        FH.writeFileToPath(ret,f'./public/{i[3]}/{i[1]}.html')
    
def createHomeIndex():
    
    temp = JinjiaTP(FH.readFileToStr(f'{CF.getThemePath()}layout/index.html'))
    
    posts=[]
    dict={}
    source_post = DB.queryAll()

    for i in source_post:
        dict['id']=i[0]
        dict['title']=i[1]
        dict['author']=i[2]
        dict['categery']=i[3]
        dict['link']=i[4]
        dict['create_time']=i[5]
        dict['update_time']=i[6]
        dict['content']=i[7]
        posts.append(dict)
        dict={}
    
    
    
    ret = temp.render(posts=posts,url_for=CF.getDomain())
    #print(ret)
    FH.writeFileToPath(ret,f'./public/index.html')
    
    
    
    
    
    
    
