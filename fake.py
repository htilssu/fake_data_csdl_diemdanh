from faker import Faker
from faker.generator import random
from faker.providers import DynamicProvider

import db
from address_provider import streets, districts, cities

# Tên
last_name_provider = DynamicProvider(
    provider_name="last_name_htilssu",
    elements=["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô"],
)

female_name_provider = DynamicProvider(
    provider_name="female_name_htilssu",
    elements=["Ngọc", "Kim", "Hồng", "Thu", "Hương", "Lan", "Mai", "Phương", "Thùy", "Diệu", "Anh", "Hà", "Yến"],
)
male_name_provider = DynamicProvider(
    provider_name="male_name_htilssu",
    elements=["Trung", "Duy", "Hải", "Hùng", "Minh", "Hà", "Phương", "Quang", "Tùng", "Việt", "An", "Bảo", "Công",
              "Đức", "Huy", "Khoa", "Long", "Nam", "Phúc", "Quốc", "Sơn", "Tùng", "Tuấn", "Vinh"],
)

street_provider = DynamicProvider(
    provider_name="street_provider_htilssu",
    elements=streets,
)

districts_provider = DynamicProvider(
    provider_name="districts_provider_htilssu",
    elements=districts)

cities_provider = DynamicProvider(
    provider_name="cities_provider_htilssu",
    elements=cities,
)

fake = Faker('it_IT')
fake.add_provider(last_name_provider)
fake.add_provider(female_name_provider)
fake.add_provider(male_name_provider)
fake.add_provider(street_provider)
fake.add_provider(districts_provider)
fake.add_provider(cities_provider)


def gen_address():
    return (fake.building_number() + ", " + fake.street_provider_htilssu() + ", " + fake.districts_provider_htilssu()
            + ", " + fake.cities_provider_htilssu())


conn = db.conn

email = "st.edu.vn"

number = 100
current_year = 24


def gen_sex():
    return random.choice([0, 1])


def gen_first_name(gender):
    if gender == 0:
        return fake.male_name_htilssu() + " " + fake.male_name_htilssu()
    else:
        return fake.female_name_htilssu() + " " + fake.female_name_htilssu()


def gen_phone_number():
    phone = fake.phone_number()
    phone_num = len(phone.split(" ")) == 1 and phone.split(" ")[0] or phone.split(" ")[1]
    if len(phone_num) == 9:
        phone_num = "0" + phone_num
    else:
        phone_num = "0" + phone_num[1:]

    return phone_num


def random_year_postfix():
    return fake.random_int(min=18, max=24)


def gen_student():
    school_year = random_year_postfix()
    idd = fake.numerify(text=f'{school_year}DH######')
    last_name = fake.last_name_htilssu()
    sex = gen_sex()
    first_name = gen_first_name(sex)
    name = last_name + " " + first_name
    email_st = idd + "@" + email
    phone = fake.phone_number()
    phone = gen_phone_number()
    address = gen_address()
    birthday = fake.date_of_birth(minimum_age=18 + current_year - school_year,
                                  maximum_age=18 + current_year - school_year)
    return Student(idd, name, email_st, phone, address, birthday, sex)


class Student:
    def __init__(self, id1, name, emaila, phone, address, birthday, sex):
        self.Id = id1
        self.Name = name
        self.Email = emaila
        self.Phone = phone
        self.Address = address
        self.Birthday = birthday
        self.Sex = sex

    def __str__(self):
        return f'{self.Id}, {self.Name}, {self.Email}, {self.Phone}, {self.Address}, {self.Birthday}, {self.Sex}'


for _ in range(number):
    print(gen_student())
