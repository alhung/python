# ask user for date in form mm/dd/yy
# validate date in correct range
# convert to form mm dd,yy
# display date

# determine if number is in correct range
def validate(date):
    # slice date to show only digits for month
    act_month = date[0:2]
    # convert string to integer
    num_month = int(act_month)
    # slice date to show only digits for day
    act_day = date[3:5]
    # convert string to integer
    num_day = int(act_day)
    num = '00'
    # determine if month and day are valid dates within specific range
    if num == '00':
        if num_month == 1 or num_month == 3 or num_month == 5\
           or num_month == 7 or num_month == 8 or num_month == 10\
           or num_month == 12:
            if num_day<=0 or num_day>31:
                return 'Error'
            else:
                return time(date)
        elif num_month == 4 or num_month == 6 or num_month == 9\
           or num_month == 11:
            if num_day<=0 or num_day>30:
                return 'Error'
            else:
                return time(date)
        elif num_month == 2:
            if num_day<=0 or num_day>28:
                return 'Error'
            else:
                return time(date)
        elif num_month<=0 or num_month>12:
            return 'Error'
        else:
            return time(date)
        
# convert the date from mm/dd/yy form to mm dd, yy form
def time(date):
    # call convert month function
    new_month = month(date)
    # call remove first dash function
    noDash1 = removeDash1(date)
    # print day
    day = date[3:5]
    # call replace dash to comma function
    comma = changeDash2(date)
    # print year
    year = date[6:10]

    new_date = new_month + noDash1 + day + comma + year
    return new_date

# change numerical value of month to alphabetic word of month
def month(date):
    month_time = date[0:2]
    if '01' in month_time:
        new_month = month_time.replace('01','January')
    elif '02' in month_time:
        new_month = month_time.replace('02','February')
    elif '03' in month_time:
        new_month = month_time.replace('03','March')
    elif '04' in month_time:
        new_month = month_time.replace('04','April')
    elif '05' in month_time:
        new_month = month_time.replace('05','May')
    elif '06' in month_time:
        new_month = month_time.replace('06','June')
    elif '07' in month_time:
        new_month = month_time.replace('07','July')
    elif '08' in month_time:
        new_month = month_time.replace('08','August')
    elif '09' in month_time:
        new_month = month_time.replace('09','September')
    elif '10' in month_time:
        new_month = month_time.replace('10','October')
    elif '11' in month_time:
        new_month = month_time.replace('11','November')
    elif '12' in month_time:
        new_month = month_time.replace('12','December')
    return new_month

# remove first dash
def removeDash1(date):
    dash1 = date[2:3]
    if '/' in dash1:
        no_dash1 = dash1.replace('/',' ')
    return no_dash1

# change second dash to comma
def changeDash2(date):
    dash2 = date[5:6]
    if '/' in dash2:
        replace_dash = dash2.replace('/',', ')
    return replace_dash

# get date from user and display date in new form
def main():
    date = input('Enter a date(mm/dd/yy): ')
    valid = validate(date)
    print(valid)

# call main function
main()
