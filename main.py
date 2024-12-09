class Person():
    def __init__(self, name, device, browser, sex, age, bill, region):
        self.name = name
        self.sex = sex
        self.age = age
        self.device = device
        self.browser = browser
        self.bill = bill
        self.region = region

    def get_sex_out(self):
        if self.sex == "female": return "женского пола"
        if self.sex == "male": return "мужского пола"
        else: return ""

    def get_age_out(self):
        age = int(self.age)
        if 10 <= age % 100 <= 19 or age % 10 >= 5 or age % 10 == 0: return "лет"
        if age % 10 == 1: return "год"
        if 2 <= age % 10 <= 4: return "года"
        else: return ""

    def get_browser_out(self):
        if self.device == "mobile": return "с мобильного браузера"
        if self.device == "tablet": return "с планшета через браузер"
        if self.device == "laptop": return "с ноутбука через браузер"
        if self.device == "desktop": return "с настольного компьютера через браузер"
        else: return ""

    def get_region_out(self):
        return f"Регион, из которого совершалась покупка: "\
                + (self.region if self.region and self.region != '-' else "не определен")

    def get_payment_done(self):
        return "совершил" + ("а" if self.sex == "female" else "")

    def string_out(self):
        sex_out = self.get_sex_out()
        age_out = self.get_age_out()
        browser_out = self.get_browser_out()
        region_out= self.get_region_out()
        payment_done_out = self.get_payment_done()
        string = (f"Пользователь {self.name} {sex_out}, "
                  f"{self.age} {age_out} {payment_done_out} "
                  f"покупку на {self.bill} y.e. {browser_out} {self.browser}. {region_out}")
        return string + "\n"


def pars_to_person(line):
    string = line.strip().split(',')
    name, device, browser, sex, age, bill, region = string

    age = int(float(age))

    person = Person(name, device, browser, sex, age, bill, region)
    return person


with open('web_clients_correct.csv', 'r') as log_file:
    next(log_file)
    with open('results.txt', 'w') as file:
        for line in log_file:
            person = pars_to_person(line)
            file.write(person.string_out())