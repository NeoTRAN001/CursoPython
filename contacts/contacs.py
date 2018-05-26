# -*- coding: utf-8 -*-

import csv

class Contact:

    def __init__ (self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__ (self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f: #csv = user, phone, email
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )


    def _print_contact(self, contact):
        print ('--- * --- * --- * --- * --- * --- * --- * --- *\n ')
        print ('Name: {}'.format(contact.name))
        print ('Phone: {}'.format(contact.phone))
        print ('Email: {}'.format(contact.email))
        print ('\n--- * --- * --- * --- * --- * --- * --- * --- *\n')

    def _not_found(self):
        print ('**********\n')
        print ("Name isn't here")
        print ('\n**********\n')
def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)

        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
            What do you want?

            [a] Add contact
            [b] Update contact
            [c] Search contact
            [d] Remove contact
            [e] List of contact
            [f] Exit
        '''))

        if command == 'a':
            name = str(raw_input('Write a name contact: '))
            phone = str(raw_input('Enter the contact number: '))
            email = str(raw_input('Write the contact email: '))

            contact_book.add(name, phone, email)
        elif command == 'b':
            print ('Update contact')
        if command == 'c':
            name = str(raw_input('Write a name contact: '))

            contact_book.search(name)
        elif command == 'd':
            name = str(raw_input('Write a name contact: '))
            contact_book.delete(name)
        if command == 'e':
            contact_book.show_all()
        elif command == 'f':
            print ('Exit')
            break

if __name__ == '__main__':
    print('\nW E L C O M E  T O  L I S T  C O N T A C T\n')
    run()
