# Add Handles To Straight Segments

# thisPath.insertNodeWithPathTime_(pathTime)

from GlyphsApp import *
from Foundation import *


class AddHandlesToStraightSegments(object):

  def __init__(self, sender):
    self.run()

  def run(self):
    layer = Glyphs.font.selectedLayers[0]

    for path in layer.paths:
      if path.selected: 
        for aNode in path.nodes:
          if aNode and (aNode.type == 'line'):
            aPath = aNode.parent
            Index = aPath.nodes._owner.pyobjc_instanceMethods.nodes().index(aNode)
            PreviousNode = aPath.nodes[Index-1]
            
            newNode = GSNode()
            newNode.type = GSOFFCURVE
            newNode.position = NSMakePoint( PreviousNode.x + ((aNode.x-PreviousNode.x) / 3 * 2), PreviousNode.y + ((aNode.y-PreviousNode.y) / 3 * 2) )
            aPath.insertNode_atIndex_(newNode, Index)
            
            newNode = GSNode()
            newNode.type = GSOFFCURVE
            newNode.position = NSMakePoint( PreviousNode.x + ((aNode.x-PreviousNode.x) / 3), PreviousNode.y + ((aNode.y-PreviousNode.y) / 3) )
            aPath.insertNode_atIndex_(newNode, Index)
              
            aNode.type = GSCURVE