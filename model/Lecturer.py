class Lecturer:

    def __init__(self, id, name, email, phone, address, birthday, sex, id_major):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.birthday = birthday
        self.sex = sex
        self.id_major = id_major

    def __str__(self):
        return (f"{self.id} - {self.name} - {self.email} - {self.phone} - {self.address} - "
                f"{self.birthday} - {self.sex} - {self.id_major}")
