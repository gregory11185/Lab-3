'''
@author Gregory Eganovi
@since 10/05/2020
@version 1.0

Description: Python program that reads names and position numbers from a file that is out of order, sorts it
using bubble sort and writes the sorted list to output.txt file.
'''

# Creates a list to store information from file.
names = list()
mystring = " "

# Opens input.txt file for reading, and output.txt file for writing and closes them automatically after use. 
with open ('input.txt', 'r') as rf:
    with open('output.txt', 'w') as wf:
        
        # Reads one line at a time from input file and stores it into names list while splitting every element of the line
        for line in rf:
            names.append(line.split())
        
        # Uses bubble sort on the 3rd element of every line in names which is the position number and if its greater than
        # the next persons position number then swaps them. Keeps swapping until all elements are in proper positions and
        # no more swapping took place
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
        
        # Writes the new sorted names list to file output.txt 
        wf.writelines(["%s\n" % item for item in names])
