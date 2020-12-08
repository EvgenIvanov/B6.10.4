from classes.guests import Guest
from classes.db import Storage

db = Storage()
print('id = ' + str(db.add_account(Guest('Дональд', 'Трамп', 'город Нью-Йорк', 'президент'))))
print('id = ' + str(db.add_account(Guest('Барак', 'Абама', 'город Вашингтон', 'экс президент'))))
print('id = ' + str(db.add_account(Guest('Джейн', 'Псаки', 'Свинарник №3', 'курица'))))

for id in db.entitys:
    print(db.get_account_by_id(id))