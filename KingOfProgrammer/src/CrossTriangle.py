N = raw_input('Please input any integer number as N (N>=1)\n')
print('Your input number is: '+N+', and the cross triangle output as following:')
'''
Write a program which will print out a numeric shape according to input to the program. The input is an integer number N (N>=1). The output is an N x N square together with its diagonal lines. Number increases by 1 from row to row. However if row# >= 10, print its last digit only.
Note:
1.  No extra space is allowed before or after each line.
2.  Please use standard input and output to solve.
3.  Please submit source code and executable file if compilation needed
'''
##The core algorithm 
int_N = int( N )+1
for x in range( 1,int_N ):
    if (x==1) | ( x==(int_N-1) ):
        print( (int_N-1) * str( x%10 ) )
    else:
        print( str(x) + ((x-2)*" ") + str(x) + str(x) + ((x-2)*" ") + str(x) )