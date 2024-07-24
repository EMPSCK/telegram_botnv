import pymysql
import config
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
            active_comp_id = await get_compId_for_user_query.get_CompId(tg_id)
            cur.execute(f"SELECT scrutineerId FROM competition WHERE compId = {active_comp_id}")
            scrutinner_id = cur.fetchone()
            cur.close()
            return scrutinner_id['scrutineerId']
    except:
        print('Ошибка выполнения запроса поиск scrutinner для chairman')
        return 0
