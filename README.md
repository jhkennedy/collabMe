[![Stories in Ready](https://badge.waffle.io/jhkennedy/collabMe.png?label=ready&title=Ready)](https://waffle.io/jhkennedy/collabMe?utm_source=badge)
CollabMe
========

This is a small Python package to generate a list of collaborators from a `bibtex` file --- A problem often faced by scientists writing NSF proposals. 

*Warning:* It's very new. 

Installation and Usage
----------------------

CollabMe has only one dependancy, [Pybtex](https://pybtex.org/). To install it, use `pip`:

```sh
pip install pybtex
```

CollabMe is still under (heavy) development! As such, just use the source:

```sh
git clone https://github.com/jhkennedy/collabMe.git
```

Then move into the collabMe directory:

```sh
cd collabMe
```

and generate a list of collaborators by passing it a bibtex file:

```sh
clbme -b Examples/example.bib
```

This will generate an alphabetical list of all the authors found in the bibtex file, and print it stdout. To save the list, simply redirect the output to a file:

```sh
clbme -b Examples/example.bib > collabs.txt
```

Development
-----------

Comments, criticisms, suggestions, request, etc. are welcome! Simply open an [issue]() on github, and I'll see what I can do. 

Contributions are especially welcome! Use the [forking workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#forking-workflow). 

