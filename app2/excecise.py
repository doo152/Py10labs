import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password =  "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
word = input("Input a word: ")

#def check_similar_word(wd): 
q = cursor.execute("select * from Dictionary")
data = cursor.fetchall()
dict = []

# get words list from dictionary
for d in data:
    (k,v) = d
    
    dict.append(k)
# check if the word is in the dictionary
check = [w for w in dict if w == word or w == word.title() or w == word.upper() or w == word.lower()]

# find a similar word if the word is not in the dictionary
if not check:
    similar_word = get_close_matches(word.lower(), dict)[0]
    yn = input("Do you mean %s instead? Enter Y for yes, or N for no: " % similar_word)
    if yn == 'Y' or yn == 'y':
        word = similar_word
    elif yn == 'N' or yn == 'n':
        print("Sorry, wrong word")
    else: 
        print("What??")
        

sql = "SELECT * FROM Dictionary where Expression = '%s' " % word
query = cursor.execute(sql)

results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else: 
    print("Not found!")
