"""**************************************************************************
* Project Name : Projekt IVS                                                *
* File : calcMath.py                                                        *
* Date : 20.04.2022                                                         *
* Last change : 23.04.2022                                                  *
* Author : Samuel Šimún (xsimun04)                                          *
*                                                                           *
* Description : Math library with basic and advanced math operations        *
*                                                                           *
**************************************************************************"""

"""**************************************************************************
* @file calcMath.py                                                         *
*                                                                           *
* @brief Math Library                                                       *
* @author Samuel Šimún (xsimun04)                                           *
**************************************************************************"""

"""******************************************************
* Function for addition 2 numbers                       *
*                                                       *
* @param First Addend                                   *
* @param Second Addend                                  *
* @return Sum of Addends                                *
******************************************************"""


def add(a, b):
    return a + b  # Return Result


"""******************************************************
* Function for subtraction 2 numbers                    *
*                                                       *
* @param Minuend                                        *
* @param Subtrahend                                     *
* @return Difference between minuend and subtrahend     *
******************************************************"""


def sub(a, b):
    return a - b  # Return Result


"""******************************************************   
* Function for multiplication 2 numbers                 *
*                                                       *
* @param First factor                                   *
* @param Second factor                                  *
* @return Product of factors                            *
******************************************************"""


def mul(a, b):
    return a * b  # Return Result


"""******************************************************   
* Function for division 2 numbers                       *
*                                                       *
* @param Dividend                                       *
* @param Divisor                                        *
* @return Quotient or Error if Divisor is 0             *
******************************************************"""


def div(a, b):
    if b == 0:  # If Divisor is equal to 0 return Error
        return "DIVISION BY ZERO"
    return a / b  # Return Result


"""****************************************************************   
* Function for counting Factorials                                *
*                                                                 *
* @param Factorial to count                                       *
* @return Value of Factorial or Error if input is not positive    *
****************************************************************"""


def factorial(x):
    if x < 0:  # Checking if factorial is less than zero
        return "NOT POSITIVE NUMBER"
    elif x == 0:  # If factorial is 0 then result is 1
        return 1

    pom = 1  # Declaration of help local variable
    for i in range(1, x + 1):
        pom = pom * i  # Multiplying pom and i until i is not equal to factorial

    return pom  # Return value of factorial


"""******************************************************   
* Function for power 2 numbers                          *
*                                                       *
* @param Base                                           *
* @param Positive Exponent                              *
* @return Result                                        *
******************************************************"""


def power(x, n):
    if n < 0:  # If exponent is less than 0 return Error
        return "NOT NATURAL NUMBER"

    return x ** n  # Return Result


"""******************************************************   
* Function of looking for root                          *
*                                                       *
* @param Index                                          *
* @param Radicand                                       *
* @return Result                                        *
******************************************************"""


def root(n, x):
    if (x < 0) or (n <= 0):  # If Index or Raicand is less than 0 return Error
        return "NUMBER IS NOT POSITIVE NUMBER"

    res = round(x ** (1 / n), 4)  # Returning rounder number of powered number by 1/n
    return res


def mod(a, b):
    """******************************************************
    * @function mod                                         *
    * Function for modulo                                   *
    *                                                       *
    * @param Dividend                                       *
    * @param Divisor                                        *
    * @return Result or Error if Divisor is 0               *
    ******************************************************"""
    if b == 0:  # If Divisor is equal to 0 return Error
        return "DIVISION BY ZERO"

    return a % b


"""*** End of file calcMath.py ***"""
