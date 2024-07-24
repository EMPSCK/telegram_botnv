
async def load_list(tg_id, text):
    judges_lst = text.split(', ')
    judges_lst = [i.strip().strip('\n').strip('.').strip() for i in judges_lst]
    print(judges_lst)
    a = ';'.join(judges_lst)
