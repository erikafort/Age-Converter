'''
Erika Fortune
10.24.17
Purpose: A program that will ask the user to enter their age convert their age to days, hours, minutes, and seconds.
'''
def getAge():
    age=float(input("Enter your age: "))
    while(age<=0):
        age=float(input("Please enter your real age: "))
    return(age)    
def getDays(age):
    days=age*365
    return(days)
def getHours(age):
    hours=getDays(age)*24
    return(hours)
def getMinutes(age):
    minutes=getHours(age)*60
    return(minutes)
def getSeconds(age):
    seconds=getMinutes(age)*60
    return(seconds)
def main():
    again="y"
    while(again!="quit"):
        age=getAge()
        days=getDays(age)
        hours=getHours(age)
        minutes=getMinutes(age)
        seconds=getSeconds(age)
        print(days)
        print(hours)
        print(minutes)
        print(seconds)      
        again=input("Would you like to perform another age conversion?(y/quit)")
    
main()
