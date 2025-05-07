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
- 
### Classes with internal data fields
A pass `create_classes` after RCO that:
- Translates all calls to class constructor into a tuple constructor.
- Translates all class field references to the reference at the corresponding index in the tuple.
- Translates calls to class constructors to add the class functions as fields of the object tuple 