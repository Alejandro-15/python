
def printRev( n ):
   
    if n > 0:
        printRev( n - 1)
        print( n )
    if n == 10:
        print( "BOOMMMMM !!!")
    
printRev(10)

   
