#!/usr/bin/python3
"""a class LockedClass with no class or object attribute"""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes,
    except for the 'first_name' attribute.
    """

    __slots__ = ('first_name',)
