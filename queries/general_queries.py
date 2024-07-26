import config
import pymysql

async def active_or_not(id):
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
            cur.execute(f"SELECT isActive FROM competition WHERE compId = {id}")
            active_or_not1 = cur.fetchone()
            cur.close()
            return active_or_not1['isActive']
    except:
        print('Ошибка выполнения запроса активное соревнование или нет')
        return 0


async def get_CompId(tg_id):
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
            cur.execute(f"SELECT id_active_comp FROM users WHERE tg_id = {tg_id}")
            id_active_comp = cur.fetchone()
            cur.close()
            return id_active_comp['id_active_comp']
    except:
        print('Ошибка выполнения запроса поиск активного соревнования')
        return 0

async def CompId_to_name(id):
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
            cur.execute(f"SELECT compName FROM competition WHERE compId = {id}")
            name = cur.fetchone()
            cur.close()
            return name['compName']
    except:
        print('Ошибка выполнения запроса поиск активного соревнования')
        return 'не установлено'