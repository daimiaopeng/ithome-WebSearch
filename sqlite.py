import sqlite3

def to_list(infor):
    w = []
    for i in infor:
        p = []
        for temp in i:
           p.append(temp)
        w.append(p)
    return w

def get_infor(comment):
    conn = sqlite3.connect('E:\\PATH\\Python\\sqlite\\ithome.db')
    # conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # cursor.execute('SELECT * FROM comment WHERE 评论>?', ('123',))
    cursor.execute('SELECT * FROM comment WHERE 评论 LIKE ?',('%'+comment+'%',))
    # cursor.execute('SELECT * FROM it之家个人信息 WHERE 昵称 LIKE "%刺%"')
    infor = cursor.fetchall()
    # for i in values:
    #     print(i)
    # print(comment)
    cursor.close()
    conn.commit()
    conn.close()
    return to_list(infor)


def sort_date(infor):
    def b(infor):
        return infor[11]
    infor.sort(key=b, reverse=True)
    return infor

def get_image(id):
    conn = sqlite3.connect('E:\\test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM it之家个人信息 WHERE id = '+str(id))
    info = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return info[0][6]
