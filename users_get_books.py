import json
from csv import DictReader


def get_new_users_list():
    """Get a new list of users from users.json"""
    with open("users.json", "r") as f:
        users = json.loads(f.read())
        new_users_list = []
        for user in users:
            dict_sample = {}
            for key, value in user.items():
                if key == "name":
                    dict_sample["name"] = value
                elif key == "address":
                    dict_sample["address"] = value
                elif key == "gender":
                    dict_sample["gender"] = value
                elif key == "age":
                    dict_sample["age"] = value
            new_users_list.append(dict_sample)
    return new_users_list


def get_new_books_list():
    """Get a new list of books from books.cvs"""
    with open('books.csv', newline='') as f:
        reader = DictReader(f)

        new_books_list = []
        for row in reader:
            sup_dict = {}
            for key, value in row.items():
                if key == "Pages":
                    sup_dict[key.lower()] = int(value)
                elif key == "Publisher":
                    pass
                else:
                    sup_dict[key.lower()] = value
            new_books_list.append(sup_dict)
    return new_books_list


def get_next_book(books):
    """Generator to get 1 book from books list"""
    for book in books:
        yield book


def users_receive_books(users, books, book):
    """Add books to users.
    All users receives "number_of_books_for_all_users".
    "number_of_users_who_got_more_books" - its an amount of users who receive one more book
     """
    number_of_users_who_got_more_books = len(books) % len(users)
    number_of_books_for_all_users = (len(books) // len(users))

    for user in users[0:number_of_users_who_got_more_books]:
        for i in range(0, (number_of_books_for_all_users + 1)):
            key = "books"
            user.setdefault(key, [])
            user[key].append(next(book))

    for user in users[number_of_users_who_got_more_books: len(users)]:
        for i in range(0, number_of_books_for_all_users):
            key = "books"
            user.setdefault(key, [])
            user[key].append(next(book))
    return users


def write_new_users_with_books_list(users_with_books):
    """Write new users with books list in json"""
    with open("result.json", "w") as f:
        s = json.dumps(users_with_books, indent=4)
        f.write(s)


if __name__ == '__main__':
    users = get_new_users_list()
    books = get_new_books_list()
    book = get_next_book(books)
    users_with_books = users_receive_books(users, books, book)
    write_new_users_with_books_list(users_with_books)

