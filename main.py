from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    def edit_phone(self, phone, new_phone):
        phone_obj = Phone(phone)
        new_phone_obj = Phone(new_phone)
        if phone_obj in self.phones:
            index = self.phones.index(phone_obj)
            self.phones[index] = new_phone_obj

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            return phone_obj
        else:
            return None


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if isinstance(record, Record):
            self.data[record.name.value] = record
        else:
            raise ValueError("Your record must be an instance of Record class")

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def __str__(self):
        result = ""
        for key, value in self.data.items():
            result += f"Contact name: {key}, phones: {'; '.join(p.value for p in value.phones)}\n"
        return result.strip()
