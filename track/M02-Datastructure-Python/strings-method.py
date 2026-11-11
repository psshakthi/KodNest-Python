# Inbuilt String Methods – Single Program
s = "  kodNest Technologies 123  "


print("Original String:", s) #  kodNest Technologies 123  


# Case conversion methods
print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
print("lower():", s.lower()) #   
print("capitalize():", s.capitalize()) #First Letter will be Capital
print("title():", s.title()) #  
# Inbuilt String Methods – Single Program
s = "  kodNest Technologies 123  "


print("Original String:", s) #  kodNest Technologies 123  


# Case conversion methods
print("upper():", s.upper()) # KODNEST TECNOLOGIES 123
print("lower():", s.lower()) #   
print("capitalize():", s.capitalize()) #  
print("title():", s.title()) #  
print("swapcase():", s.swapcase()) #it swap the lowecase to capital letter and UpperCase to loweracse


# Searching & counting
print("find('Tech'):", s.find("Tech")) #  findind the index value to the word
print("count('o'):", s.count("o")) #


# Replace
print("replace('123', '2025'):", s.replace("123", "2028"))
#


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) #
print("endswith('123  '):", s.endswith("123  ")) #


# Split & Join
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) # 


# Strip spaces
print("strip():", s.strip()) #
print("lstrip():", s.lstrip())# 
print("rstrip():", s.rstrip())#  


# Checking methods
print("isalpha():", s.isalpha())#
print("isdigit():", s.isdigit())#
print("isalnum():", s.isalnum())#


# Length
print("Length of string:", len(s)) #


# Searching & counting
print("find('Tech'):", s.find("Tech")) # 10 it shows index value in word of T
print("count('o'):", s.count("o")) # it count the character inside the quote


# Replace
print("replace('123', '2025'):", s.replace("KodNes", "2025"))
#


# Start & End check
print("startswith('  kod'):", s.startswith("  kod")) #True->if the strings start with kod
print("endswith('123  '):", s.endswith("123  ")) #True->if the strings ends with 123


# Split & Join Split->it splits the string into a list,Join->it joins the list into a string
words = s.split() #
print("split():", words)
print("join():", "-".join(words)) # it joins the list into a string


# Strip spaces
print("strip():", s.strip()) #
print("lstrip():", s.lstrip())# 
print("rstrip():", s.rstrip())#  


# Checking methods
print("isalpha():", s.isalpha())# False -> bcz it is not only store alphabets
print("isdigit():", s.isdigit())#False -> bcz it is not only store numbers
print("isalnum():", s.isalnum())#False -> bcz it is not only store alphabets or numbers but it have space between the alpha and number
print("Hello123".isalnum()) #True -> bcz it os only alpha and numbers without thw space btw  number and alpha
print("Hello".isalnum()) #True-> bcz it os only alpha atlaest 
# Length
print("Length of string:", len(s))

s9= "hello"
print(id(s9), s9)

s11 = "hello"
print(s11)
s12 = (s11 + "World")
print(id(s12),s12)

s13 = "Python"
s14 = "python"
print(id(s13), s13)
print(id(s14), s14)
print(s13 == s14)
print(s13 is s14)

print("----String Slicing----")
s15 = "Python"
print(s15)
print(s15[2])
print(s15[1:4])
print(s15[0:5])
print(s15[ : ])
print(s15[ :4])
print(s15[2:])
print(s15[0::1])
print(s15[3:5:3])


