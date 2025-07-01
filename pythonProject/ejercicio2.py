'''
suit

Spades	↦	3
Hearts	↦	2
Diamonds	↦	1
Clubs	↦	0

rank

Jack	↦	11
Queen	↦	12
King	↦	13

'''
import math
import random


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check ranks
        return self.rank < other.rank


'''Using tuples:

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
'''


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)


'''
Inheritance
Inheritance is the ability to define a new class that is a modified version of an existing class.
When a new class inherits from an existing one, the existing one is called the parent and the 
new class is called the child.
This definition indicates that Hand inherits from Deck; that means we can use methods like 
pop_card and add_card for Hands as well as Decks.
When a new class inherits from an existing one, the existing one is called the parent and 
the new class is called the child.
In this example, Hand inherits __init__ from Deck, but it doesn't really do what
we want: instead of populating the hand with 52 new cards, the init method for Hands
should initialize cards with an empty list.
If we provide an init method in the Hand class, it overrides the one in the Deck class:
'''


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


'''A natural next step is to encapsulate this code in a method called move_cards:'''


def move_cards(self, hand, num):
    for i in range(num):
        hand.add_card(self.pop_card())


deck1 = Deck()
print(deck1)

card1 = Card(3, 13)
print(card1)

hand = Hand('new hand')
print(hand.cards)

# []
print(hand.label)
# 'new hand'
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)


class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    def __str__(self):
        return str(self.radius)

    def __add__(self, other):
        return self.radius + other.radius


c1 = Circle(2)
c2 = Circle(3)
print(c1)
print(c2)
print(c1 + c2)


class Sphere:
    def __init__(self, r):
        self.radius = r

    def volume(self):
        return (4 / 3) * math.pi * math.pow(self.radius, 3)

    def surfarea(self):
        return 4 * math.pi * math.pow(self.radius, 2)


esfera = Sphere(1)
print(esfera.volume())
print(esfera.surfarea())


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surfarea(self):
        return 2 * self.length * self.width + 2 * self.width * self.height + 2 * self.length * self.height

    def __str__(self):
        return f'Length: {self.length} Width: {self.width} Height: {self.height}'

    def __add__(self, other):
        if isinstance(other, Box):
            n_l = self.length + other.length
            n_w = self.width + other.width
            n_h = self.height + other.height
            return Box(n_l, n_w, n_h)

    def __sub__(self, other):
        if isinstance(other, Box):
            n_l = self.length - other.length
            if n_l < 0:
                n_l = 0
            n_w = self.width - other.width
            if n_w < 0:
                n_w = 0
            n_h = self.height - other.height
            if n_h < 0:
                n_h = 0
            return Box(n_l, n_w, n_h)


box1 = Box(3, 4, 5)
print(box1)
box2 = Box(4, 4, 4)
print(box2)
box3 = box1 + box2
print(box3)
print(box1 - box2)

import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    def __str__(self):
        return 'Radius:' + str(self.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius


c1 = Circle(4)
c2 = Circle(5)
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)


class Circle1:
    def __init__(self, radius):
        self.radius = radius
        try:
            if self.radius < 0:
                print('Negative Radius Input: setting radius attribute equal to zero')
                self.radius = 0
        except TypeError:
            print('Type Error for Radius Input: setting radius attribute equal to zero')
            self.radius = 0

    # Place your code here
    # Use these statements to ensure agreement with the answer checker:
    #       print('Negative Radius Input: setting radius attribute equal to zero')
    #       print('Type Error for Radius Input: setting radius attribute equal to zero')

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * pow(self.radius, 2)


c1 = Circle1(-3)
print(c1.radius, c1.area())


class Rectangle:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, z):
        super().__init__(z, z)

    def apratio(self):
        return self.area() / self.perimeter()


sq = Square(3)

print(sq.area(), sq.apratio())

'''
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

Python also has a super() function that will make the child class inherit all the methods 
and properties from its parent:

Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.

Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

In the example below, the year 2019 should be a variable, and passed into the Student class 
when creating student objects. To do so, add another parameter in the __init__() function:

Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

If you add a method in the child class with the same name as a function in the parent class, 
the inheritance of the parent method will be overridden.
'''
