from Comparser import parse_input
from processing import add_contact, change_phone, show_num, birthday_add, show_birthday, save_data, load_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            message = add_contact(args, book)
            print(message)

        elif command == "change":
            message = change_phone(args, book)
            print(message)

        elif command == "phone":
            message = show_num(args, book)
            print(message)

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            message = birthday_add(args, book)
            print(message)

        elif command == "show-birthday":
            message = show_birthday(args, book)
            print(message)

        elif command == "birthdays":
            message = book.get_upcaming_birthdays(book)
            print(message)

        else:
            print("Invalid command.")
    save_data(book)

if __name__ == "__main__":
    main()


