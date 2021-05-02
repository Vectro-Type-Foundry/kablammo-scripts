__doc__="""
In selection, alert in console if any glyphs are not duplexed, or same width across masters.
"""

# Travis Kochel. Updated August 10, 2020.

from GlyphsApp import *
import re


class GlyphWarnings(object):

  def __init__(self, sender):
    Glyphs.showMacroWindow()
    self.run()

  def inconsistentWidths(self):
    print('Inconsistent Widths')
    primaryLayerNames = [m.name for m in Glyphs.font.masters]
    for glyph in Glyphs.font.glyphs:
      layers = [l for l in glyph.layers if (l.isMasterLayer or l.isSpecialLayer)]
      widths = [l.width for l in layers]
      if len(set(widths)) > 1:
        print(str(glyph.name) + ': ', widths)

  def badLayerNames(self):
    print('Bad Layer Names')
    for glyph in Glyphs.font.glyphs:
      for layer in glyph.layers:
        if 'off' in layer.name:
          print(glyph.name, layer.name)
        if '{' in layer.name:
          find = re.compile(r"^[^{]*")
          match = re.search(find, layer.name).group(0)
          if match:
            print(glyph.name, layer.name)


  def run(self):
    self.inconsistentWidths()
    self.badLayerNames()

