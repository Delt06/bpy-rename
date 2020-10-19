# bpy-rename

A small script to automatically adjust the names of objects in the hierarchy.

## Features
- Converts to snake case (`example_name`)
- Removes prohibited words
- Corrects misspelled words


## Requirements
From the `/bin` directory of the Blender's built-in Python, execute:

```
./python -m ensurepip
./python -m pip install pyspellchecker
```

## Usage
Select the objects for renaming and run the script.


## Configuration
- `known_words` - a list of extra words that are added to the dictionary of the spell checker
- `prohibited_words` - a list of words that are removed from the names
