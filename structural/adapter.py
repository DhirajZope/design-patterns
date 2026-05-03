# Adapeters are bridges between two incompatible services.
# Pros:
# 1. Reusability
# 2. Flexibility
# 3. Non-Invasive
#
# Cons:
# 1. Complexity
# 2. Overhead

from abc import ABC, abstractmethod


class BankService:
    def make_payment(self, amount):
        print(f"Processing payment of ${amount}")


class PaymentService(ABC):
    @abstractmethod
    def pay(self, amount): ...


class BankServiceAdapter(PaymentService):
    def __init__(self, bank_service):
        self.bank_service = bank_service

    def pay(self, amount):
        self.bank_service.make_payment(amount)


def process_payment(payment_service, amount):
    payment_service.pay(amount)


bank_service = BankService()
payment_service = BankServiceAdapter(bank_service)
process_payment(payment_service, 100)
