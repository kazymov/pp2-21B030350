#python-RegEx:

"""
$ -Ends with->"planet$"
^ -Starts with->"^hello"
. -Any character (except newline character)->"he..o"
[] -A set of characters->"[a-m]"
\ -Signals a special sequence (can also be used to escape special characters)->"\d"
* -Zero or more occurrences->"he.*o"
+ -One or more occurrences->"he.+o"
? -Zero or one occurrences->"he.?o"
{} -Exactly the specified number of occurrences->"he.{2}o"
| -Either or->"falls|stays"
() -Capture and group
"""

"""#1-search
import re 

txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)
if x:
    print("Yes")
else:
    print("No")
    """


"""#2-The findall() function returns a list containing all matches.
import re

txt = "The rain in Spain"
x = re.findall("rai", txt)
print(x)
#['rai']"""



"""#3
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#The first white-space character is located in position: 3"""


"""#4
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#['The', 'rain', 'in', 'Spain']"""