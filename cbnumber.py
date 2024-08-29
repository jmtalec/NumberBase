"""
NumberBase © 2024 by Jean Moïse Talec is licensed under CC BY-NC-SA 4.0. 
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/
"""

from enum import Enum
from typing import Iterable, Union
from meta import _MetaNumberBase


__author__ = "Jean Moïse Talec"
__all__ = ["NumberBase", "Bases"]
__version__ = "1.0"

class Bases(Enum):
    DECIMAL = "0123456789"
    BINARY  = "01"
    HEXADECIMAL = "0123456789ABCDEF"

class NumberBase(int):
    #_int_attrs: list[str]

    def __new__(cls, x: int, base_map: Union[Iterable[object], Bases] = Bases.DECIMAL, null: object = None):
        # Create the int instance using __new__
        return super().__new__(cls, x)
    
    def __init__(self, x: int, base_map: Union[Iterable[object], Bases] = Bases.DECIMAL, null: object=None) -> None:
        

        #with open("./meta_int_data_type.json", "w") as f:
        #    dump(self._int_attrs, f)

        if type(base_map) == Bases:
            self.base = len(base_map.value)  
            self.base_map = tuple(base_map.value)
            self._field = dict(enumerate(base_map.value))  
        else:

            self.base = len(base_map)
            self.base_map = tuple(base_map)
            self._field = dict(enumerate(base_map))

        if null:
            self.null = null
        else:
            self.null = self._field[0]
        
        #for attr in dir(self):
        #    if attr in self._int_attrs:
        #        method = getattr(self, attr)
        #        if callable(method) and not inspect.isdatadescriptor(method):
        #            @classmethod
        #            def wrapper(cls, other):
        #                if isinstance(other, NumberBase):
        #                    # When adding another NumberBase, use the custom logic
        #                    return NumberBase(super().__getattribute__(attr)(other), base_map=self.base_map, null=self.null)
        #                elif isinstance(other, int):
        #                    # When adding an int, perform the addition and then convert back to NumberBase
        #                    return NumberBase(super().__getattribute__(attr)(other), base_map=self.base_map, null=self.null)
        #                else:
        #                    return NotImplemented
        #            setattr(self, attr, self._decorate(method))
        
        self._immutable = ("base", "base_map", "null", "_immutable", "_locked")
        # This lock is immuable
        self._locked = True

    def to_base(self, base_map, null=None):
        return NumberBase(self, base_map, null)

    def __setattr__(self, name, value):
        # Prevent reassignment of certain attributes after initialization
        if hasattr(self, '_locked') and name in self._immutable:
            raise AttributeError(f"The '{name}' attribute is immutable")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name in self._immutable:
            raise AttributeError(f"The '{name}' attribute is immutable")
        super().__delattr__(name)

    def __iter__(self):
        result = []
        num = self
        if num == 0:
            yield self.null
            return 
        elif self.base == 1:
            result = [self.base_map[0] for x in range(self)]
        else:
            while num > 0:
                remainder = num % self.base
                result.append(self._field[remainder])
                num //= self.base
            result.reverse()
        while result:
            yield result.pop(0)

    def __str__(self) -> str:
        return str().join([str(x) for x in self])

    def __repr__(self):
        return "[bn]: "+str(self)

    #def _decorate(self, method):
    #    def wrapper(*args, **kwargs):
    #        result = method(*args, **kwargs)
    #        if isinstance(result, NumberBase) or isinstance(result, int):
    #            return NumberBase(result, base_map=self.base_map, null=self.null)
    #        else:
    #            return result
    #    return wrapper
    
 
    def __add__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__add__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__add__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __and__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__and__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__and__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
                
    def __divmod__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__divmod__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__divmod__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__floordiv__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__floordiv__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __lshift__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__lshift__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__lshift__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __mod__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__mod__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__mod__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __mul__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__mul__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__mul__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __pow__(self, value, mod=None):
        v = super().__pow__(value, mod)
        if v >= 0:
            return NumberBase(v, self.base_map, self.null)
        else:
            return v
        
    def __radd__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__radd__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__radd__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rand__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rand__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rand__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
    
    def __rdivmod__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rdivmod__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rdivmod__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rfloordiv__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rfloordiv__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rfloordiv__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rlshift__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rlshift__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rlshift__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
    
    def __rmod__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rmod__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rmod__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rmul__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rmul__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rpow__(self, value, mod=None):
        v = super().__rpow__(value, mod)
        if v >= 0:
            return NumberBase(v, self.base_map, self.null)
        else:
            return v
        
    def __rrshift__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rrshift__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rrshift__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rshift__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rshift__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rshift__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rsub__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rsub__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rsub__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __rtruediv__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rtruediv__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rtruediv__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
    
    def __rxor__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__rxor__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__rxor__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __sub__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__sub__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__sub__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __truediv__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__truediv__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__truediv__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented
        
    def __xor__(self, other):
        if isinstance(other, NumberBase):
            return NumberBase(super().__xor__(other), base_map=self.base_map, null=self.null)
        elif isinstance(other, int):
            return NumberBase(super().__xor__(other), base_map=self.base_map, null=self.null)
        else:
            return NotImplemented

        

if __name__ == "__main__":
    from string import digits, ascii_lowercase
    num = NumberBase(25, [0, 1])
    print(num)
    print(num+1)
