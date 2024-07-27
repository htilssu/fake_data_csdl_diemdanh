# read json file
import json

from faker import Faker

with open('subject.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

subject_id_len = 5

fake = Faker()


def gen_subject_id():
    return fake.random_int(min=10 ** (subject_id_len - 1), max=(10 ** subject_id_len) - 1)


def gen_credit():
    return fake.random_int(min=1, max=6)


def gen_subject_name():
    return fake.word()


def gen_subjects():
    subjects = []
    for i in data:
        print(i)


gen_subjects()


class Subject:
    def __init__(self, idd, name, credit):
        self.id = idd
        self.name = name
        self.credit = credit
