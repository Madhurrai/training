def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year=1990):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30

def date_value(day ,month, year):
    value=0
    y=year-1
    # total days elapsed till the end of previous year
    value = y * 365 + y//4  - y//100 + y//400
    # add total days passed till previous month of this year
    m=1
    while m<month:
        #print(f'Adding {days_in_month(m,year)} for {m}/{year}')
        value+= days_in_month(m,year)
        m+=1
    #add days of this month
    value+=day
    return value
def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff
def calendar(month,year):
    startDay=date_to_week_day(1,month,year)
    week=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    days=days_in_month(month,year)
    for i in week:
        print(i,end=" ")
    print()
    d=1
    i=0
    while(d<=days):
        if(i==0):
            print(startDay*4*" ",end="")
            i+=1
        elif(i==1):
            startDay=0
            i+=1
        for j in range(startDay*4,28,4):
            if(d<10):
                print(d,end="   ")
            else:
                print(d,end="  ")
            d+=1
        print()
calendar(9,2023)