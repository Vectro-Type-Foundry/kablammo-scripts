#MenuTitle: Collapse Handles (Kablammo)

# This collapses handles/off-curve points and place it on parent node. 
# Only applies to selected points. 
# Keeps it as a curve. 
# Useful for the gashes, in so the handles come straight out during interpolation.

import GlyphsApp

currentLayer = Glyphs.font.selectedLayers[0]

def getParentNode(node):
  if node.nextNode.type != 'offcurve':
    return node.nextNode
  else:
    return node.prevNode

def collapseNodeFromHandle(node):
  parentNode = getParentNode(node)
  node.x = parentNode.position.x
  node.y = parentNode.position.y
  # print(node)

def collapseHandlesFromNode(node):
  if node.prevNode.type == 'offcurve':
    collapseNodeFromHandle(node.prevNode)
  if node.nextNode.type == 'offcurve':
    collapseNodeFromHandle(node.nextNode)

def main():
  currentLayer.parent.beginUndo()
  for path in currentLayer.paths:
    for node in path.nodes:
      if node.selected and node.type == 'offcurve':
        collapseNodeFromHandle(node)
      elif node.selected:
        collapseHandlesFromNode(node)
  currentLayer.parent.endUndo()
main()