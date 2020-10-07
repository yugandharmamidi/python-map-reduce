# Python Map Reduce

Basic Python introduction and concepts needed in preparation for working with map-reduce solutions.

## Requirements

- Install Chocolatey, the Windows package manager
- Install the Anaconda 3 version for Python + common packages
- Install Visual Studio Code for text editing
- Add Open Command Window Here as Administrator to your File Explorer context menu.

See: [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Case 1:  Local file-based

```PowerShell
py shopping_mapper.py
py shopping_sorter.py
py shopping_reducer.py
```

## Case 2:  Use standard input and output

Use the console (standard input and output) and shell commands to pipe information.  We'll use the built-in shell sort command, so we don't need that anymore. 

cat data | map | sort | reduce

PowerShell and Bash use the same commands:

```Bash
cat part.txt
cat part.txt | python shopping_mapper.py
cat part.txt | python shopping_mapper.py | sort
cat part.txt | python shopping_mapper.py | sort  | python shopping_reducer.py
```
To Process the larger file i.e., purchases.txt. we need to run the following commands,
```Bash
cat purchases.txt
cat purchases.txt | python shopping_mapper.py
cat purchases.txt | python shopping_mapper.py | sort
cat purchases.txt | python shopping_mapper.py | sort  | python shopping_reducer.py
```
## References

- [Udacity "Introduction to Hadoop and MapReduce"](https://classroom.udacity.com/courses/ud617/)
- [IBM Python for Data Science](https://cognitiveclass.ai/courses/python-for-data-science)
- [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Repository

- [https://github.com/denisecase/python-map-reduce](https://github.com/denisecase/python-map-reduce)
