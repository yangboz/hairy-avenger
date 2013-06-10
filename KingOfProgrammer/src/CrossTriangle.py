N = raw_input('Please input any integer number as N (N>=1)\n')
print('Your input number is:'+N)
'''
Write a program which will print out a numeric shape according to input to the program. The input is an integer number N (N>=1). The output is an N x N square together with its diagonal lines. Number increases by 1 from row to row. However if row# >= 10, print its last digit only.
Note:
1.  No extra space is allowed before or after each line.
2.  Please use standard input and output to solve.
3.  Please submit source code and executable file if compilation needed
'''
print('And the cross triangle output as following:')
##The core algorithm 
int_N = int( N )+1
for x in range( 1,int_N ):
    print( int_N * str(x) )