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
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.

from itertools import chain, repeat

from garoupa.algebra.dihedral.dr import Dr
from garoupa.algebra.dihedral.ds import Ds
from garoupa.algebra.matrix.group import Group
from garoupa.algebra.product.product import Product


class D(Group):
    def __init__(self, n, seed=None):
        self.r = lambda: (Dr(r, n) for r in range(n))
        self.s = lambda: (Ds(s, n) for s in range(n))
        sorted = lambda: chain(self.s(), self.r())
        super().__init__(Dr(0, n), sorted, seed)
        self.n = n

    @property
    def comm_degree(self):
        """Exact commutativity degree"""
        num = (self.n + 6) if self.n % 2 == 0 else (self.n + 3)
        den = 2 * self.order
        return num / den

    def __iter__(self):
        while True:
            yield self.rnd.choice([Dr, Ds])(self.samplei(), self.n)

    def __repr__(self):
        return f"D{self.n}"

    def __xor__(self, other):
        return Product(*repeat(self, other))

    __pow__ = __xor__

    def replace(self, *args, **kwargs):
        dic = {"n": self.n, "seed": self.seed}
        dic.update(kwargs)
        return self.__class__(**dic)
