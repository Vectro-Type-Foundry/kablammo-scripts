#MenuTitle: Collapse Shape (Kablammo)

# This will collaps selected points into a single invisible point. 
# No points are lost, they just all sit at the same coordinate.
# This is useful for the interior spots that need to disappear at certain masters

import GlyphsApp

currentLayer = Glyphs.font.selectedLayers[0]

def selectedPaths(): 
  return filter(lambda x: x.selected , currentLayer.paths)
  
def getCenter(path):
  bounds = path.bounds
  x = bounds.origin.x + (bounds.size.width * 0.5)
  y = bounds.origin.y + (bounds.size.height * 0.5)
  return {'x': x, 'y': y}

def collapsePath(path):
  center = getCenter(path)
  for node in path.nodes:
    node.x = center['x']
    node.y = center['y']

def main():
  for path in selectedPaths():
    collapsePath(path)


main()