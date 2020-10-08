# Case 2 - Reducer using standard input and output
# Easy to test locally with Bash


import sys


thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    amount, department = datalist

    if department != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(str(thisValue) + '\t' + thisKey+'\n')

      # start over for each new key
      thisKey = department 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(amount)

# output the final key-summaryvalue result outside the loop
print(str(thisValue) + '\t' + thisKey+'\n')





