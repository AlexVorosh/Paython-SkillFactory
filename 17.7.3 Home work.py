money = int(input("money = "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

deposit.append(int(money * per_cent['ТКБ']/100))
deposit.append(int(money * per_cent['СКБ']/100))
deposit.append(int(money * per_cent['ВТБ']/100))
deposit.append(int(money * per_cent['СБЕР']/100))
# Пока не понимаю, как сделать код проще, чтобы при добавлении новых данных в словарь, не приходилось писать новый запрос deposit. append....
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))