from pydoc import stripid

from faker import Faker
from faker.generator import random
from faker.providers import DynamicProvider

from db import (clazz_list, insert_class, insert_lecturer, insert_student, lecturer_list,
                major_list, \
                specialized_list, )
from model.class_ import Class
from model.Lecturer import Lecturer
from model.student import Student
from name_provider import cities_provider, districts_provider, female_name_provider, \
    last_name_provider, \
    male_name_provider, \
    street_provider

major_provider = DynamicProvider(
    provider_name="major_htilssu",
    elements=major_list,
)

spec_provider = DynamicProvider(
    provider_name="spec_htilssu",
    elements=specialized_list,
)

lec_provider = DynamicProvider(
    provider_name="lec_htilssu",
    elements=lecturer_list,
)

clzz_provider = DynamicProvider(
    provider_name="class_htilssu",
    elements=clazz_list,
)

fake = Faker('it_IT')
fake.add_provider(last_name_provider)
fake.add_provider(female_name_provider)
fake.add_provider(male_name_provider)
fake.add_provider(street_provider)
fake.add_provider(districts_provider)
fake.add_provider(cities_provider)
fake.add_provider(major_provider)
fake.add_provider(spec_provider)
fake.add_provider(lec_provider)
fake.add_provider(clzz_provider)


def gen_address():
    return (
            fake.building_number() + ", " + fake.street_provider_htilssu() + ", "
                                                                             "" +
            fake.districts_provider_htilssu()
            + ", " + fake.cities_provider_htilssu())


# conn = db.conn

student_mail = "st.edu.vn"
lecturer_mail = "edu.vn"

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
    elif len(phone_num) < 10:
        phone_num = "0" + phone_num[1:]

    return phone_num


def random_year_prefix():
    return fake.random_int(min=18, max=24)


def gen_student():
    clazz: Class = fake.class_htilssu()
    school_year = random_year_prefix()
    clazz_id = stripid(clazz.name)
    s = clazz_id.replace(clazz.spec_id, "")[:2]
    if s != str(school_year):
        return None
    idd = fake.numerify(text=f'{school_year}DH######')

    last_name = fake.last_name_htilssu()
    sex = gen_sex()
    first_name = gen_first_name(sex)
    name = last_name + " " + first_name
    email_st = idd + "@" + student_mail
    fake.phone_number()
    phone = gen_phone_number()
    address = gen_address()
    birthday = fake.date_of_birth(minimum_age=18 + current_year - school_year,
                                  maximum_age=18 + current_year - school_year)
    return Student(idd, name, email_st, phone, address, birthday, sex, clazz_id)


def fake_lecturer(number):
    list_lec = []
    for i in range(number):
        id = fake.numerify(text=f'######')
        sex = gen_sex()
        name = fake.last_name_htilssu() + " " + gen_first_name(sex)
        email = fake.email(domain=lecturer_mail)
        phone = gen_phone_number()
        address = gen_address()
        birthday = fake.date_of_birth(minimum_age=27, maximum_age=50)
        major = fake.major_htilssu()
        list_lec.append(Lecturer(id, name, email, phone, address, birthday, sex, major.id))

    return list_lec


def fake_lecturer_and_insert(number):
    list_lec = fake_lecturer(number)
    for lec in list_lec:
        insert_lecturer(lec)


def fake_class(number):
    class_l = []
    for i in range(number):
        spec = fake.spec_htilssu()
        lec = fake.lec_htilssu()
        num_id = fake.numerify(text=f'##')
        class_l.append(Class(spec.id + str(random_year_prefix()) + num_id, spec.id, lec.id))

    return class_l


def fake_class_and_insert(number):
    cl_list = fake_class(number)
    for cl in cl_list:
        insert_class(cl)


def fake_student_and_insert(number):
    for i in range(number):
        student = gen_student()
        if student is None:
            continue
        insert_student(student)
