from address_book import AddressBook
from record import Record


book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

alice_record = Record("Alice")
alice_record.add_phone("1234567890")
alice_record.add_phone("5555555555")


book.add_record(alice_record)

for name, record in book.data.items():
    print(record)


john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  


found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")
