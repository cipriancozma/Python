# Fundamental Data Types
# int and float
# print(type(2 + 4))  # int -> 6
# print(type(2 / 4))  # float -> 0.5

# str
# print(type("hi hello"))
long_string = '''
WWW
0 0
---
'''
# print(long_string)

# bool
isValid = True
# print(type(isValid))

# list
li = [1, 2, 3, 5, True, 'a']
# print(li)

# None
a = None
# print(type(a))

# Dictionaries
dictionary = {
    'a': 1,
    'b': 2
}
# print(dictionary['a'])
# print(dictionary.values())

# Tuples - immutable lists
my_tupple = (1, 2, 3, 4, 5)
# print(my_tupple[1])

# Sets
my_set = { 1, 2, 3, 4, 5, 6, 5}
list_set = [1, 2, 2, 3, 4, 5]
# print(set(list_set))
# print(my_set)

# math functions
# print(round(3.2))
# print(abs(-3))

# operator precedence
# print((5 + 4) * 10 / 2) # 45
# print(((5 + 4) * 10) / 2) # 45
# print((5 + 4) * (10 / 2)) # 45
# print(5 + (4 * 10) / 2) # 25
# print(5 + 4 * 10 // 2) # 25

# binary
# print(bin(256))

# string indexes
selfish = '01234567'
# print(selfish[1:8:1])

#methods
# print(len('helloooo'))

quote = 'to be or not to be'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.replace('be', 'me'))

# list methods
cart = ['notebooks', 'toys', 'grapes', 'hello']
# print(cart[0:2])

basket = [1, 2, 3, 4, 5]

# adding
basket.append(6)
# print(basket)
basket.insert(2, 8)
# print(basket)
basket.extend([200])
# print(basket)

# removing
basket.pop()
# print(basket)
basket.remove(6)
# print(basket)
# basket.clear()
# print(basket)

# print(basket.index(2))

basket_letters = ['a', 'b', 'c', 'd', 'e', 'c']

# print(basket_letters.index('d'))

# print('e' in basket_letters)

# print(basket_letters.count('c'))

# basket_letters.sort() # I can use also sorted() - it produces a new array
# print(basket_letters)

# sort and reverse
new_list = sorted(basket_letters)
new_list.reverse()
# print(new_list)

# print(list(range(1, 100)))

sentence = ' '
new_sentence = sentence.join(['hello', 'my', 'name', 'is', 'ciprian'])
# print(new_sentence)

# list unpacking
a, b, c, *other = [1, 2, 3, 4, 5, 6]
# print(a)
# print(other)

# dictionary methods
user = {
    'name': 'ciprian',
    'greet': 'hello'
}

# print(user.get('age')) # instead of throwing an error by putting the age directly user['age'], if the user does not contain the age key it will print None

# print('size' in user.keys())
# print('hello' in user.values())
# print(user.items())
# print(user.clear())

# tuple methods
new_tuple = (4, 6, 8, 10)
# tuple_var = new_tuple[1:2]
# print(tuple_var)
# print(new_tuple.count(4))
# print(new_tuple.index(4))

# set methods
set_1 = { 1, 2, 3, 4, 5 }
set_2 = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(set_2))
# print(my_set.discard(5))
# print(set_1.difference_update(set_2))
# print(set_1)
# print(set_1.intersection(set_2))
# print(set_1.isdisjoint(set_2))
# print(set_1.union(set_2))
# print(set_1.issubset(set_2))
# print(set_1.issuperset(set_2))
