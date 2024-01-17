#
# Nach dem Parameter steht ein Doppelpunkt mit einem Datentyp, dieser ist ein Indikator für Python was als Parameter zu erwarten ist, dies können sie fürs Erste ignorieren.
#
def init_books():
    pass


def read_rental():
    pass


def add_rental(books: dict):
    """

    :param books: typ Dictionary
    :return:
    """
    print('Here is the book rental part')


def show_balance(books: dict):
    """
    shows the balance
    :param books:
    :return:
    """
    print('Print the book balance here')


def read_int(prompt: str, minimum: int, maximum: int):
    return int(input(prompt))  # Placeholder to let main run. Delete when doing the aassignment


def read_date(prompt):
    """

    :param prompt:
    :return:
    """
    pass


def main():
    books = init_books()
    while True:
        print('\nLibrary Management System')
        print('1. Add Rental')
        print('2. Show Balances')
        print('3. Exit')
        choice = read_int('Enter your choice (1/2/3): ', 1, 3)

        if choice == 1:
            add_rental(books)
        elif choice == 2:
            show_balance(books)
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
