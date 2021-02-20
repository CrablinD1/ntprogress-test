from datetime import datetime
from prettytable import PrettyTable


class Client:
    operations = []
    bank = {}

    def deposit(self, client_name, amount, description):
        try:
            self.bank[client_name] += amount
        except KeyError:
            self.bank[client_name] = amount
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operations.append(
            [description, date, amount, self.bank[client_name], client_name])
        return 'Deposit operation was successful!'

    def withdraw(self, client_name, amount, description):
        try:
            if self.bank[client_name] >= amount:
                self.bank[client_name] -= amount
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.operations.append(
                    ([description, date, -amount, self.bank[client_name],
                      client_name]))
                return 'Withdrawal operation was successful!'
            else:
                return 'not enough money'
        except KeyError:
            return 'client not found'

    def show_bank_statement(self, client_name, since, till):
        timing = []
        for i in self.operations:
            if since <= i[1] <= till and i[4] == client_name:
                timing.append(i)
        if not timing:
            return 'no operations during that period or client not found'
        return self.create_table(timing)

    def create_table(self, timing):
        table = PrettyTable()
        table.field_names = ["Date", "Desctiption", "Withdrawals", "Deposits",
                             "Balance"]
        w, d = 0, 0
        for i in timing:
            if i[2] > 0:
                table.add_row([i[1], i[0], '', i[2], i[3]])
                w += i[2]
            if i[2] < 0:
                table.add_row([i[1], i[0], i[2], '', i[3]])
                d += i[2]
        table.add_row(
            ['', 'Total', f'${w}', f'${d}', f'${self.bank[client_name]}'])
        return table


if __name__ == "__main__":
    print('Service started! Enter "exit" to close service')
    a = Client()
    while True:
        mess_in = input()
        if mess_in == 'exit':
            print('Goodbye')
            break
        else:
            mess = mess_in.split('--')
            try:
                command = mess[0]
                client_name = mess[1].split('"')[1]
                description = mess[3].split('"')[1]
            except IndexError:
                print('wrong command')
                continue
            if command == 'deposit ':
                amount = mess[2].split('=')[1]
                print(Client.deposit(a, client_name, int(amount), description))
            elif command == 'withdraw ':
                amount = mess[2].split('=')[1]
                print(
                    Client.withdraw(a, client_name, int(amount), description))
            elif command == 'show_bank_statement ':
                amount = mess[2].split('"')[1]
                print(Client.show_bank_statement(a, client_name, amount,
                                                 description))
            else:
                print('command not found', command)
