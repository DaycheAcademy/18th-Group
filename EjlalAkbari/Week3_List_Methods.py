months = ['january', 'february', 'march', 'april', 'may',
          'june','july', 'august', 'september', 'october', 'november']
print(months)
# list.append() --> add an item to the end of the list
months.append('december')
print(months)
# list.count() --> Return the number of times x appears in the list
print(months.count('may'))
months.append('may')
print(months.count('may'))
# list.reverse () --> reverse the list
months.reverse()
print(months)
# list.sort() --> sort the list
months.sort()
print(months)
# list.pop() --> remove the item from the end of the list
months.pop() # --> by executing this line the september will be removed from months list
print(months)
# list.clear() --> remove all items from the
months.clear()
print(months)




# list.index() -->
# print(list.index('july'))
