import os


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.funds = 0
        self.withdrawals = 0

    def deposit(self, money, description=''):
        self.ledger.append({"amount": money, "description": description})
        self.funds += money

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            self.funds -= amount
            self.withdrawals += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.funds
    
    def transfer(self, amount, category_to_transfer):
        if self.withdraw(amount, f"Transfer to {category_to_transfer.name}"):
            category_to_transfer.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.funds - amount >= 0:
            return True
        else:
            return False
    
    def __str__(self):
        title = self.get_str_title()
        movements = self.get_str_ledger()
        total = self.get_str_total()
        return f'{title}\n{movements}\n{total}'

    def get_str_title(self):
        max_line_len = 30

        total_asteriscs = max_line_len - len(self.name)
        round_half_asteriscs = total_asteriscs // 2
        asterisc_left = total_asteriscs - round_half_asteriscs
        return f'{(round_half_asteriscs) * "*"}{self.name}{asterisc_left * "*"}'

    def get_str_ledger(self):
        formatted_ledger = ''
        max_description_len = 23
        max_amount_len = 7

        for i in range(len(self.ledger)):
            # Check description length. It can not be upper than 23 characters
            description_title = self.ledger[i]["description"]
            description_spaces = max_description_len - len(description_title)
            if len(description_title) > max_description_len:
                description_spaces = ''
                description_title = description_title[:max_description_len]
            else:
                description_spaces = description_spaces * ' '
            description_formatted = f'{description_title}{description_spaces}'
            
            # Check amount length. It can not be upper than 7 characters
            description_amount = f'{self.ledger[i]["amount"]:.2f}'
            description_amount_str = str(description_amount)
            amount_spaces = max_amount_len - len(description_amount_str)
            if len(description_amount) > max_amount_len:
                pass
            else:
                amount_spaces = amount_spaces * ' '
            amount_formatted = f'{amount_spaces}{description_amount_str}'

            #  Final output format
            if i == len(self.ledger) - 1:
                formatted_item = f'{description_formatted}{amount_formatted}'
            else:
                formatted_item = f'{description_formatted}{amount_formatted}\n'

            formatted_ledger += formatted_item
            
        return formatted_ledger

    def get_str_total(self):
        return f'Total: {self.funds:.2f}'

def create_spend_chart(categories):
    title = 'Percentage spent by category'

    categories_by_percentage = get_category_percentage(categories)
    chart = get_formatted_chart(categories_by_percentage)
    horizontal_labels = get_horizontal_label(categories_by_percentage)
    
    final_bar_chart = title + os.linesep + chart + horizontal_labels
    print(final_bar_chart)
    return final_bar_chart
        
def get_category_percentage(categories):
    categories_by_percentage = {}
    total_withdrawals = 0

    for category in categories:
        total_withdrawals += category.withdrawals

    for category in categories:
        percentage = (category.withdrawals * 100) / total_withdrawals
        if percentage / 10 < 1:
            rounded_percentage = 0
        else:
            rounded_percentage = percentage - (percentage % 10) 
        categories_by_percentage[category.name] = int(rounded_percentage)

    return categories_by_percentage

def get_formatted_chart(categories):
    string_chart = ''
    vertical_label = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    one_space = ' '
    two_spaces = '  '
    bar_sep = '|'

    for label in vertical_label:
        if label / 10 >= 10:
            string_chart += str(label) + bar_sep + one_space
        elif label == 0:
            string_chart += two_spaces + str(label) + bar_sep + one_space
        else:
            string_chart += one_space + str(label) + bar_sep + one_space

        for value in categories.values():
            if label <= value:
                string_chart += 'o'
            else:
                string_chart += one_space
            string_chart += two_spaces
        string_chart += os.linesep

    return string_chart

def get_horizontal_label(categories):
    string_labels = '    -'
    spaces_before_letter = '     '
    two_spaces = '  '
    max_len_category = 0

    for key in categories.keys():
        if len(key) > max_len_category:
            max_len_category = len(key)

    for _ in range(len(categories)):
        string_labels += '---'
    
    string_labels += os.linesep
    string_labels += spaces_before_letter

    for i in range(max_len_category):
        for key in categories.keys():
            try:
                string_labels += key[i] + two_spaces
            except IndexError:
                string_labels += ' ' + two_spaces
        string_labels += os.linesep
        string_labels += spaces_before_letter

    return string_labels
