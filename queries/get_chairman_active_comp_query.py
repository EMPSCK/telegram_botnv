import pymysql
import config


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
            cur.execute(f"SELECT compName, compId FROM competition WHERE chairman_id = {tg_id}")
            competitions = cur.fetchall()
            cur.close()
            return competitions
    except:
        print('Ошибка выполнения запроса на поиск соревнований для chairman1')
        return 0
