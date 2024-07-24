import pymysql
import config


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
