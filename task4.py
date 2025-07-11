
def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments."
    return wrapper


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main():
    """
    Основний цикл взаємодії бота з користувачем.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, args = parse_input(user_input)

        if cmd in ("exit", "close"):
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif cmd == "add":
            print(add_contact(args, contacts))

        elif cmd == "change":
            print(change_contact(args, contacts))

        elif cmd == "phone":
            print(show_phone(args, contacts))

        elif cmd == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()