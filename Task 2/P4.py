dict = {}
with open("grades.txt") as f:
    for line in f:
       line = line.replace("-", " ")
       line = line.replace(":", " ")
       id,name,grade,birthyear,gender= line.split()
       if (not grade.isdigit()): #or (not birthday.isdigit()) or (not name.isalnum()) or (not gender.isalnum()):
          continue
       dict[id] = {
           'name': name,
           'grade': int(grade),
           'birthyear': int(birthyear),
           'gender': gender
       }
#A
print(dict)

#B # Oldest Users's ID 
oldest = min([i["birthyear"] for i in dict.values()])
id_oldest = list(filter(lambda x: dict[x]["birthyear"] == oldest, dict.keys()))[0]
print("Oldest Users's ID :", id_oldest)

#C # Average Score
sum_score = sum([dict[id]['grade'] for id in dict])
average_score = sum_score/len(dict)
#print("Average Score Is :", average_score)
print("Average Score Is :{:.2f}".format(round(average_score,2)))
print("Average Score Is :{:.2f}".format(round(average_score)))

#D # What Is The Sex Of The User with The Highest Score 
max_score=max([i["grade"] for i in dict.values()])
id_gender= list(filter(lambda x: dict[x]["grade"] == max_score, dict.keys()))[0]
print(dict[id_gender]["gender"])





