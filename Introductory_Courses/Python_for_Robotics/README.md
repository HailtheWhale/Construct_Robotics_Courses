# Python for Robotics
The "Python for Robotics" course provided by the Construct. 

## Interesting info that was learned:
- Python is use in many Machine Learning applications, and is commonly used in ROS programs.
- Objects Oriented Programming is better for more complicated programs as opposed to Procedure Oriented. Namely ones which have many functions that must share variables. 
- Using the "global" keyword is only safe for small scripts. 
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
- Ask and *wait* for user input.
`input(<InputMessage>)`

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
        - Booleans `True` or `False`
- Operators 
    - Arithmetic and assignment operators are for the maths. See the below images, taken from ***The Construct's*** course.
 ![Arith_Op](https://github.com/HailtheWhale/Image_Repo/blob/main/Construct_Robotics_Courses/Introductory_Courses/Python_for_Robotics/Arithmetic_Ops.png)
 ![Assign Op](https://github.com/HailtheWhale/Image_Repo/blob/main/Construct_Robotics_Courses/Introductory_Courses/Python_for_Robotics/Assignment_Ops.png)
    - Comparison operators are for boolean logic.
 ![Comp Op](https://github.com/HailtheWhale/Image_Repo/blob/main/Construct_Robotics_Courses/Introductory_Courses/Python_for_Robotics/Comparison_Ops.png)
- Conditionals. Boolean Logic.
    - Sytax:
    
    ```
        if <Condition1>:
            <Statement1>
        elif <Condition2>:
            <Statement2>
        else:
            <Statement3>
    ```
    
     - Use compararison operators mentioned previously for conditionals. 
     - Else is optional. It will run if all other conditions are false.
- Loops. 
    - To keep code clean. To make large operations possible.
    - FOR loop.
        - Use for iterables. Runs until the end of the iterable unless broken. 
        - Syntax
        
        ```
            for <IterableName> in <Iterable>:
                <Statements>
        ```
        
    - WHILE loop.
        - USe when waiting for some condition. Runs until condition is false.
        - Syntax
        
        ```
            while <Condition1>:
                <Statements>
        ```
        
    - Special Keywords
        - `break`. For breaking out of loops prematurely.
        - `continue`. For skipping one iteration of a loop.
- Methods and Functions.
    - Use whenever there are any repeated blocks of code.
    - Synax:
    
        ```
        def <FunctionName>(<Condition1>=<Var1>,<Condition2>=<Var2>,...):
            <Statements>
            return <SomeValue>`
       ```
       
    - `return` statement is *optional*. It immediately ends the function process and returns some value.
    - Calling these: `<FunctionName>(<InputConditions>)`
- Object Oriented Programming.
    - Better for large codes. Let's functions share variables and keeps variables local to an object.
    - Objects are made from classes. Classes may be made by you.
    - Syntax
    
        ```
        class <ClassName>:`
            `def __init__(self,<Input1>,<Input2>,...):
                <Arguments>
            def <Method1>(self,<Input1>=<Var1>,<Input2>=<Var2>,...):
                <Arguments>
            if __name__ == '__main__':
                <Arguments>
         ```
         
        - `__init__` is a constructor. It only runs when an object is instanciated.
        - `if __name__ == '__main__'` runs whenever the python script itself is run.
        - May add as many methods and initialization arguments as desired.

## Snapshots and Demonstrations
Snapshots and demonstrations of what I found interesting. 

A while loop to continously check the distance of an object in front of the Turtlebot, and then stop when the robot is < 1 meter from the wall.

https://user-images.githubusercontent.com/82235221/211200491-0dd1f7b6-7e27-4f2b-9c97-c2e32d3faff4.mp4

A script which calls methods from the robot_control_class object to make the Summit robot go into a room.

https://user-images.githubusercontent.com/82235221/211200739-b1aa5b3d-87fd-4bda-a136-a895def191d2.mp4

An instanciated object which makes the Summit robot go to an opening, and then move in a small and big square.

https://user-images.githubusercontent.com/82235221/211200747-588e9729-27db-475a-94b8-9c2d4f4879ea.mp4

An instanciated object which makes the Turtlebot escape the Maze and celebrate.

[Youtube Link](https://youtu.be/JJU3nZ9ftgc)
