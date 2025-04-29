class Account:
    def __init__(self, id: int):
        self.id = id
        self.is_admin = False

    def get_id() -> None:
        return id


class Admin(Account):
    def __init__(self, id):
        super().__init__(id)

        self.is_admin = True


acc_1 = Account(1)
acc_2 = Admin(2)
print(acc_1.get_id())
print(acc_2.get_id())
