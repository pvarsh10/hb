# Python program to demonstrate 
# Creation of Set in Python

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with 
# the use of a String
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

# Creating a Set with
# the use of Constructor
# (Using object to Store String)
String = 'GeeksForGeeks'
set1 = set(String)
print("\nSet with the use of an Object: " )
print(set1)

# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

# Creating a Set with
# the use of a tuple
t=("Geeks","for","Geeks")
print("\nSet with the use of Tuple: ")
print(set(t))

# Creating a Set with
# the use of a dictionary
d={"Geeks":1,"for":2,"Geeks":3}
print("\nSet with the use of Dictionary: ")
print(set(d))
