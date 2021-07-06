# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# Change the value 10 in x to 15.  Once you're done, x = [ [5,2,3], [15,8,9] ].
def replace10inSubarrays(someList):
    for z in range(0, len(someList), 1):
        for y in range(0, len(someList[z]), 1):
            if(someList[z][y] == 10):
                someList[z][y] = 15
    return someList
print(replace10inSubarrays(x))            

# Change the last_name of the first student from 'Jordan' to 'Bryant'
def changeLastNameOfFirst(someListOfDictionaries):
    someListOfDictionaries[0]['first_name'] = 'Bryant'
    return someListOfDictionaries
newDictionary = changeLastNameOfFirst(students)
print(newDictionary)

# In the sports_directory, change 'Messi' to 'Andres'
def changeMessiToAndres(someDictionary):
    someDictionary['soccer'][0] = 'Andres'
    return someDictionary
testDictionary = changeMessiToAndres(sports_directory)
print(testDictionary)

z = [ {'x': 10, 'y': 20} ]
# Change the value 20 in z to 30
def change20To30(someListOfDictionaries):
    someListOfDictionaries[0]['y'] = 30
    return someListOfDictionaries
test2Dictionary = change20To30(z)
print(test2Dictionary)


# 2. Iterate through a list of Dictionaries 
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key and the 
# associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) will return
# first_name - Michael, last_name - Jordan [... each on a new line]
def iterateDictionary(listOfDictionaries):
    key1 = 'first_name'
    key2 = 'last_name'
    for i in range(0, len(listOfDictionaries), 1):
        print(key1 + " - " + listOfDictionaries[i][key1] + ", " + key2 + " - " + listOfDictionaries[i][key2])
iterateDictionary(students)        

# 3 Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of 
# dictionaries and a key name, the function prints the value stored in that key for 
# each dictionary. For example, iterateDictionary2('first_name', students)
# should output:
#     Michael
#     John
#     Mark
#     KB
# And iterateDictionary2('last_name', students) should output:
#     Jordan
#     Rosales
#     Guillen
#     Tonel
def iterateDictionary2(someKey, someList):
    for i in range(0, len(someList), 1):
        print(someList[i][someKey])
iterateDictionary2('first_name', students)

# 4 Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are 
# all lists, prints the name of each key along with the size of its list, and then 
# prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# 7 LOCATIONS
# San Jose [...all locations]
def printInfo(someDictionary):
    listOfKeys = list(someDictionary.keys())
    for i in range(0, len(listOfKeys), 1):
        thisKey = listOfKeys[i]
        numberOfValuesForKey = len(dojo[thisKey])
        print(numberOfValuesForKey, thisKey.upper())
        for j in range(0, len(someDictionary[thisKey]), 1):
            print(someDictionary[thisKey][j])
printInfo(dojo)