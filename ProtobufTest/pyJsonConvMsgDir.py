#! /usr/bin/env python

from __future__ import print_function
import Addressbook_pb2 
import sys
from google.protobuf import json_format
import json
import glob
import errno

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

json_string = {}
files = glob.glob("/home/yy/fod/jsonfile/*.json")
for name in files:
	try:
		with open(name) as f:
			json_string.update(json.load(f))
	except IOError as exc:
		if exc.errno != errno.EISDIR:
			raise

address_book = json_format.ParseDict(json_string, Addressbook_pb2.AddressBook())

ListPeople(address_book)

with open(sys.argv[1], "wb") as f:
  f.write(address_book.SerializeToString())
