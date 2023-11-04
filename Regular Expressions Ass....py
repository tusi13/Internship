#!/usr/bin/env python
# coding: utf-8

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# 
# Sample Text- 'Python Exercises, PHP exercises.'
# 
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[6]:


import re
text='Python Exercises, PHP exercises.'
print(re.sub("[ ,. ]",":", text))


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# 
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# 
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[69]:


import pandas as pd
import numpy as np
dict={'SUMMARY':['hello, world!', 'XXXXX test', '123four, five:; six...']}
df=pd.DataFrame(dict)
df['SUMMARY']= df['SUMMARY'].str.replace('[123!.,:X;\s]'," ",regex=True)
df



# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[89]:


import re
text= 'Python and Data Science are good for future'
pattern=re.compile(r'\b\w{4}\b')
print(pattern.findall(text))


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[120]:


import re
text= 'Python and Data Science are good for future abcde'
pattern=re.compile(r'\b\w{3,5}\b')
result=pattern.findall(text)
print(result)


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# 
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist
# 

# In[142]:


import re
text=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for text1 in text:
    print(re.sub(r'([())])','',text1))


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# 
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# 
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[153]:


import re
string=open('C:\Users\Vikash Kumar\Desktop\Sample _Text.txt').read()
new_str=re.sub('[^a-zA-Z0-9\n\.]','',string)
open('output_Sample_text','w').write(new_str)            


# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# 
# Sample text: “ImportanceOfRegularExpressionsInPython”
# 
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[155]:


import re
text='ImportanceOfRegularExpressionsInPython'
print(re.findall('[A-Z][^A-Z]*',text))    


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# 
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[160]:


test_str='RegularExpression1IsAn2ImportantTopic3InPython'
res=re.sub('(\d+)',r' \1',test_str)
print('Output:'+str(res))


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# 
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[161]:


test_str='RegularExpression1IsAn2ImportantTopic3InPython'
res=re.sub('(\d+)',r' \1',test_str)
print('Expected Output:'+str(res))


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# 
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv

# In[165]:


import pandas as pd
data=pd.read_csv(https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv)
print(data)


#  Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[181]:


import re
text='Python is usefull language and its started in 20_feb_1991'
text1="pdasndlds dasdas"
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("text"))
print(text_match('pdasndlds dasdas'))   


# Question 12- Write a Python program where a string will start with a specific number.

# In[184]:


import re
string='9-12345'
string1='52345'
def match_num(string):
    text=re.compile(r'^9')
    if text.match(string):
        return True
    else:
        return False
print(match_num(string))
print(match_num(string1))


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[188]:


import re
ip='192.0168.090.1'
string=re.sub('\.[0]*','.',ip)
print(string)


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# 
# Expected Output- August 15th 1947
# 
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[ ]:





# Question 15- Write a Python program to search some literals strings in a string. 
# 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# 
# Searched words : 'fox', 'dog', 'horse'
# 

# In[199]:


import re
patterns=['fox', 'dog', 'horse']
text= 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print("searching for '%s' in '%s' " % (pattern,text))
    if re.search(pattern,text):
          print('matched')
    else:
          print('Not matched')


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# 
# Searched words : 'fox'
# 

# In[219]:


import re
pattern ='fox'
text='The quick brown fox jumps over the lazy dog.'
match=re.search(pattern,text)
print("Found '%s'in '%s' from %d to %d" %\
      (match.re.pattern,match.string,s,e))



# Question 17- Write a Python program to find the substrings within a string.
# 
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# 
# Pattern : 'exercises'.
# 

# In[1]:


import re
text='Python exercises, PHP exercises, C# exercises'
pattern='exercises'
for match in re.findall(pattern,text):
    print("Found '%s'" %match)


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[2]:


import re
text='Python exercises, PHP exercises, C# exercises'
pattern='exercises'
for match in re.finditer(pattern,text):
    s=match.start()
    e=match.end()
    print("Found ''%s' at %d:%d" % (text[s:e],s,e))
    


# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[3]:


import re
def change_date_formate(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',dt)
dt1="2023-11-04"
print("orginal date in yyyy-mm-dd format:",dt1)
print("New date in dd-mm-yyyy formate:",change_date_formate(dt1))


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# 
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# 
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[6]:


import re
def find_decimal_number(string):
    pattern = re.compile(r'\d+\.\d{1,2}')
    decimal_number=re.findall(pattern,string)
    return decimal_number
text="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output=find_decimal_number(text)
print("Output is :" ,output)
    


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[8]:


import re
text="Write a 70 Python program to separate and print the numbers and their position of a given string."
for m in re.finditer("\d+",text):
    print(m.group(0))
    print("Index position:",m.start())


# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# 
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# 
# Expected Output: 950
# 

# In[21]:


import re
text='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
numeric_value=re.findall(r'\d+',text)
numeric_value=[int(value) for value in numeric_value]
max_value=max(numeric_value)
print(max_value)


# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# 
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# 
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[26]:


import re
def insert_space(text):
    pattern=r'([A-Z][a-z]+)'
    res= re.sub(pattern,r' \1',text)
    res=res.strip()
    return res
text1="RegularExpressionIsAnImportantTopicInPython"
output=insert_space(text1)
print(output)


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[27]:


import re
pattern=r'[A-Z][a-z]+'
text='Python regex to Find Sequences of one Upper case Letter followed by lower case letters'
matches=re.findall(pattern,text)
print(matches)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[28]:


import re
text='Hello hello world world'
def remove_duplicates(text):
    pattern=r'\b(\w+)(\s+\1\b)+'
    result=re.sub(pattern,r'\1',text)
    return result
output=remove_duplicates(text)
print(output)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[ ]:





# Question 27-Write a python program using RegEx to extract the hashtags.
# 
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# 
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[38]:


import re
text='RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <U+00A0><U+00BD><U+00B1><U+0089> "acquired funds" No wo'
def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags
hashtags=extract_hashtags(text)
print(hashtags)


# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# 
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# 
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[55]:


import re

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
output = re.sub(pattern, "", text)

print(output)


# Question 29- Write a python program to extract dates from the text stored in the text file.
# 
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# 
# Note- Store this sample text in the file and then extract dates.
# 

# In[ ]:





# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# 
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# 
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.
# 

# In[57]:


import re

def remove_words(string):

  pattern = re.compile(r'\b\w{2,4}\b')
  modified_string = re.sub(pattern, "", string)
  return modified_string
  text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
output = remove_words(text)
print(output)


# In[ ]:




