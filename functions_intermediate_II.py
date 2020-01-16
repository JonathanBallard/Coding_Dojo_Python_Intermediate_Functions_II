import random
import math
#Functions Intermediate II


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#Section 1 - Update Values in Dictionaries and Lists
#1
x[1][0] = 15

#2
students[1]['last_name'] = 'Bryant'

#3
sports_directory['soccer'][0] = 'Andres'

#4
z[0]['y'] = 30


#Section 2 - Iterate Through a List of Dictionaries


def iterateDictionary(list):
    for i in range(0,len(list), 1):
        for key, value in list[i].items():
            print(key,value)
            


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#Section 3 - Get Values From a List of Dictionaries
def iterateDictionary2(key_name, list):
    for i in range(len(list)):
        print(list[i][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print('LINE BREAK')
print('LINE BREAK')
print('LINE BREAK')
print('LINE BREAK')
print('LINE BREAK')
#Section 4 - Iterate Through A Dictionary with List Values

def printInfo(some_dict):
    count = 0
    for key, value in some_dict.items():
        print(len(value), key)
        for i in value:
            count += 1
            print(i)
    

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)














