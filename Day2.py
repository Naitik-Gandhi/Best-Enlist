Python 3.9.5 

>>> print("30 days 30 hour challenge")
30 days 30 hour challenge

>>> print('30 days 30 hour challenge')
30 days 30 hour challenge

>>> Hours = "thirty" print(Hours)
SyntaxError: invalid syntax
  
>>> Hours = "thirty"
>>> print(Hours)
thirty

>>> Days = "Thirty days"
>>> print(Days[0])
T

>>> print(Days[4])
t

>>> Challenge = "I will win"
>>> print(Challenge[7:10])
win

>>> print(len(Challenge))
10

>>> print(Challenge.lower())
i will win

>>> a = "30 Days"
>>> b = "30 hours"
>>> c = a + b
>>> print(c)
30 Days30 hours

>>> c = a + ' ' + b
>>> print(c)
30 Days 30 hours

>>> text = "Thirty days and Thirty hours"
>>> x = text.casefold()
>>> print(x)
thirty days and thirty hours

>>> x = 'DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU.'
>>> print(x)
DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU.

>>> a = x.casefold()
>>> print(a)
don’t trouble trouble until trouble troubles you.

>>> txt = "DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
>>> a = txt.isalpha()
>>> print(a)
False

>>> a = txt.isalnum()
>>> print(a)
False

>>> a = txt.capitalize()
>>> print(a)
Don’t trouble trouble until trouble troubles you.

>>> a = txt.casefold()
>>> print(a)
don’t trouble trouble until trouble troubles you.

>>> a = txt.find('t')
>>> print(a)
-1

>>> a = txt.find('a')
>>> print(a)
-1

>>> a = txt.find('T')
>>> print(a)
4

>>> txt = ('TutorialDay2')
>>> a = txt.isalnum()
>>> print(a)
True

>>> a = txt.isalpha()
>>> print(a)
False
