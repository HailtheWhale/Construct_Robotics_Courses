# C++ for Robotics
The "C++ for Robotics Course" offered by the Construct.

## Interesting Info that was learned:
- C++ is a compiled language... meaning every script change must be compiled before it may be executed.
- ROS can handle C++ compilation.
- C++ variables must have their types defined before use. 

## Skills that were learned:
- Importing modules. Creating variables.
- 


## Syntax Cheatsheet:
- Compiling a C++ file.
`g++ -std=c++11 <ScriptNameorPathToScript>.cpp -o <CompiledScriptName>`
- Including ROS C++ modules
`#include "<ROSPackageName>/<ROSPackageHeader>.h"`
- Including C++ modules
`#include <<PackageName>/<ROSPackageHeader>.h>`
- Printing variables (ROS SPECIFIC)
`ROS_INFO_STREAM(<OutputMessage1> << <OutputMessage2> << <OutputMessage3>)`
- Printing variables (need `#include <iostream>` for this)
`cout << <SomeText_or_Variable> << endl`

## Concept Cheatsheet:
- The `int main(int argc, char **argv){}`
  - The main body of C++ scripts.
  - All code in this function is what's executed. This includes calling other functions. 
  - `return 0;`
    - Simply closes this main body.
- Data Types 
  - Booleans: `true` or `false`.
  - Numbers: `int` or `double` or `float`.
    - Floats hold up to 7 decimals. Doubles hold up to 15.
  - Texts: `char` or `string`.
    - Characters need the length of the text specified. Ex: `char h[6] = "hello"`
    - Strings do not. Ex: `d = "Hi there."`
    - Strings may be concatenated.
    - Both may have characters accessed through indexing. 
  - Lists: `list<<DataType>> <VariableName>({<Val1>,<Val2>,<Val3>,...});`
    - May be of any data type, but this must be specified. 
  - Dictionaries: ``

## Snapshots and Demonstrations:
Snapshots and demonstrations of what I found interesting.
