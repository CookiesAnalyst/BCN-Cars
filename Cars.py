#1. IMPORT CSV
#2. READ CVS
#3. READ SPECIFIC COLUMNS AND ROWS OF CVS AND OUTPUT DE RESULT.
    #3.1. PRINT DATA OF NEIGHBOURGHOODS FROM MORE TO LESS POLLUTED CARS.
    #3.2. PRINT DATA OF CARS ON 2017 THAT MUST GO OUT OF CIRCULATION BY 2020.
#4. CREATE AN EXTRA ROW FOR DISTRICTS AS THE SUM OF DIFFERENT COLUMNS AND ROWS.
#5. MAP THE DATA WITH COLOUR ON A MAP BY DISTRICTS, VARYING INTENSITY FROM MORE TO LESS POLLUTED.

#1
file = open ("antt2016.csv", 'r')
print (file.name)

#2
#print (file.read ())

lines = file.readlines()
result = []
for x in lines:
    print(result.append(x.split(,)[0])) #--> read more about split!
    print (result)

file.close ()


print ("How many cars should be out of circulation if today begans the ban?\n"
       "1.-Neighbourhood\n 2.- District\n 3.- Barcelona")


#This example could be useful for further versions plotting elections results instead of cars in a map ob BCN.

# Example of list comprehension --> print [x.split(' ')[1] for x in open(file).readlines()]


