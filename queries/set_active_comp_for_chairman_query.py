import pymysql
import config

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
        print('Ошибка выполнения запроса на установку соревнований для chairman')
        return 0
