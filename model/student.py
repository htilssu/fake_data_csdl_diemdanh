class Student:
    def __init__(self, id1, name, emaila, phone, address, birthday, sex, clazz_id):
        self.Id = id1
        self.Name = name
        self.Email = emaila
        self.Phone = phone
        self.Address = address
        self.Birthday = birthday
        self.Sex = sex
        self.Clazz_id = clazz_id

    def __str__(self):
        return (f'{self.Id}, {self.Name}, {self.Email}, {self.Phone}, {self.Address}, '
                f'{self.Birthday}, {self.Sex}')
