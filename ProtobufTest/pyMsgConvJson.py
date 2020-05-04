#! /usr/bin/env python

from __future__ import print_function
import Addressbook_pb2 
import sys
from google.protobuf import json_format
import json

address_book = Addressbook_pb2.AddressBook()

if len(sys.argv) != 2:
  print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
  sys.exit(-1)

address_book = Addressbook_pb2.AddressBook()

# Read the existing address book.
with open(sys.argv[1], "rb") as f:
  address_book.ParseFromString(f.read())

message=address_book
json_string = json_format.MessageToDict(message)

with open('testdata.json', 'w') as x:
	json.dump(json_string,x)


