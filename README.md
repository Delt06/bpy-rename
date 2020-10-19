# bpy-rename

A small script to automatically adjust the names of objects in the hierarchy in Blender.

## Features
- Converts to snake case (`example_name`)
- Removes prohibited words
- Corrects misspelled words


## Requirements
From the `/bin` directory of the Blender's built-in Python, execute with admin rights:  
(example of directory in Windows: `C:\Program Files\Blender Foundation\Blender 2.90\2.90\python\bin`)
```
./python -m ensurepip
./python -m pip install pyspellchecker
```

## Usage
Select the objects for renaming and run the script.

If there are any words that the spell checker was not able to correct, they will be appended with `error_postfix` (`<fix>`, by default). Use the search bar to manually resolve such cases.

There are messages printed to console. If the console is not visible, click `Window/Toggle System Console` in top left corner of Blender window.


## Configuration
- `known_words` - a list of extra words that are added to the dictionary of the spell checker
- `prohibited_words` - a list of words that are removed from the names
- `spell.distance` - the maximum distance between the word and a candidate for its correction. Possible values: {1, 2}.
