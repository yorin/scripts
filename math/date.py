from datetime import date 
  
#Python provides datetime module to deal with all datetime related issues in python. Using datetime we can find the age by subtracting birth year from current year. Along with this, we need to focus on the birth month and birthday. For this, we check if current month and date are less than birth month and date. If yes subtract 1 from age, otherwise 0.
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 
      
# Driver code  
print(calculateAge(date(1976, 11, 26)), "years of age")


#This case has to be raised as an exception because the calculation of birthdate may be inaccurate. This method includes try and catch for this exception.
def calculateAge2(born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 
          
# Driver code 
print(calculateAge2(date(1997, 2, 3)), "years of age") 

#Using division
#In this approach, we calculate the number of date from the birth date till current date. Divide the number of date by the days in a year i.e 365.2425.
def calculateAge3(birthDate): 
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age 
          
# Driver code 
print(calculateAge3(date(1997, 2, 3)), "years")
