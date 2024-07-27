# import db
from faker.providers import DynamicProvider

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