# CS 3020 - Final Project
## Classes with functions and inheritance
Isabelle Kriz, Eve Hammond, Nora Garcia de Vicente

## Features Implemented

The goal of this project is to implement custom classes.

Classes can:
- Define internal data fields
- Define internal functions and call them from each object.
- Allow for class inheritance.

An example of functionality
```
class Shape:
    area: int
    def get_area(self: Shape) -> int:
        return self.area

class Square(Shape):
    side_len: int
    def get_side_len(self: Square) -> int:
        return self.side_len

sq = Square(4, 2)
print(sq.get_area())
print(sq.get_side_len())
```
## Implementation approach
### Type checking
- Added to the global environment a hash_map that matches variables to the custom classes they are.
- Added to the global environment a hash_map that matches class names with a list of their fields and their types
- Added a new dataclass `CustomType` to keep track of which variables are classes and not jus treat them as strings.
- TC case for ClassDef adds the class type and its definition to our global environment
- TC case for FieldRef checks the class is defined and then checks the referenced field is the correct type.
### RCO
- FieldRefs are treated the same way as Prims, and stored in a separate temp value because they will eventually be converted to subscripts
- If Assign() has a FieldRef on the left side, creates a new instance of the class with all fields copied except the one to be changed because tuples are immutable
### Classes with internal data fields
A pass `create_classes` after RCO that:
- Internally encoded class fields as class.field to allow for repeated field names
- Translates all calls to class constructor into a tuple constructor.
- Translates all class field references to the reference at the corresponding index in the tuple.
- Translates calls to class constructors to add the class functions as fields of the object tuple 
### Superclasses
- Refined typechecker to add all fields of parent class to the current class when ClassDef
- When calling class functions, we check recursively all the parent classes to find the first class that has defined that function
### Class functions
- Encoded function names as <class_name><function_name> to allow repeated function names for different classes
- Worked on the parser to allow function definitions inside classes
- Altered the tuple case in select-instructions to allow for functions stored inside of tuples by adding a leaq instruction

## Limitations
- Given a function for class Point named add(). defining a function Pointadd would not be allowed
- You can only change class values inside a function if you return self. 
Since tuples are immutable in principle, implementing this was unfeasible in the given timeframe.