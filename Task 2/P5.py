from P4 import dict

dict1 = dict

with open("filtered.txt", 'w') as f: 
    for i in dict1: 
        name = dict1[i]['name']
        birthyear = dict1[i]['birthyear']
        f.write(f'{i} {name} - {birthyear} \n')