# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4


from asyncore import write
from fileinput import close


path = "file.txt"
data = open(path,"r+",encoding="utf-8")
new_list=[]
for line in data:
    new_list.append(line.strip())
print(new_list)
for i in new_list:
    str_temp=i
    int_temp=i[-1]
    if int(int_temp)>4:
        str_temp=str_temp.upper()
        data.write(f"{str_temp}\n")
    else:
        data.write(f"{str_temp}\n")
    data.close   
