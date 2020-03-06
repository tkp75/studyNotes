#!/usr/bin/env python3

#5#
traffic_light = {"Green": "Go", "Yellow": "Wait", "Red": "Stop"}
entry = traffic_light.popitem()
print(entry)

#7#
string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = []
for s in string_list:
  if len(s) < 5:
    result.append(len(s))
print(result)

#c)
string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = [len(s) for s in string_list if len(s) < 5]
print(result)

