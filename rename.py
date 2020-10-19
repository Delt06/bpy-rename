import bpy
import re
from spellchecker import SpellChecker

# a list of known words (in addition to the built-in)
known_words = [
    'example', 'of', 'list'
]

# a list of prohibited words (removed from the names)
prohibited_words = [
    'material', 'mat', 'mesh'
]

spell = SpellChecker(case_sensitive=True)
spell.word_frequency.load_words(known_words)
spell.distance = 1


def to_snake_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def to_words(name):
    return name.split('_')


def remove_prohibited_words(words):
    return [w for w in words if not w in prohibited_words]


def apply_spell_correction(words):
    return [spell.correction(w) for w in words]


def to_name(words):
    return '_'.join(words)


def adjust_name(name):
    name = to_snake_case(name)
    
    words = to_words(name)
    words = remove_prohibited_words(words)
    words = apply_spell_correction(words)
    
    name = to_name(words)
    return to_snake_case(name)


for obj in bpy.context.selected_objects:
    obj.name = adjust_name(obj.name)
    
    if obj.data:
        obj.data.name = adjust_name(obj.data.name)
        
    for slot in obj.material_slots:
        if slot.material:
            slot.material.name = adjust_name(slot.material.name)
