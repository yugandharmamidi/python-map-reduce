# Case 1 - Reducer using Files
# Easy to test
# Not quite Hadoop-ready

with open("department_sorted.txt","r") as sorted:
  with open("department_reducer.txt", "w") as output:

    thisKey = ""
    thisValue = 0.0

    for line in sorted:
      datalist = line.strip().split('\t')
      if (len(datalist) == 2) : 
        department, amount = datalist

        if department != thisKey:
          if thisKey:
            # output the previous key-summaryvalue result
            output.write(thisKey + '\t' + str(thisValue)+'\n')
            print(thisKey + '\t' + str(thisValue)+'\n')

          # start over for each new key
          thisKey = department 
          thisValue = 0.0
  
        # apply the aggregation function
        thisValue += float(amount)

    # output the final key-summaryvalue result outside the loop
    output.write(thisKey + '\t' + str(thisValue)+'\n')
    print(thisKey + '\t' + str(thisValue)+'\n')
