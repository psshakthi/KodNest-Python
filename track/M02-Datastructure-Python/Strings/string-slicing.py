# ============================================================

# STRING SLICING - POSITIVE SLICING PRACTICE

# ============================================================

#

# Syntax:

# string[start:stop:step]

#

# Rules:

# 1. start is included

# 2. stop is excluded

# 3. positive step moves from left to right

# 4. If step is not given, default step is 1

#

# Try to predict the output before running each question.

# ============================================================





# ------------------------------------------------------------

# LEVEL 1 - BASIC start:stop

# ------------------------------------------------------------




text = "Python"
print(text[0:3])#Pyt

text = "Programming"
print(text[1:5])#rogr

text = "Developer"
print(text[2:6])#velo

text = "Computer"
print(text[3:7])#pute

text = "Artificial"
print(text[0:4])#Arti
print(text[2:7])#tific

text = "JavaScript"
print(text[4:10])#aScrip

text = "DataScience"
print(text[4:10])#Science
# ------------------------------------------------------------
# LEVEL 2 - MISSING START OR STOP
# ------------------------------------------------------------

text = "PythonProgramming"
print(text[:6])#python

text = "PythonProgramming"
print(text[6:])#Programming

text = "FullStackDeveloper"
print(text[:9])#FullStack

text = "FullStackDeveloper"
print(text[9:])#Developer

text = "MachineLearning"
print(text[:7])#Machine

text = "MachineLearning"
print(text[7:])#Learning


# ------------------------------------------------------------
# LEVEL 3 - POSITIVE STEP
# ------------------------------------------------------------

# 15. Take every second character
text = "ABCDEFGHIJ"
print(text[0:8:2])#
# 16. Take every second character
text = "ABCDEFGHIJ"
print(text[1:9:2])
# 17. Take every third character
text = "ABCDEFGHIJKL"
print(text[0:12:3])
# 18. Take every second character
text = "ABCDEFGHIJKL"
print(text[2:10:2])
# 19. Take every second number
text = "1234567890"
print(text[0:10:2])
# 20. Take every second number starting from index 1
text = "1234567890"
print(text[1:9:2])
# ------------------------------------------------------------
# LEVEL 4 - TRICKY POSITIVE SLICING
# ------------------------------------------------------------
# 21. Take every third character
# text = "Programming"
print(text[0:11:3])
# 22. Take every third character starting from index 1
text = "Programming"
print(text[1:10:3])
# 23. Take every second character
text = "PythonProgramming"
print(text[2:14:2])
# 24. Take every third character
text = "PythonProgramming"
print(text[1:15:3])
# 25. Take every second character
text = "ABCDEFGHIJKLMNO"
print(text[3:13:2])
# 26. Take every third character
text = "ABCDEFGHIJKLMNO"
print(text[2:14:3])
# ------------------------------------------------------------
# LEVEL 5 - INTERVIEW STYLE
# ------------------------------------------------------------
# 27. Predict the output
text = "PythonProgramming"
print(text[0:16:4])
# 28. Predict the output
text = "ABCDEFGHIJKLM"
print(text[1:12:3])
# 29. Predict the output
text = "DataScienceWithPython"
print(text[4:18:2])
# 30. Predict the output
text = "FullStackDevelopment"
print(text[2:19:3])
# ------------------------------------------------------------
# CONCEPT QUESTIONS
# ------------------------------------------------------------
# 31. Compare the following
text = "Python"
print(text[1:5])
print(text[1:5:1])
print(text[1:5:2])
# 32. What happens when start > stop?
text = "Python"
print(text[4:2])
# 33. What happens when start == stop?
text = "Python"
print(text[2:2])#ytho
# 34. What happens when indexes are outside the string?
text = "Python"
print(text[10:20])#yh

text = "Python"
print(text[0:100])#Python
# ------------------------------------------------------------
# BONUS CHALLENGES
# ------------------------------------------------------------

text = "ABCDEFGHIJKLM"
print(text[2:11:3])#CFIL

text = "ProgrammingLanguage"
print(text[3:15:2])#gamnLn

text = "PythonDeveloper"
print(text[1:12:3])#yoel

text = "DataScience"
print(text[0:10:2])#DtSin

text = "FullStackDeveloper"
print(text[4:16:2])#Sakeeo
