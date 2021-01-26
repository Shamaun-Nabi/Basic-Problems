dict_months = {"January":31, "February":28, "March":31,
"April":30, "May":31, "June":30, "July":31,
"August":31, "September":30, "October":31,
"November":30, "December":31}
print(dict_months)

user_input=input("Enter Your Month's Name \n")
if user_input in dict_months.keys():
    # x=dict_months[user_input]
    # print(f"{x} days")
    print(f"{dict_months[user_input]} days")
else:
    print("Not a Valid Name")