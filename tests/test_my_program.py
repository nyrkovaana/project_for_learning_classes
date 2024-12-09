import pytest
from main import Person, pars_to_person


def test_get_sex_out():
    person_female = Person("Anna", "mobile", "Chrome", "female", 25, 100, "Russia")
    person_male = Person("John", "mobile", "Chrome", "male", 30, 200, "USA")

    assert person_female.get_sex_out() == "женского пола"
    assert person_male.get_sex_out() == "мужского пола"


def test_get_age_out():
    person_1 = Person("Anna", "mobile", "Chrome", "female", 21, 100, "Russia")
    person_2 = Person("John", "mobile", "Chrome", "male", 25, 200, "USA")
    person_3 = Person("Mike", "desktop", "Firefox", "male", 11, 50, "UK")
    person_4 = Person("Lucy", "tablet", "Safari", "female", 102, 500, "India")

    assert person_1.get_age_out() == "год"
    assert person_2.get_age_out() == "лет"
    assert person_3.get_age_out() == "лет"
    assert person_4.get_age_out() == "года"


def test_get_browser_out():
    person_mobile = Person("Anna", "mobile", "Chrome", "female", 25, 100, "Russia")
    person_tablet = Person("John", "tablet", "Safari", "male", 30, 200, "USA")
    person_laptop = Person("Mike", "laptop", "Firefox", "male", 35, 300, "UK")
    person_desktop = Person("Lucy", "desktop", "Opera", "female", 40, 400, "India")

    assert person_mobile.get_browser_out() == "с мобильного браузера"
    assert person_tablet.get_browser_out() == "с планшета через браузер"
    assert person_laptop.get_browser_out() == "с ноутбука через браузер"
    assert person_desktop.get_browser_out() == "с настольного компьютера через браузер"


def test_get_region_out():
    person_with_region = Person("Anna", "mobile", "Chrome", "female", 25, 100, "Russia")
    person_without_region = Person("John", "tablet", "Safari", "male", 30, 200, "-")

    assert person_with_region.get_region_out() == "Регион, из которого совершалась покупка: Russia"
    assert person_without_region.get_region_out() == "Регион, из которого совершалась покупка: не определен"


def test_get_payment_done():
    person_female = Person("Anna", "mobile", "Chrome", "female", 25, 100, "Russia")
    person_male = Person("John", "tablet", "Safari", "male", 30, 200, "USA")

    assert person_female.get_payment_done() == "совершила"
    assert person_male.get_payment_done() == "совершил"


def test_string_out():
    person = Person("Anna", "mobile", "Chrome", "female", 25, 100, "Russia")

    expected_string = ("Пользователь Anna женского пола, 25 лет совершила покупку на 100 y.e. "
                       "с мобильного браузера Chrome. Регион, из которого совершалась покупка: Russia\n")

    assert person.string_out() == expected_string


def test_pars_to_person():
    line = "Anna,mobile,Chrome,female,25,100,Russia\n"
    person = pars_to_person(line)

    assert person.name == "Anna"
    assert person.device == "mobile"
    assert person.browser == "Chrome"
    assert person.sex == "female"
    assert person.age == 25
    assert person.bill == "100"
    assert person.region == "Russia"
