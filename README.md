# Python collection views
Mutable and immutable views over standard collections with proper type annotations.

## Install
```
pip install collection-views
```

## Sample
```python
from collection_views import ImmutableViewList

mylist = ["Hello", "collection", "views"]
myview = ImmutableViewList(mylist)

print(myview[1]) # prints "collection"
print(myview[1:]) # prints "['collection', 'views']"
myview[0] = "Bye" # Does not support item assignment!
```

## Python support
New releases will support all actively maintained Python versions.
The latest release targets python 3.8 through 3.12.

## Features
* `ImmutableViewList`, an immutable view over a list.
