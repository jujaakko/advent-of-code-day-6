# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:13:44 2020

@author: Juhana
"""

line2 = ""  
unique_characters = "" 
group_answers = [] 
i = 0


"""
Part 1
"""

with open(r"C:\Users\Juhana\Desktop\input6.txt", 'r') as file: #luetaan annettu tiedosto ja muokataan ne yksittäisiksi passiriveiksi
    #answers = [file.readline() for line in file]
    
    for line in file:
            line = line.strip()
            if line == "":
                unique_characters = set(line2)
                unique_characters_count = len(unique_characters)
                group_answers.append(unique_characters_count)
                line2 = ""
                continue
            line2 = line2 + line.strip()


unique_characters = set(line2)
unique_characters_count = len(unique_characters)
group_answers.append(unique_characters_count)
       
    
#print(sum(group_answers))



"""
Part 2
"""

group_member_counter = 0
ok_answers = 0
all_group_answers = []
line2 = ""

with open(r"C:\Users\Juhana\Desktop\input6.txt", 'r') as file: #luetaan annettu tiedosto ja muokataan ne yksittäisiksi passiriveiksi
    #answers = [file.readline() for line in file]
    
    for line in file:
        line = line.strip()
        if line == "":
                unique_characters = set(line2)
                for unique_character in unique_characters:
                    if line2.count(unique_character) == group_member_counter:
                        ok_answers = ok_answers+1
                all_group_answers.append(ok_answers)
                line2 = ""
                group_member_counter = 0
                ok_answers = 0
                continue
        line2 = line2 + line.strip()
        group_member_counter = group_member_counter + 1

print(line2, group_member_counter)

print(sum(all_group_answers))

ok_answers = 0
unique_characters = set(line2)
for unique_character in unique_characters:    
    if line2.count(unique_character) == group_member_counter:
        print(unique_character)
        ok_answers = ok_answers+1
all_group_answers.append(ok_answers)

print(sum(all_group_answers))