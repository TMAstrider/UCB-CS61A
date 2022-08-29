# def generate_subsets():
#     """
#     >>> subsets = generate_subsets()
#     >>> for _ in range(3):
#     ... print(next(subsets))
#     ...
#     [[]]
#     [[], [1]]
#     [[], [1], [2], [1, 2]]
#     """
#     # x = [[]]
#     # yield x
#     # y = 0
#     # while True:
#     #     y += 1
#     #     yield x + [[y] + _ for _ in subsets]
#     subsets = [[]]
#     n = 1
#     while True:
#         yield subsets
#         subsets = subsets + [s + [n] for s in subsets]
#         n += 1
        
# subsets = generate_subsets()
# for _ in range(4):
#     print(next(subsets))

# def sum_paths_gen(t):
#     """
#     >>> t1 = tree(5)
#     >>> next(sum_paths_gen(t1))
#     5
#     >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
#     >>> sorted(sum_paths_gen(t2))
#     [6, 7, 10]
#     """
#     if is_leaf :
#         yield label(t)
#     for b in branches(t):

#         for s in sum_paths_gen(b):
#             yield s + label(b)


# def collect_words(t):
#     """Return a list of all the words contained in the tree where the value of each node in
#     the tree is an individual letter. Words terminate at the leaf of a tree.
#     >>> collect_words(greetings)
#     ['hi', 'hello', 'hey']
#     """
#     if is_leaf(t):
#         return [label(t)]
#     words = []
#     for branch in branches(t):
#         words += [label(t) + word for word in collect_words(branch)]
#     return words

# print('a' + 'b')


# def make_withdraw(balance, password):
#     """Return a password-protected withdraw function.

#     >>> w = make_withdraw(100, 'hax0r')
#     >>> w(25, 'hax0r')
#     75
#     >>> error = w(90, 'hax0r')
#     >>> error
#     'Insufficient funds'
#     >>> error = w(25, 'hwat')
#     >>> error
#     'Incorrect password'
#     >>> new_bal = w(25, 'hax0r')
#     >>> new_bal
#     50
#     >>> w(75, 'a')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     40
#     >>> w(20, 'n00b')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
#     >>> w(10, 'l33t')
#     "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
#     >>> type(w(10, 'l33t')) == str
#     True
#     """
#     "*** YOUR CODE HERE ***"
#     i = 0
#     def withdraw(amount, password_input):
#         # nonlocal i
        
#         lst = []
#         if len(lst) == 3 :
#                 return "Frozen account. Attempts: " + str(lst)
#         if password_input != password:
#             lst += [password_input]
            
#             # i += 1
#             # return 
#             #     return "Frozen account. Attempts: " + str(lst)
#             return 'Incorrect password' , withdraw

#         nonlocal balance
#         if password == password_input:
#             if balance < amount:
#                 return 'Insufficient funds'
#             balance -= amount
#             return balance
#     return withdraw

# def repeated(t, k):
#     """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
#     if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
#     in the first.

#     >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
#     >>> repeated(s, 2)
#     9
#     >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
#     >>> repeated(s2, 3)
#     8
#     >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
#     >>> repeated(s, 3)
#     2
#     >>> repeated(s, 3)
#     5
#     >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
#     >>> repeated(s2, 3)
#     2
#     """
#     assert k > 1
#     "*** YOUR CODE HERE ***"
#     cnt = 0
#     flag = 0
#     tmp = next(t)
#     for i in t :
#         if i == tmp and flag == 0 :
#             cnt += 2
#             flag = 1
#             if cnt == k :
#                 return tmp
#         if i == tmp and flag == 1:
#             cnt += 1 
#             if cnt == k :
#                 return tmp
#         tmp = i
# s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
# repeated(s, 2)


# def permutations(seq):

#     if len(seq) == 1:
#         yield seq
#     # if len(seq) == 1:
#     #     yield seq
#     else:
#         for element in permutations([x for x in seq if x != seq[0]]):
#             for k in range(len(element) + 1):
#                 yield element[:k] + [seq[0]] + element[k:]

# print(sorted(permutations([1, 2, 3])))


# from tkinter import N


# def hailstone(n):
#     """
#     >>> for num in hailstone(10):
#     ...     print(num)
#     ...
#     10
#     5
#     16
#     8
#     4
#     2
#     1
#     """
#     "*** YOUR CODE HERE ***"
#     yield n
#     while True:
#         if n % 2 == 0:
#             n //= 2
#             # yield n
#             yield n
#         elif n % 2 == 1 and n != 1:
#             n = 3 * n + 1
#             yield n

# for num in hailstone(10):
#     print(num)


# print(89466489648964896489654)


# class Car(object):
#     num_wheels = 4
#     gas = 30
#     headlights = 2
#     size = 'Tiny'

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.color = 'No color yet. You need to paint me.'
#         self.wheels = Car.num_wheels
#         self.gas = Car.gas

#     def paint(self, color):
#         self.color = color
#         return self.make + ' ' + self.model + ' is now ' + color

#     def drive(self):
#         if self.wheels < Car.num_wheels or self.gas <= 0:
#             return 'Cannot drive!'
#         self.gas -= 10
#         return self.make + ' ' + self.model + ' goes vroom!'

#     def pop_tire(self):
#         if self.wheels > 0:
#             self.wheels -= 1

#     def fill_gas(self):
#         self.gas += 20
#         return 'Gas level: ' + str(self.gas)

# deneros_car = Car('Tesla', 'Model S')
# Car.drive()


# disc 07
# disc 07
# disc 07

# class Email:
#     """Every email object has 3 instance attributes: the
#     message, the sender name, and the recipient name.
#     """
#     def __init__(self, msg, sender_name, recipient_name):
#         pass
#         self.msg = msg
#         self.sender_name = sender_name
#         self.recipient_name = recipient_name

# class Server:
#     """Each Server has an instance attribute clients, which
#     is a dictionary that associates client names with
#     client objects.
#     """
#     def __init__(self):
#        self.clients = {}

#     def send(self, email):
#         """Take an email and put it in the inbox of the client
#         it is addressed to.
#         """
#         client = self.clients[email.recipient_name]
#         clinet.receive(email)

    
#     def register_client(self, client, client_name):
#         """Takes a client object and client_name and adds it
#         to the clients instance attribute.
#         """
#         client = self.clients[client_name]


# class Client:
#     """Every Client has instance attributes name (which is
#     used for addressing emails to the client), server
#     (which is used to send emails out to other clients), and
#     inbox (a list of all emails the client has received).
#     """
#     def __init__(self, server, name):
#         self.inbox = []

#         self.server = server
#         self.name = name
#         self.server.register_client(self, self.name)

#     def compose(self, msg, recipient_name):
#         """Send an email with the given message msg to the
#         given recipient client.
#         """
#         email = Email(msg, self.name, recipient_name)
#         self.server.send(email)

#     def receive(self, email):
#         """Take an email and add it to the inbox of this
#         client.
#         """
#         self.inbox.append(email)

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
class B(A):
    def f(self):
        return 4

x, y = A(), B()
print(x.f())
print(B.f())
