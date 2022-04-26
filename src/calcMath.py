"""!
* Project Name : Projekt IVS                                                
* File : calcMath.py                                                        
* Date : 20.04.2022                                                         
* Last change : 23.04.2022                                                  
* Author : Samuel Šimún (xsimun04)                                                                                                                     
* Description : Math library with basic and advanced math operations                                                                                 
"""

"""!
 @file calcMath.py                                                         
                                                                           
 @brief Math Library                                                       
 @author Samuel Šimún (xsimun04)
"""




def add(a, b):
    """!
    Function for addition of 2 numbers
    @param a Addend
    @param b Addend
    @return Sum of Addends    
    """
    return a + b  # Return Result




def sub(a, b):
    """!
    Function for subtraction 2 numbers                    
                                                          
    @param a Minuend                                        
    @param b Subtrahend                                     
    @return Difference between minuend and subtrahend
    """
    return a - b  # Return Result




def mul(a, b):
    """!
    Function for multiplication 2 numbers                 
                                                          
    @param a First factor                                   
    @param b Second factor                                  
    @return Product of factors
    """
    return a * b  # Return Result




def div(a, b):
    """!  
    Function for division 2 numbers                       
                                                          
    @param a Dividend                                       
    @param b Divisor                                        
    @return Quotient or Error if Divisor is 0
    """
    if b == 0:  # If Divisor is equal to 0 return Error
        return "DIVISION BY ZERO"
    return a / b  # Return Result





def factorial(x):
    """! 
    Function for counting Factorials                                
                                                                    
    @param x Factorial to count                                       
    @return Value of Factorial or Error if input is not positive
    """
    if x < 0:  # Checking if factorial is less than zero
        return "NOT POSITIVE NUMBER"
    elif x == 0:  # If factorial is 0 then result is 1
        return 1

    pom = 1  # Declaration of help local variable
    for i in range(1, x + 1):
        pom = pom * i  # Multiplying pom and i until i is not equal to factorial

    return pom  # Return value of factorial





def power(x, n):
    """! 
    Function for power of 2 numbers                          
                                                          
    @param x Base                                           
    @param n Positive Exponent                              
    @return Result or Error if exponent is less than 0                                       
    """
    if n < 0:  # If exponent is less than 0 return Error
        return "NOT NATURAL NUMBER"

    return x ** n  # Return Result





def root(n, x):
    """!   
    Function of looking for root                          
                                                          
    @param n Index                                          
    @param x Radicand                                       
    @return Result or Error if Index or Radicand is less than 0
    """
    if (x < 0) or (n <= 0):  # If Index or Radicand is less than 0 return Error
        return "NUMBER IS NOT POSITIVE NUMBER"

    res = round(x ** (1 / n), 4)  # Returning rounder number of powered number by 1/n
    return res


def mod(a, b):
    """!                                         
    Function for modulo                                   
                                                           
    @param a Dividend                                       
    @param b Divisor                                        
    @return Result or Error if Divisor is 0

    """
    if b == 0:  # If Divisor is equal to 0 return Error
        return "DIVISION BY ZERO"

    return a % b


"""*** End of file calcMath.py ***"""
