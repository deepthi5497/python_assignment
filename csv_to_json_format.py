import xlrd
import datetime
import json

# reading the data from excel file "Input_excel.xlsx"

wb = xlrd.open_workbook("Input_excel.xlsx")
sheet = wb.sheet_by_index(0)
col_name_dict = {}
for value in range(sheet.ncols):
    col_name_dict[value] = sheet.cell_value(0, value)
num_of_row = sheet.nrows - 1
print(num_of_row)
row_list =[]
for i in range(sheet.nrows):
    row_dict = {}
    if i != 0:
        for j in range(sheet.ncols):
            row_dict[col_name_dict[j]] = sheet.cell_value(i, j)
        row_list.append(row_dict.copy())

print(row_list)

# creating json format for fields such as Name, age, Courses, Date of birth

courses = ""
json_collective_list = []

for row in row_list:
    # print(row)
    json_dict = {}
    for k, v in row.items():
        if v != "":
            if k == "Courses":
                courses = str(v)
                json_dict[k] = courses.split(",")
            elif k == "Name" or k == "DOB":
                json_dict[k] = v
            elif k == "Age":
                json_dict[k] = int(v)
    # print(json_dict)
    if json_dict:
        json_collective_list.append(json_dict)
print(json_collective_list)


# creating json format for fields such as phone type , phone numbers , siblings types ,sibling names

json_dict1 = {}
json_dict2 = {}
json_ph_list = []

flag = 0
count = 0

json_dict3 = {}
json_dict4 = {}
json_sb_list = []
current_name = ""
prev_name = ""


for row in row_list:
    count += 1
    if row.get('Name') != "":
        current_name = row.get('Name')
    if prev_name != current_name:
        if json_dict1 and json_dict3:
            if flag == 0:
                json_ph_list.append(json_dict1.copy())
                json_sb_list.append(json_dict3.copy())
            flag = 1

            json_dict2["Phone"] = json_ph_list
            json_dict4["Siblings"] = json_sb_list

            for i in json_collective_list:
                if "Phone" not in i.keys():
                    i.update(json_dict2)
                    i.update(json_dict4)
                    break

        json_ph_list = []
        json_sb_list = []

        for k, v in row.items():
            if k == "Phone Type":
                json_dict1["Phone Type"] = v

            if k == "Phone Number":
                json_dict1["Phone Number"] = v

            if k == "Siblings Type" and v != "":
                json_dict3["Siblings Type"] = v

            if k == "Siblings Name" and v != "":
                json_dict3["Siblings Name"] = v

        prev_name = current_name
        json_ph_list.append(json_dict1.copy())
        json_sb_list.append(json_dict3.copy())
    else:
        for k, v in row.items():
            if k == "Phone Type":
                json_dict1["Phone Type"] = v

            if k == "Phone Number":
                json_dict1["Phone Number"] = v

            if k == "Siblings Type" and v != "":
                json_dict3["Siblings Type"] = v

            if k == "Siblings Name" and v != "":
                json_dict3["Siblings Name"] = v

        prev_name = current_name
        json_ph_list.append(json_dict1.copy())
        json_sb_list.append(json_dict3.copy())
        flag = 1

        if num_of_row == count:
            json_dict2["Phone"] = json_ph_list
            json_dict4["Siblings"] = json_sb_list

            for i in json_collective_list:
                if "Phone" not in i.keys():
                    i.update(json_dict2)
                    i.update(json_dict4)
                    break

    # elif count == 6:
    #     json_dict2["Phone"] = json_ph_list
    #     json_dict4["Siblings"] = json_sb_list
    #
    #     for i in json_collective_list:
    #         if "Deepthi" in i.values():
    #             i.update(json_dict2)
    #             i.update(json_dict4)
    #     json_ph_list = []
    #     json_sb_list = []

print(json_collective_list)

# writing the converted json values to a json file "Output_json.json"

final_json_dict = dict()
final_json_dict["Queries"] = json_collective_list

with open("Output_json.json","w") as json_file:
    json.dump(final_json_dict, json_file)
