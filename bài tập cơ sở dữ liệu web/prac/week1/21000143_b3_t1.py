def find_how_many_day_in_month(month):
    dict_month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    return dict_month[month]

print("How many days in january?",find_how_many_day_in_month(1))