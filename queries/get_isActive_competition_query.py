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