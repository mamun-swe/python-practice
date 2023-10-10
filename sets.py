my_set_1 = set([1, 2, 3, 4])
my_set_2 = set([1, 2, 3, 4, 5, 6, 7, 8])


# Python code to demonstrate addition of tuple to a set.
s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']
 
# adding tuple t to set s.
s.add(t)
 
# adding list l to set s.
s.update(l)
 
print(s)