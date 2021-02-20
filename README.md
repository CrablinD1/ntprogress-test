<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="ntprogresstest_0"></a>ntprogress-test</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">Тестовое задание</p>
<p class="has-line-data" data-line-start="4" data-line-end="8">Работа с сервисом должна осуществляться через Interactive CLI<br>
● состояние счетов хранится только в рамках одной сессии<br>
● у клиента может быть только один счет<br>
● валюта у всех счетов одинаковая - USD</p>
<p class="has-line-data" data-line-start="10" data-line-end="14">Поддерживаемые операции:<br>
● deposit - операция пополнения счета на сумму, аргументы: client, amount, description<br>
● withdraw - операция снятия со счета, аргументы: client, amount, description<br>
● show_bank_statement - вывод на экран выписки со счета за период, аргументы: client, since, till</p>
<p class="has-line-data" data-line-start="16" data-line-end="20">Примеры команд для проверки:<br>
deposit --client="John Jones" --amount=100 --description="ATM Deposit"<br>
withdraw --client="John Jones" --amount=50 --description="ATM Withdrawal"<br>
show_bank_statement --client="John Jones" --since="2021-01-01 00:00:00" --till="2021-03-01 00:00:00"</p>
