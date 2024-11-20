class SealedMetaForm(type):

    def __init__(cls, name, bases, cls_dict):
        super().__init__(name, bases, cls_dict)

        # Define allowed subclasses via __sealed__
        if "__sealed__" in cls_dict:
            cls._allowed_subclasses = cls_dict["__sealed__"]
        else:
            base = bases[0]
            if not hasattr(base, "_allowed_subclasses") or cls.__name__ not in base._allowed_subclasses:
                raise TypeError(f"{cls.__name__} is not allowed to subclass {base.__name__}")

class Shape(metaclass=SealedMetaForm):
    __sealed__ = ["Square", "Rectangle"]

    def price(self):
        raise NotImplementedError("Must implement in subclass")

class Square(Shape):
    def price(self):
        return "Pricing Square"

class Rectangle(Shape):
    def price(self):
        return "Pricing Rectangle"