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
        elif self.sex == "male": return "мужского пола"
        else: return ""
    def get_age_out(self):
        age = int(self.age)
        if 10 <= age % 100 <= 19 or age % 10 >= 5 or age % 10 == 0: return "лет"
        elif age % 10 == 1: return "год"
        elif 2 <= age % 10 <= 4: return "года"
        else: return ""
    def get_browser_out(self):
        if self.device == "mobile": return "с мобильного браузера"
        elif self.device == "tablet": return "с планшета через браузер"
        elif self.device == "laptop": return "с ноутбука через браузер"
        elif self.device == "desktop": return "с настольного компьютера через браузер"
        else: return ""
    def get_region_out(self):
        if self.region: return f"Регион, из которого совершалась покупка: {self.region}."
        else: return ""
    def get_payment_done(self):
        if self.sex == "female": return "совершила"
        else: return "совершил"
    def string_out(self):
        sex_out = self.get_sex_out()
        age_out = self.get_age_out()
        browser_out = self.get_browser_out()
        region_out= self.get_region_out()
        payment_done_out = self.get_payment_done()
        string = (f"Пользователь {self.name} {sex_out}, "
                  f"{self.age} {age_out} {payment_done_out} "
                  f"покупку на {self.bill} y.e. {browser_out} {self.browser}. {region_out}")
        return string

def pars_to_list(line):
    string = line.strip().split(',')
    name, device, browser, sex, age, bill, *region = string
    region_str = region[0]
    person = Person(name, device, browser, sex, age, bill, region_str)
    return person

with open('web_clients_correct.csv', 'r') as log_file:
    next(log_file)
    with open('results.txt', 'w') as file:
        for line in log_file:
            person = pars_to_list(line)
            file.write(person.string_out())



#string = Person("Allen  Miss. Elisabeth Walton", "mobile","Chrome","female",
#                "29", "885","St Louis: MO")
#string1 = Person('Barber  Miss. Ellen "Nellie"', "laptop","Firefox","male",
#                "32", "885","")
