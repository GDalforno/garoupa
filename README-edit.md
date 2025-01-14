![test](https://github.com/davips/garoupa/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/garoupa/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/garoupa)
<a href="https://pypi.org/project/garoupa">
<img src="https://img.shields.io/pypi/v/garoupa.svg?label=release&color=blue&style=flat-square" alt="pypi">
</a>
![Python version](https://img.shields.io/badge/python-3.8%20%7C%203.9-blue.svg)
[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5501845.svg)](https://doi.org/10.5281/zenodo.5501845)
[![arXiv](https://img.shields.io/badge/arXiv-2109.06028-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2109.06028)
[![API documentation](https://img.shields.io/badge/doc-API%20%28auto%29-a0a0a0.svg)](https://davips.github.io/garoupa)


# GaROUPa - Identification based on group theory
The identification module of this library is evolving at its successor library [hosh (code)](https://github.com/davips/hosh) / [hosh (package)](https://pypi.org/project/hosh).
The algebra module exists only here.
 


GaROUPa solves the identification problem of multi-valued objects or sequences of events.<br>This [Python library](https://pypi.org/project/garoupa) / [code](https://github.com/davips/garoupa) provides a reference implementation for the UT*.4 specification presented [here](https://arxiv.org/abs/2109.06028).  | ![fir0002  flagstaffotos [at] gmail.com Canon 20D + Tamron 28-75mm f/2.8, GFDL 1.2 &lt;http://www.gnu.org/licenses/old-licenses/fdl-1.2.html&gt;, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Malabar_grouper_melb_aquarium.jpg/256px-Malabar_grouper_melb_aquarium.jpg)
:-------------------------:|:-------------------------:

We adopt a novel paradigm to universally unique identification (UUID), making identifiers deterministic and predictable, 
even before an object is generated by a (possibly costly) process.   
Here, data versioning and composition of processing steps are directly mapped as simple operations over identifiers.
We call each of the latter a Hosh, i.e., an identifier is an _**o**perable **h**a**sh**_.

A complete implementation of the remaining ideas from the [paper](https://arxiv.org/abs/2109.06028) is provided in this
[cacheable lazy dict](https://pypi.org/project/ldict/2.211016.3) which depends on GaROUPa and serves as an advanced usage example.
<br>
A more robust (entirely rewritten) version is available in the package [idict](https://pypi.org/project/idict).

## Overview
A product of identifiers produces a new identifier as shown below, where sequences of bytes (`b"..."`) are passed to simulate binary objects to be hashed.

![img.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img.png) | New identifiers are easily <br> created from the identity <br> element `ø`. Also available as `identity` for people <br>or systems allergic to <br>utf-8 encoding.
-------------------------|-------------------------

![img_1.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_1.png) | Operations can be reverted by the inverse of the identifier.
-------------------------|-------------------------

![img_2.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_2.png) | Operations are associative. <br>They are order-sensitive by default, <br>in which case they are called _ordered_ ids.
-------------------------|-------------------------

However, order-insensitive (called _unordered_) and order-insensitive-among-themselves (called _hybrid_) identifiers are also available. | .
-------------------------|-------------------------
![img_3.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_3.png) | .

This is how they affect each other: | .
-------------------------|-------------------------
![img_4.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_4.png) | .

The chance of collision is determined by the number of possible identifiers of each type.
Some versions are provided, e.g.: UT32.4, UT40.4 (default), UT64.4.
They can be easily implemented in other languages and are 
intended to be a specification on how to identify multi-valued objects and multi-step processes.
Unordered ids use a very narrow range of the total number of identifiers.
This is not a problem as they are not very useful.

One use for unordered ids could be the embedding of authorship or other metadata into an object without worrying about the timing, since the resulting id will remain the same, no matter when the unordered id is operated with the id of the object under construction. | . 
-------------------------|-------------------------
![img_5.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_5.png) | . 

Conversely, hybrid ids are excelent to represent values in a data structure like a map, 
since the order is not relevant when the consumer process looks up for keys, not indexes.
Converselly, a chain of a data processing functions usually implies one step is dependent on the result of the previous step.
This makes ordered ids the perfect fit to identify functions (and also their composition, as a consequence).

### Relationships can also be represented
Here is another possible use. ORCIDs are managed unique identifiers for researchers.
They can be directly used as digests to create operable identifiers.
We recommend the use of 40 digits to allow operations with SHA-1 hashes. 
They are common in version control repositories among other uses.
![img_orcid.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_orcid.png)

Unordered relationships are represented by hybrid ids.
Automatic transparent conversion between ORCID dashes by a hexdecimal character can be implemented in the future if needed.
![img_orcid-comm.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_orcid-comm.png)

## More info
Aside from the [paper](https://arxiv.org/abs/2109.06028), [PyPI package](https://pypi.org/project/garoupa) 
and [GitHub repository](https://github.com/davips/garoupa), 
one can find more information, at a higher level application perspective, 
in this presentation:
![image](https://raw.githubusercontent.com/davips/garoupa/14cb45b888eb8a18ae093d200075c1a8a7e9cacb/examples/capa-slides-gdocs.png)
A lower level perspective is provided in the [API documentation](https://davips.github.io/garoupa).

## Python installation
### from package
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI
pip install garoupa
```

### from source
```bash
git clone https://github.com/davips/garoupa
cd garoupa
poetry install
```

### Examples
Some usage examples.

<<operation>>

### Examples (abstract algebra)
Although not the focus of the library, GaROUPa hosts also some niceties for group theory experimentation.
Some examples are provided below.

<<groups>>

<<commutativity>>

<<repetition>>

**Tendence of commutativity on Mn**
<details>
<p>

```python3
from itertools import chain

from garoupa.algebra.matrix.m import M
from garoupa.algebra.matrix.m8bit import M8bit


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1:]:
            if a * b == b * a:
                count += 2
            i += 2
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t{100 * count / i} %", sep="")


M1_4 = map(M, range(1, 5))
for G in chain(M1_4, [M8bit(), M(5)]):
    traverse(G)
# ...
for G in map(M, range(6, 11)):
    i, count = 0, 0
    for a, b in zip(G, G):
        if a * b == b * a:
            count += 1
        i += 1
        if i >= 1_000_000:
            break
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t~{100 * count / i} %", sep="")

"""
|M1| = 1:                        1/1:  0 bits	100.0 %
|M2| = 2:                        4/4:  1 bits	100.0 %
|M3| = 8:                      40/64:  3 bits	62.5 %
|M4| = 64:                 1024/4096:  6 bits	25.0 %
|M8bit| = 256:              14848/65536:  8 bits	22.65625 %
|M5| = 1024:           62464/1048576:  10 bits	5.95703125 %
|M6| = 32768:              286/32768:  15 bits	0.872802734375 %
|M7| = 2097152:          683/1000000:  21 bits	0.0683 %
|M8| = 268435456:         30/1000000:  28 bits	0.003 %
|M9| = 68719476736:        1/1000000:  36 bits	0.0001 %
|M10| = 35184372088832:     0/1000000:  45 bits	0.0 %
"""
```
</p>
</details>

**Groups benefit from methods from the module 'hosh'**
<details>
<p>

```python3
from garoupa.algebra.matrix import M

m = ~M(23)
print(repr(m.hosh))
```
<a href="https://github.com/davips/garoupa/blob/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png">
<img src="https://raw.githubusercontent.com/davips/garoupa/main/examples/7KDd8TiA3S11QTkUid2wy87DQIeGQ35vB1bsP5Y6DjZ.png" alt="Colored base-62 representation" width="380" height="18">
</a>
</p>
</details>



## Performance
Computation time for the simple operations performed by GaROUPa can be considered negligible for most applications,
since the order of magnitude of creating and operating identifiers is around a few μs:
![img_6.png](https://raw.githubusercontent.com/davips/garoupa/main/examples/img_6.png)
On the other hand, we estimate up to ~7x gains in speed when porting the core code to  _rust_.
The package [hosh](https://pypi.org/project/hosh) was a faster implementation of an earlier version of GaROUPa,
It will be updated to be fully compatible with current GaROUPa at major version `2.*.*`.
As the performance of garoupa seems already very high, an updated 'rust' implementation might become unnecessary.
Some parts of the algebra module need additional packages, they can be installed using:
`poetry install -E full`

## Grants
This work was partially supported by Fapesp under supervision of
Prof. André C. P. L. F. de Carvalho at CEPID-CeMEAI (Grants 2013/07375-0 – 2019/01735-0).
