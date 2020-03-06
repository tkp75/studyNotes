#!/usr/bin/env python3

'''
Given a string containing only square brackets, [], you must check whether the brackets are balanced or not. The brackets are said to be balanced if, for every opening bracket, there is a closing bracket.

You will write your code in the check_balance() function, which returns True if the brackets are balanced and False if they are not.

For an empty string, the function will return True.

For the sake of simplicity, you can assume that the string will not contain any other characters.

[[[[]]]]  [][][][]  [[]]]]][[  ][
Balanced  Balanced  Unbalanced Unbalanced

Sample Input #
"[[[[][]]]]"

Sample Output #
True
'''

def check_balance(brackets): # The argument is a string
  sum=0
  for i in range(len(brackets)):
    if brackets[i] == "]":
      sum-=1
    elif brackets[i] == "[":
      sum+=1
    else:
      print("ERROR")
      break
    #print(str(i)+"->"+brackets[i])
    if sum < 0:
      break
  if sum != 0:
      return False
  return True

print("Balanced(\"\"): "+str(check_balance("")))
print("Balanced(\"][\"): "+str(check_balance("][")))
