import pymysql
import config
from queries import general_queries


async def set_active_comp_for_chairman(tg_id, id):
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
            cur.execute(f"UPDATE users SET id_active_comp = {id} WHERE tg_id = {tg_id}")
            conn.commit()
            cur.close()
            return 1
    except:
        print('Ошибка выполнения запроса на установку соревнований')
        return 0



from queries import get_compId_for_user_query

async def get_Scrutineer(tg_id):
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
            active_comp_id = await general_queries.get_CompId(tg_id)
            cur.execute(f"SELECT scrutineerId FROM competition WHERE compId = {active_comp_id}")
            scrutinner_id = cur.fetchone()
            cur.close()
            return scrutinner_id['scrutineerId']
    except:
        print('Ошибка выполнения запроса поиск scrutinner для chairman')
        return 0


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
            cur.execute(f"SELECT compName, compId FROM competition WHERE chairman_id = {tg_id} and isActive = 1")
            competitions = cur.fetchall()
            cur.close()
            return competitions
    except:
        print('Ошибка выполнения запроса на поиск соревнований для chairman1')
        return 0
