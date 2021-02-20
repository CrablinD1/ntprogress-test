# ntprogress-test
Тестовое задание


Работа с сервисом должна осуществляться через Interactive CLI
● состояние счетов хранится только в рамках одной сессии
● у клиента может быть только один счет
● валюта у всех счетов одинаковая - USD


Поддерживаемые операции:
○ deposit - операция пополнения счета на сумму, аргументы: client, amount,
description
○ withdraw - операция снятия со счета, аргументы: client, amount, description
○ show_bank_statement - вывод на экран выписки со счета за период, аргументы:
client, since, till


Примеры команд для проверки:
deposit --client="John Jones" --amount=100 --description="ATM Deposit"
withdraw --client="John Jones" --amount=50 --description="ATM Withdrawal"
show_bank_statement --client="John Jones" --since="2021-01-01 00:00:00" --till="2021-03-01 00:00:00"
