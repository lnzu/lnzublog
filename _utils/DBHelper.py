import sqlite3
import pprint

__con = sqlite3.connect("posts.db")

__cur = __con.cursor()

__table_name = 'posts'

__values = ['title','author','categery','link','create_time','update_time','content']

"""
0.标题       title
1.作者       author
2.分类       categery
3.链接       link
4.创建时间    create_time
5.修改时间    update_time
6.文章内容    content
"""

def __init__():    
    a = """id integer primary key autoincrement,
    %s text,
    %s text,
    %s text,
    %s text,
    %s integer,
    %s integer,
    %s text
    """%(__values[0],__values[1],__values[2],__values[3],__values[4],__values[5],__values[6])
    
    sql = "create table if not exists %s(%s)"%(__table_name,a)
    
    __cur.execute(sql)
    
__init__()


def insert(a,b,c,d,e,f,g):
    sql = 'insert into %s(%s,%s,%s,%s,%s,%s,%s) values(?,?,?,?,?,?,?)'%(__table_name,__values[0],__values[1],__values[2],__values[3],__values[4],__values[5],__values[6])
    
    __cur.execute(sql,(a,b,c,d,e,f,g))
    __con.commit()
    
#insert('title','author','11','link',21214255,24512535,'content')

def queryAll():
    sql = 'select * from %s'%(__table_name)
    return __cur.execute(sql).fetchall()

def queryCategery():
    sql = 'select categery from %s'%(__table_name)
    c = __cur.execute(sql).fetchall()
    
    list = []    
    for i in set(c):
        list.append(i[0])
    return list






    

