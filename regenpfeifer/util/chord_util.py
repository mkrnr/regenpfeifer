'''
Created on May 11, 2019

@author: mkoerner
'''
from regenpfeifer.util import stroke_util


def remove_markup(chord):
    strokes = chord.split("/")
    stripped_strokes = []
    for stroke in strokes:
        stripped_strokes.append(stroke_util.remove_markup(stroke))
    return "/".join(stripped_strokes)
