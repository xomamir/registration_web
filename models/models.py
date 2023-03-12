import datetime


class User:
    def __init__(
        self, 
        login:str, 
        password: str,

        first_name: str, 
        last_name: str, 
        is_admin: bool, 
        ) -> None:
        self.login = login
        self.password = password

        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.datetime_created = datetime.datetime.now()
    @staticmethod
    def create_user(
        login: str,
        password: str,
        password2: str,
        first_name: str,
        last_name: str,
        users:list['User']
    ) -> 'User':
        if password!=password2:
            raise ValueError(
                'Ошибка в равенстве паролей'
            )
        user: User = User(
            login = login,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_admin=False
        )
        if user.is_valid(users):
            return user
        else:
            raise ValueError(
                    "Не прошёл валидацию"
                )
    def is_valid(self, users: list['User']) -> bool:
        for i in users:
            if i.login == self.login:
                raise ValueError(
                    "Не прошёл валидацию"
                )
        if len(self.password)<5:
            return False
        return True







