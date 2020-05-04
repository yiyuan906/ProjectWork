#! /usr/bin/env python

from __future__ import print_function
import Addressbook_pb2 
import sys
from google.protobuf import json_format
import json

def ListPeople(address_book):
  for person in address_book.people:
    print("Person ID:", person.id)
    print("  Name:", person.name)
    if person.email != "":
      print("  E-mail address:", person.email)

    for phone_number in person.phones:
      if phone_number.type == Addressbook_pb2.Person.MOBILE:
        print("  Mobile phone #:", end=" ")
      elif phone_number.type == Addressbook_pb2.Person.HOME:
        print("  Home phone #:", end=" ")
      elif phone_number.type == Addressbook_pb2.Person.WORK:
        print("  Work phone #:", end=" ")
      print(phone_number.number)

address_book = Addressbook_pb2.AddressBook()					#important

with open('/home/yy/fod/jsonfile/part-00000-a32fbff6-10b5-4588-adf4-10f5e1caec1b-c000.json') as f:
	data = json.load(f)

address_book = json_format.ParseDict(data, Addressbook_pb2.AddressBook())

ListPeople(address_book)

with open(sys.argv[1], "wb") as f:
  f.write(address_book.SerializeToString())
