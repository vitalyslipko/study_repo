class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'


class OrderFromAliexpress:

    demand = 198

    def order(self, info):
        self.verification(info)
        print(f"Goods can be ordered")

    def verification(self, info):
        if not self.availability(info):
            raise MyCustomError

    def availability(self, info):
        if self.demand > 100:
            return False
        else:
            return True


x = OrderFromAliexpress()
x.order("")
