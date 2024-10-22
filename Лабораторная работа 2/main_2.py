salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

missing_amount = 0  # Количество денег, которых нехватает

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for i in range(0, months):
    missing_amount += salary  # Получение запралаты
    missing_amount -= spend  # Расходы
    spend += spend * increase  # Рост цен

money_capital = int(missing_amount * -1) # Подушка безопасности

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
