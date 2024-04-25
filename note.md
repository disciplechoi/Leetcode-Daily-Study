## 4/25/24
* dictionaries 
- Dictionaries are used to store data values in key:values pairs.
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

* collections.defaultdict
- default type should be defined.
- collections.defaultdict(int)
- my_dict = collections.defaultdict(list)
my_dict = {
    'key1'= [1,2,3,4]
    'key2'= [a,b,c,d,e]
}
-my_dict.values() -> ([[1,2,3,4],[a,b,c,d,e]])

* get char from string
for char in s:
    print(char)