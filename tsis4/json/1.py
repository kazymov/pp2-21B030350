import json

with open("1.json", "r") as fail:
    #"r"- reading mode
    #"w" -write info 
    data = fail.read()
    
    
data = json.loads(data)# load-get data from file
output_data = "Interface status\n"
output_data += "="*540+"\n" #size of "="

obj1 = data["imdata"][0]["l1PhysIf"]["attributes"]
header_of_table = ""
border_between_keyandvalue = ""

lengths_of_cells_of_table = {}


#for right ordering
#для стилировки- все данные были распределены по столбцам 
for key, value in obj1.items():
    length_of_cell = 3
    if len(key) > len(value):
        length_of_cell += len(key)
    else:
        length_of_cell += len(value)
    lengths_of_cells_of_table[key] = length_of_cell
    header_of_table += f'{key}{" "*(length_of_cell - len(key))}'
    border_between_keyandvalue += f'{"-"*(length_of_cell - 3)}{" "*3}'
    
    
output_data += header_of_table + "\n"#for adding names of columns to output stream
output_data += border_between_keyandvalue + "\n" # for adding borders


for obj in data['imdata']:
    obj = obj["l1PhysIf"]["attributes"]
    data_to_print = ""
    # for loop in array
    
    for key, value in obj.items():
        data_to_print += f"{value}{' '*(lengths_of_cells_of_table[key]-len(value))}"
    output_data += data_to_print + "\n"
    
    
    
#print(output_data)
with open("output.txt", "w") as f:
    f.write(output_data)
