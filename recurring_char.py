//recurrig chracters


# Python program to count occurrences
# of a given character
 
# Method that return count of the 
# given character in the string
def count(s, c) :
     
    # Count variable
    res = 0
     
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res
     
     
# Driver code
str= "geeksforgeeks"
c = 'e'
print(count(str, c))
