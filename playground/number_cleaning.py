import re


class number_cleaner:
    def __init__(self):
        self.r = re.compile(r"\d")

    def clean_number(self, phone_number):
        numbers = self.r.findall(phone_number)
        area_code = "".join(numbers[-10:-7])
        first_3 = "".join(numbers[-7:-4])
        last_4 = "".join(numbers[-4 : len(numbers)])
        return "({}) {}-{}".format(area_code, first_3, last_4)


def cleaner(phone_number):
    r = re.compile(r"\d")
    numbers = r.findall(phone_number)
    area_code = "".join(numbers[-10:-7])
    first_3 = "".join(numbers[-7:-4])
    last_4 = "".join(numbers[-4 : len(numbers)])
    return "({}) {}-{}".format(area_code, first_3, last_4)


if __name__ == "__main__":
    phone_numbers = ["(123) 456-7890", "1234567890", "123.456.7890", "+1 123 456-7890"]

    results = map(cleaner, phone_numbers)
    print(list(results))

    cleaner = number_cleaner()

    print(list(map(cleaner.clean_number, phone_numbers)))
