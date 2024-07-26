import pymysql
import config
import re
async def create_new_comp(text):
    try:
        conn = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn:
            text = text.split('\n')
            text = [i.split(': ')[1].strip() for i in text]
            cur = conn.cursor()
            sql = "INSERT INTO competition (`compGuid`, `date1`, `date2`, `compName`, `city`, `chairman_Id`, `scrutineerId`, `lin_const`, `isActive`, `isSecret`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, tuple(text))
            conn.commit()
            cur.close()
            return 1
    except:
        print('Ошибка выполнения запроса создания соревнования')
        return 0

async def get_tournament_list():
    try:
        conn = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM competition")
            comp = cur.fetchall()
            cur.close()
            text = ''
            for i in comp:
                for k in i:
                    text += f'{k}: {i[k]}\n'
                text += '\n'
            return text
    except:
        print('Ошибка выполнения запроса поиск scrutineer для chairman')
        return 0

async def get_tournament(id):
    try:
        conn = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM competition WHERE compId = {id}")
            comp = cur.fetchone()
            cur.close()
            text = ''
            for k in comp:
                text += f'{k}: {comp[k]}\n'
            return text
    except:
        print('Ошибка выполнения запроса поиск scrutinner для chairman')
        return 0

async def edit_tournament(id, text):
    try:
        text = text.split('\n')
        text = [i.split(': ')[1].strip() for i in text]
        print(text)
        conn = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn:
            cur = conn.cursor()
            cur.execute(f"UPDATE competition  SET compId = {text[0]}, date1 = {text[2]}, date2 = {text[3]}, compName = {text[4]}, city = {text[5]}, chairman_Id = {text[6]}, scrutineerId = {text[7]}, lin_const = {text[8]}, isActive = {text[9]}, isSecret = {text[10]}  WHERE compId = {id}")
            conn.commit()
            cur.close()
            return 1
    except:
        print('Ошибка выполнения запроса создания соревнования')
        return 0