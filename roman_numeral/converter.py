# attempt 1

# class dict:
#   def __init__(self):
#     self._storage = { }

#   # add a key value?  
#   def add_pair(self, key, value):
#     self[key] = value
#     #return {key: value}?
  
#   def get_value(self, key, value):
#     if key in self:
#       print(value)
    



# attempt 2 

# part I: write a function to convert from normal numbers to Roman Numerals

# func(num) => rnum   
# input num
# ouput rnum

#wrong  assumption?
# find num that matches 
# send corresponding rnum
# ?dictionary  -> jumped to data storage
# https://realpython.com/python-data-structures/


# def converter(num):
#   # rules?
#   # inefficient to store data
#     # if 1 => I                               
#     # if 2 => II   
#     # if 3 => III  
#     # if 4 => IV    if num = 4 , then IV   
    
#     # if 5 => V
#     # if 6 => VI     if num > 5, then VI
#     # if 7 => VII
#     # if 8 => VIII
#     # if 9 => 

#   rnum = " "
#   return rnum


# def converter(num):
#   if num == 1:
#     rnum = "I"
#     return rnum

# print(converter(1))






# attempt 3

# part I: write a function to convert from INT to STR

# INT to STR
# 1 - I     11 - XI   
# 2 - II
# 3 - III
# 4 - IV    14 - XI
# 5 - V     15 - XV
# 6 - VI    16 - XVI
# 7 - VII
# 8 - VIII
# 9 - IX    19 - XIX    29 - XXI     39 - XXIX   49 - XLIX
# 10 - X    20 - XX     30 - XXX     40 - XL     50 - L


# #rules?

# def convert(num):
#   return "II"



# part 2: write a function to convert from STR to INT




# solution from https://codingdojo.org/solution/KataRomanNumeralsAsReadableAsWeCouldMakeIt/

def convert(num):
  numeral_dict = {
       'ones':     ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        'tens':     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        'hundreds': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        'thousands': ['', 'M', 'MM', 'MMM'],
  }

# dictionary with array 


  s = []   # list
  for index in ['ones', 'tens', 'hundreds', 'thousands']:
    num, remainder = divmod(num, 10)    #num/10
    s.insert(0, numeral_dict[index][remainder])  #?
    print(s)
    print(index, remainder)
  return ''.join(s)

# divmod(no to divide, # divide by) - returns tuple with quotient and remiander
# <separator>.join()     can be empty

# convert(3)  -> ? 0, 3  ?
# ['III']
# ones 3
# ['', 'III']
# tens 0
# ['', '', 'III']
# hundreds 0
# ['', '', '', 'III']
# thousands 0

# convert(49)  -> 49/10 -> 9 reminder
# ['IX']
# ones 9
# ['XL', 'IX']      
# tens 4               ?  4
# ['', 'XL', 'IX']
# hundreds 0
# ['', '', 'XL', 'IX']
# thousands 0

convert(116)
# ['VI']
# ones 6
# ['X', 'VI']
# tens 1
# ['C', 'X', 'VI']
# hundreds 1
# ['', 'C', 'X', 'VI']
# thousands 0



# attempt #


# part I: write a function to convert from n to r


# part 2: write a function to convert from r to n