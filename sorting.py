'''
 @author Gregory Eganovi
  @since 10/04/2020
  @version 1.0

  Description: Program that reads a file called "input.txt" that has
  a list of names and a position number on each
  line that have been scrambled. The program reads the lines and sorts
  them in a proper order by position number and
  prints the sorted list to a file called output.txt.

  Uses 2 methods. One called populateArray() which receives 2 arrays with
  maximum of 100 slots each. Fills the arrays with proper values from
  the file. First name and last name in one array.
  Position number in another. Returns number of items in the array. A second
  method called bubbleSort() also receives 2 arrays and the number of
  items and uses the position number to sort both arrays in proper
  order.
'''








    #Fills the arrays with values and
    #returns the number of items in the arrays.
    def populateArray(person, position):
        sc = open("input.txt","r")
        count = 0
        temp = ""

        while sc.hasNext():
            person[count] = sc.next()
            temp = sc.next()
            person[count] = person[count] + " " + temp
            position[count] = sc.nextInt()

            count+=1

        return count


    # Sorts both of the arrays based on position number.
    def bubbleSort(person, position, count):
        hold = 0
        temp = ""
        switched = True

        for i in range(count - 1 and switched):
            switched = False

            for j in range (count - i - 1):
                if position[j] > position[j+1]:
                    switched = True
                    hold = position[j]
                    position[j] = position[j+1]
                    position[j + 1] = hold
                    temp = person[j]
                    person[j] = person [j+1]
                    person[j+1] = temp


    person = []
    position = []
    count = 0

    ps = open("output.txt","w")

    count = populateArray(person, position)
    bubbleSort(person, position, count)

    for i in range(count):
        ps.write("%d\t %s\n", position[i], person[i])



