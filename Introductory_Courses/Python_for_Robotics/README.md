# Python for Robotics
The "Python for Robotics" course provided by the Construct. 

## Interesting info that was learned:
- Python is use in many Machine Learning applications, and is commonly used in ROS programs.
- Objects Oriented Programming is better for more complicated programs as opposed to Procedure Oriented. Namely ones which have many functions that must share variables. 
- Using the "global" is only safe for small scripts. 
- Prints are extremely helpful for debugging. 
- When working with LaserScanners, it's best to incorporate the data from multiple parts of a scan into boolean logic rather than one scan. This makes the program more robust.

## Skills that were learned:
- Importing Python modules, making variables from classes, calling valiables and methods from class instances.
- Different variable types, and how to maniplate these. 
- How to work with user input.
- Constructing boolean logic. 
- Forming FOR and WHILE loops. 
- Making functions.
- Creating classes. 

## Syntax Cheatsheet
Noteworthy Python Syntax from this course. For your and my convenience. 
- Import entire Python module.
`import <PythonModuleName>`
- Import a class or method from Python module.
`from <PythonModuleName> import <Method_or_ClassName>`
- Calling a method for an instanciated object.
`<ObjectName>.<MethodName>(<InputVariables>)`
- Displaying data.
`print(<EnterSomeTextHere_or_AVariableName>, <EnterSomeTextHere_or_AVariableName>, ...)`
    - Combines whatever is put in the input slots
- Display variable data type.
`type(VariableName)`

## Concept Cheetsheet
- Creating and storing variables
    - Python automatically sets data types whenever something is stored in a variable. 
    - Setting something equal to something else. Preferably with snake_case.
        - Example: `a = "Some string."
    - Python also lets you redefine whatever is stored is said variables
        - Example: `a = "Some other string."`
- Data types
    - Automatically declared by Python. Can be a major source of bugs.
        - To determine data type: `type(VariableName)`
    - Types:
        - Numbers `1,2,3,...`, Floats `0.2,0.4,0.352,...`
        - Strings `"This"` or `'That'`
        - Lists `["This","is","a",1,0.4,"list"]`
            - Can contain a combination of variable types. Denoted by brackets.
            - Positions in these are indexed, starting from 0. 
        - Tuples `("This","is","a",1,0.4,"list")`
            - Can contain a combination of variables. Immutable. Denoted by Parenthesis.
            - Positions in these are indexed, starting from 0.
        - Dictionaries `{1:"This",2:"is",3:"Dictionary"}`
            - A combination of key value pairs. Keys are immutable, but may be removed. Denoted by curly braces.
            - NO indices. Access elements via keys. 
     
## Snapshots and Demonstrations
Snapshots and demonstrations of what I found interesting. 
