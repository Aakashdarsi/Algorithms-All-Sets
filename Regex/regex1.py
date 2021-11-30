# re is used for gegular expresesions
import re
 #regular expressions module Used to work with regular expressions
test = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''
#There are many methods in regular expresssions in python
# SOme are like findall, search, split, sub, finditer
 #r is a meta character which specifies the raw string

# In regular expression we use raw strings as a base rule
pattern = re.compile(r'fass')
matches = re.finditer(pattern)
for i in matches:
    print(i)