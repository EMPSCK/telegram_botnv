import pymysql
import config
from queries import general_queries

def get_list_comp(tg_id):
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
            cur.execute(f"SELECT compName, compId FROM competition WHERE scrutineerId = {tg_id} and isActive = 1")
            competitions = cur.fetchall()
            cur.close()
            return competitions
    except:
        print('Ошибка выполнения запроса на поиск соревнований для chairman1')
        return 0



async def get_Chairman(tg_id):
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
            cur.execute(f"SELECT chairman_Id FROM competition WHERE scrutineerId = {tg_id}")
            chairman_id = cur.fetchone()
            cur.close()
            return chairman_id['chairman_Id']
    except:
        print('Ошибка выполнения запроса поиск chairman для scrutineer')
        return 0