# Case 1 - Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("purchases.txt", "r") as input:
  with open("department_mapped.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("    ")
      if (len(datalist) == 6) : 
        date, time,store, department, amount, paymentType = datalist

        # output intermediate key-value pairs
        output.write(department + "\t" + amount + "\n")

        # display to console (not required - just for the user)
        print(department + "\t" + amount + "\n")

