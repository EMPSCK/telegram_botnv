import config
import pymysql

async def load_list(tg_id, text, compid):
    judges_lst = text.split(', ')
    judges_lst = [i.strip().strip('\n').strip('.').strip() for i in judges_lst]
    a = ';'.join(judges_lst)
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
            cur.execute(f"UPDATE competition SET judges_pool = '{a}' WHERE compId = {compid}")
            conn.commit()
            cur.close()
    except Exception as e:
        print(e)
        print('Ошибка выполнения запроса на загрузку списка судей')
