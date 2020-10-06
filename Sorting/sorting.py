'''
@author Gregory Eganovi
@since 10/05/2020
@version 1.0
'''

names = list()
mystring = " "
with open ('input.txt', 'r') as rf:
    with open('output.txt', 'w') as wf:
        for line in rf:
            names.append(line.split())

        passes = len(names) - 1
        switched = True
        while passes > 0 and switched:
            switched = False
            for i in range(passes):
                if int(names[i][2]) > int(names[i+1][2]):
                    temp = names[i]
                    names[i] = names[i+1]
                    names[i+1] = temp
                    switched = True
            passes = passes - 1
        wf.writelines(["%s\n" % item for item in names])