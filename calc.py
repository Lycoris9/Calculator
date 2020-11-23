#extras: division, powers, decimals

#loop - tested
continues = "Y"
while continues == "Y":

#operation - tested
    print("Operations: 1 = addition, 2 = subtraction, 3 = multiplication, 4 = division, 5 = powers")
    stroperation = input("Choose an operation: ")
    floatoperation = float(stroperation)

#addition - tested
    if floatoperation == 1:
    
    #inputs - tested
        straddend1 = input("Enter Your First Addend: ")
        straddend2 = input("Enter Your Second Addend: ") 
        floataddend1 = float(straddend1)
        floataddend2 = float(straddend2)
        
    #operation - tested
        floataddans = floataddend1 + floataddend2 
        straddans = str(floataddans)
        print("The sum is:" + straddans)

#subtraction - tested
    elif floatoperation == 2:
    
    #inputs - tested
        strminuend = input("Enter Your Minuend: ")
        strsubtrahend = input("Enter Your Subtrahend: ") 
        floatminuend = float(strminuend)
        floatsubtrahend = float(strsubtrahend)
        
    #operation - tested
        floatsubans = floatminuend - floatsubtrahend
        strsubans = str(floatsubans)
        print("The difference is:" + strsubans)

#multiplication - tested
    elif floatoperation == 3:
        
    #inputs - tested
        strfactor1 = input("Enter Your First Factor: ")
        strfactor2 = input("Enter Your Second Factor: ") 
        floatfactor1 = float(strfactor1)
        floatfactor2 = float(strfactor2)
        
    #operation - tested
        floatmultans = floatfactor1*floatfactor2
        strmultans = str(floatmultans)
        print("The product is:" + strmultans)

#division - tested
    elif floatoperation == 4:
        
    #inputs - tested
        strdividend = input("Enter Your Dividend: ")
        strdivisor = input("Enter Your Divisor: ") 
        floatdividend = float(strdividend)
        floatdivisor = float(strdivisor)
        
    #operation - tested
        floatdivans = floatdividend/floatdivisor
        strdivans = str(floatdivans)
        print("The quotient is:" + strdivans)
 
 #powers - tested
    elif floatoperation == 5:
    
    #inputs - tested
        strbase = input("Enter Your Base: ")
        strexponent = input("Enter Your Exponent: ") 
        floatbase = float(strbase)
        floatexponent = float(strexponent)
        
    #operation - tested
        floatexpans = pow(floatbase, floatexponent)
        strexpans = str(floatexpans)
        print("The power is:" + strexpans)
 
 #continue - tested
    continues = input("Continue? Y/N: ") 
