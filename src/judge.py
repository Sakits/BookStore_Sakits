import os
print('Input the test case you want to run!')
x = int(input())

os.system('./run.sh')

if x == 1:
    com = 'rm my.out'
    os.system(com)
    os.system('./run.sh')

    for i in range(1, 11):
        print('Runing test data', i)
        com = 'time ./main < ../Data/AdvancedDataSet/testcase' + str(x) + '/' + str(i) + '.in > my.out'
        os.system(com)
        print("Diffing Output")
        com = 'diff my.out ../Data/AdvancedDataSet/testcase' + str(x) + '/' + str(i) + '.out'
        os.system(com)

    os.system('./run.sh')
        
