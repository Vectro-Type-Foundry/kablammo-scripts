# This collapses handles/off-curve points and place it on parent node. 
# Only applies to selected points. 
# Keeps it as a curve. 
# Useful for the gashes, in so the handles come straight out during interpolation.

from GlyphsApp import *

class CollapseHandles(object):

  def __init__(self, sender):
    self.currentLayer = Glyphs.font.selectedLayers[0]
    self.run()

  def getParentNode(self, node):
    if node.nextNode.type != 'offcurve':
      return node.nextNode
    else:
      return node.prevNode

  def collapseNodeFromHandle(self, node):
    parentNode = self.getParentNode(node)
    node.x = parentNode.position.x
    node.y = parentNode.position.y
    # print(node)

  def collapseHandlesFromNode(self, node):
    if node.prevNode.type == 'offcurve':
      self.collapseNodeFromHandle(node.prevNode)
    if node.nextNode.type == 'offcurve':
      self.collapseNodeFromHandle(node.nextNode)

  def run(self):
    self.currentLayer.parent.beginUndo()
    for path in self.currentLayer.paths:
      for node in path.nodes:
        if node.selected and node.type == 'offcurve':
          self.collapseNodeFromHandle(node)
        elif node.selected:
          self.collapseHandlesFromNode(node)
    self.currentLayer.parent.endUndo()
