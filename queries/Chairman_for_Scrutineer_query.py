import pymysql
import config
from queries import get_compId_for_user_query

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