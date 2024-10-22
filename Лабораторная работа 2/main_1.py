money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month_without_debts = 0 # Количество месяцев без долгов

while True:
    money_capital += salary  # Получение ежемесячной зарплаты
    money_capital -= spend  #  Расходы
    spend += spend * increase #  Рост цен

    if money_capital >= 0:  #  Есть ли долг
        month_without_debts += 1  #  Подсчет количества месяцев без долгов
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month_without_debts)
