#change this code so it can receive n lists (probably easier to do in haskell)
# note: this is easier to do with sets


def removedups(list1, list2):
    set1, set2 = set(list1), set(list2)
    commonSet = set1 & set2
    return sorted(set1 - commonSet), sorted(set2 - commonSet), commonSet

phpfpm = ['make','php5','php-apc','php5-curl','php5-dev','php5-fpm','php-pear','python-simpl*8/ejson',]
apache = ['php5','php5-dev','make','php-apc', 'php-pear', 'php5-curl', 'php5-mcrypt', 'php5-memcached', 'php5-suhosin',]
print(removedups(phpfpm,apache))
