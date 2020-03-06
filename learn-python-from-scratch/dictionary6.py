#!/usr/bin/env python3

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print (phone_book)

cersei = phone_book.pop("Cersei")
print (phone_book)
print (cersei)

# Removes and returns an arbitrary pair as a tuple
lastAdded = phone_book.popitem()
print (lastAdded)
