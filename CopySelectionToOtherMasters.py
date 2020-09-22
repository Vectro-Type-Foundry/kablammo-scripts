#MenuTitle: Copy selection to other masters
# -*- coding: utf-8 -*-
__doc__="""
Propagate selected paths to all other masters.
"""

# Ethan Cohen. Updated 9/16/2020.

import GlyphsApp
import copy

f = Glyphs.font
l = Font.selectedLayers[0]
g = l.parent

for layer in g.layers:
  if layer != l:
    for i in range(len(l.paths)):
      if l.paths[i].selected:
        layer.paths.insert(i, l.paths[i].copy())

Glyphs.redraw()