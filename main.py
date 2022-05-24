# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(wd1, wd2):
        """accept two strings, and determine if they are anagrams.""" 
        if sorted(wd1) == sorted(wd2): 
            return True
        else: 
            return False

print(find_anagrams('hello', 'world'))
print(find_anagrams('racecar', 'carrace'))

