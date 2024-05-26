# payments.py
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, customer_email, amount):
        self.customer_email = customer_email
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, customer_email, amount, card_number, expiry_date, cvv):
        super().__init__(customer_email, amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self):
        # Simulate credit card payment processing logic
        print(f"Processing credit card payment for {self.amount}...")
        payment_status = "Success"
        return payment_status

class PayPalPayment(Payment):
    def __init__(self, customer_email, amount, paypal_id):
        super().__init__(customer_email, amount)
        self.paypal_id = paypal_id

    def process_payment(self):
        # Simulate PayPal payment processing logic
        print(f"Processing PayPal payment for {self.amount}...")
        payment_status = "Success"
        return payment_status

class BankTransferPayment(Payment):
    def __init__(self, customer_email, amount, bank_account):
        super().__init__(customer_email, amount)
        self.bank_account = bank_account

    def process_payment(self):
        # Simulate bank transfer payment processing logic
        print(f"Processing bank transfer payment for {self.amount}...")
        payment_status = "Success"
        return payment_status

class CashPayment(Payment):
    def process_payment(self):
        # Simulate cash payment processing logic
        print(f"Processing cash payment for {self.amount}...")
        payment_status = "Success"
        return payment_status
