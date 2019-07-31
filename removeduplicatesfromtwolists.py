#change this code so it can receive n lists (probably easier to do in haskell)
# note: this is easier to do with sets


import copy

def removedups(list1,list2):
    initiallist1 = copy.deepcopy(list1)
    commonList = []
    for element in initiallist1:
        if element in list2:
            list1.remove(element)
            list2.remove(element)
            commonList.append(element)
    list1.sort()
    list2.sort()
    commonList.sort()
    return list1,list2,commonList

#test
list1 = ['b','a','d']
list2 = ['a','b','c']
print(removedups(list1,list2))


phpfpm = ['make','php5','php-apc','php5-curl','php5-dev','php5-fpm','php-pear','python-simpl*8/ejson',]
apache = ['php5','php5-dev','make','php-apc', 'php-pear', 'php5-curl', 'php5-mcrypt', 'php5-memcached', 'php5-suhosin',]
print(removedups(phpfpm,apache))
