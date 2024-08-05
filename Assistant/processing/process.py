from .decorator import input_error
from Assistant.classes import AddressBook, Record
import pickle

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book: AddressBook):
    name, phone, sec_phone = args
    record = book.find(name)
    message = "Phone nymber changed"
    if record is None:
        return "The contact does not exist"
    else:
        record.edit_phone(phone, sec_phone)
        return message

@input_error
def show_num(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        return f"{record}"
    else:
        return "The contact does not exist"

@input_error
def birthday_add(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Birthday added"
    if record:
        record.add_birthday(birthday)
        return message
    else:
        return "The contact does not exist"

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record:
        if record.birthday:
            print(type(record.birthday.value))
            return f"{name} birthday {record.birthday.value}"

    else:
        return "The contact does not exist"

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено
