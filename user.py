class User:
    def __init__(self):
        self.email = input("Introduzca su email: ")
        self.__password = input("Introduzca su contraeña: ")
        self.permissions = ['edit', 'crear', 'update']
        self.username = None

    def set_username(self):
        self.username = input("Introducza su username: ")
        print("Usrname cambiado a : {} ".format(self.set_username))


class Pro_User(User):
    def __init__(self):
        super().__init__()
        self.permissions += ['delete', 'download']

    def pay_subscription(self, cantidad):
        print("Has pagado la suscripción ({})".format(cantidad))


class UserManager:
    def create_user(self, suscripcion):
        if suscripcion:
            User = Pro_User()
        else:
            User = User()
    
        print('Usuario creado.')