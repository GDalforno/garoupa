#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
# 
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
# 
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and is unethical regarding the effort and
#  time spent here.

"""Some shortcuts to the null operand and to ease creating elements"""
from garoupa.hosh import Hosh


class Identity(Hosh):
    """
    Identity element

    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.

    Parameters
    ----------
    version
        UT32.4 or UT64.4 changes the number of digits and robustness against collisions
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'
    """
    def __init__(self, version, etype_inducer="ordered"):
        super().__init__([0, 0, 0, 0, 0, 0], version=version)
        self._etype_inducer = etype_inducer

    @property
    def u(self):
        """Shortcut to induce etype=unordered in the next operand, when it is not a ready Hosh object.
        default=Ordered, h=Hybrid and u=Unordered

        Usage:

        >>> from garoupa import ø, Ø, Hosh
        >>> a = ø.u * b"654"
        >>> print(a)
        2_e2b898e_______________________
        >>> b = Ø.u * b"654"
        >>> print(b)
        f_ec361e9ebb223fc_______________________________________________
        >>> Hosh(b"654", "unordered", "UT32.4") == a and b == Hosh(b"654","unordered", "UT64.4")
        True
        """
        return Identity(self.version, etype_inducer="unordered")

    @property
    def h(self):
        """Shortcut to induce etype=hybrid in the next operand, when it is given as a bytes object.
        default=Ordered, h=Hybrid and u=Unordered

        Usage:

        >>> from garoupa import Hosh, ø, Ø
        >>> a = ø.h * b"654"
        >>> print(a)
        rf_a6340cfb8d0a6b7451ecb1a8317a1
        >>> b = Ø.h * b"654"
        >>> print(b)
        rh_dc705c5c6cff41d8fe4f49956e425b275f3c091372d4a0ba8c673caa46edc
        >>> Hosh(b"654", "hybrid", "UT32.4") == a and b == Hosh(b"654","hybrid", "UT64.4")
        True
        """
        return Identity(self.version, etype_inducer="hybrid")


class ø(Identity):
    """
    32-digit identity element

    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.

    Normal usage (as an already instantiated object:

    >>> from garoupa import ø
    >>> ø.id
    '00000000000000000000000000000000'
    >>> print(ø * 872696823986235926596245)
    00_000000000b8ccfd58058a15174a9b

    Parameters
    ----------
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'
    """

    def __init__(self, etype_inducer="ordered"):
        super().__init__("UT32.4", etype_inducer)


class Ø(Identity):
    """
    64-digit identity element

    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.

    Normal usage (as an already instantiated object:

    >>> from garoupa import Ø
    >>> Ø.id
    '0000000000000000000000000000000000000000000000000000000000000000'
    >>> print(Ø * 872696823986235926596245)
    00_00000000000000000000000000000000000000000b8cbfd58058b15174ad1

    Parameters
    ----------
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'
    """

    def __init__(self, etype_inducer="ordered"):
        super().__init__("UT64.4", etype_inducer)