import pymysql
import config
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
            text = [i.split(')')[1] for i in text]

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
            comp[0] = str(comp[0])
            comp = '\n\n'.join(list(map(str, comp)))
            return comp + '\n/start'
    except:
        print('Ошибка выполнения запроса поиск scrutinner для chairman')
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
            return comp
    except:
        print('Ошибка выполнения запроса поиск scrutinner для chairman')
        return 0

async def edit_tournament(id, text):
    text = text.split('\n')
    text = [i.split(')')[1] for i in text]
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
            sql = "UPDATE competition (`compGuid`, `date1`, `date2`, `compName`, `city`, `chairman_Id`, `scrutineerId`, `lin_const`, `isActive`, `isSecret`) SET (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE compId = {id}"
            cur.execute(sql, tuple(text))
            conn.commit()
            cur.close()
            return 1
    except:
        print('Ошибка выполнения запроса создания соревнования')
        return 0