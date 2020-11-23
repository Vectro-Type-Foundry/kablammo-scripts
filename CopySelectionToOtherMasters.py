# -*- coding: utf-8 -*-
__doc__="""
Propagate selected paths to all other masters.
"""

# Ethan Cohen. Updated 9/16/2020.

import copy

from GlyphsApp import *

class CopySelectionToOtherMasters(object):

  def __init__(self, sender):
    self.run()

  def run(self):
    f = Glyphs.font
    l = f.selectedLayers[0]
    g = l.parent

    for layer in g.layers:
      if layer != l:
        for i in range(len(l.paths)):
          if l.paths[i].selected:
            #layer.paths.insert(i, l.paths[i].copy())
            layer.shapes.insert(i, l.shapes[i].copy())

    Glyphs.redraw()