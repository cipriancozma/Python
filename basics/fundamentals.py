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
