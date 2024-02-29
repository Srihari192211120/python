def findSeason(month, date):
    if(month == 'Mar' and date >= 20 or month == 'Apr' or month == 'May' or month == 'Jun' and date >= 21):
        print("the season is Summer")
    if(month == 'Dec' and date >= 21 or month == 'Jan' or month == 'Feb' or month == 'Mar' and date < 20):
        print("the season is Winter")
    if(month == 'Jun' and date >= 21 or month == 'Jul' or month == 'Aug' or month == 'Sep' and date <= 21):
        print("the season is Spring")
    if(month == 'Sep' and date >= 22 or month == 'Oct' or month == 'Nov' or month == 'Dec' and date <= 20):
        print("the season is Fall")


month_g = input("enter month: ")
date = int(input("enter date: "))

month = month_g[:3].capitalize()

findSeason(month,date)
