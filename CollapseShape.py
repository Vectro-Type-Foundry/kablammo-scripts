# This will collaps selected points into a single invisible point. 
# No points are lost, they just all sit at the same coordinate.
# This is useful for the interior spots that need to disappear at certain masters

from GlyphsApp import * 

class CollapseShape(object):

  def __init__(self, sender):
    self.currentLayer = Glyphs.font.selectedLayers[0]
    self.run()

  def selectedPaths(self): 
    return filter(lambda x: x.selected , self.currentLayer.paths)
    
  def getCenter(self, path):
    bounds = path.bounds
    x = bounds.origin.x + (bounds.size.width * 0.5)
    y = bounds.origin.y + (bounds.size.height * 0.5)
    return {'x': x, 'y': y}

  def collapsePath(self, path):
    center = self.getCenter(path)
    for node in path.nodes:
      node.x = center['x']
      node.y = center['y']

  def run(self):
    for path in self.selectedPaths():
      self.collapsePath(path)


