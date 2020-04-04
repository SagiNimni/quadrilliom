from block import Trader

MAX_TRANSACTIONS = 2400


class Ledger:
    """
    The Ledger the a data of transactions that a single block in a certain block-chain contains
    This class contains functions that are used to edit the Ledger

    When a ledger reaches a certain amount of transactions it is no longer available for transactions
    """
    def __init__(self):
        self.transactions = 0
        self.__data__ = []

    def gets(self):
        pass

    def pays(self, payment, signature):
        pass
