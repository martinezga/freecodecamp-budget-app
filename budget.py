class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.funds = 0

    def deposit(self, money, description=''):
        self.ledger.append({"amount": money, "description": description})
        self.funds += money

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            self.funds -= amount
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
        if self.funds - amount > 0:
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
        formated_ledger = ''
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
            description_formated = f'{description_title}{description_spaces}'
            
            # Check amount length. It can not be upper than 7 characters
            description_amount = f'{self.ledger[i]["amount"]:.2f}'
            description_amount_str = str(description_amount)
            amount_spaces = max_amount_len - len(description_amount_str)
            if len(description_amount) > max_amount_len:
                pass
            else:
                amount_spaces = amount_spaces * ' '
            amount_formated = f'{amount_spaces}{description_amount_str}'

            #  Final output format
            if i == len(self.ledger) - 1:
                formated_item = f'{description_formated}{amount_formated}'
            else:
                formated_item = f'{description_formated}{amount_formated}\n'

            formated_ledger += formated_item
            
        return formated_ledger

    def get_str_total(self):
        return f'Total: {self.funds:.2f}'

def create_spend_chart(categories):
    categories_by_percentage = {}
    categories_amount = len(categories)
    title = 'Percentage spent by category'

    categories_by_percentage = get_category_percentage(categories)
        
def get_category_percentage(categories):
    pass


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "deposit")
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food')
food.transfer(50, entertainment)

print(food)

