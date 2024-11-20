from abc import ABC, abstractmethod

class SealedMeta(type):
    def __init__(cls, name, bases, cls_dict):
        super().__init__(name, bases, cls_dict)
        # If the class is defined with `__sealed__`, save it
        if "__sealed__" in cls_dict:
            cls._allowed_subclasses = cls_dict["__sealed__"]
        # Check if the class is allowed to subclass the base
        else:
            base = bases[0]
            if not hasattr(base, "_allowed_subclasses") or cls.__name__ not in base._allowed_subclasses:
                raise TypeError(f"{cls.__name__} is not allowed to subclass {base.__name__}")

class Shape(ABC, metaclass=SealedMeta):
    __sealed__ = ["Circle", "Rectangle"]  # Allowed subclasses

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return "Area of Circle"

class Rectangle(Shape):
    def area(self):
        return "Area of Rectangle"

# TypeError: Triangle is not allowed to subclass Shape
class Triangle(Shape):
    def area(self):
        return "Area of Triangle"