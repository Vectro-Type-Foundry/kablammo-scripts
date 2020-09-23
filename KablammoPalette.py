#MenuTitle: KablammoPalette
# -*- coding: utf-8 -*-
__doc__="""
Brings up window with easy access to all scripts
"""

from vanilla import *
from CollapseHandles import *
from CollapseShape import *
from SyncToFirstLayerSelected import *
from DuplexWarnings import *
from UseLayerForAllMasters import *
from CopySelectionToOtherMasters import * 
from DeleteSelectionInAllMasters import *
from SynchronizeNodeSelection import *

class KablammoPalette(object):

  def __init__(self):
    self.w = Window((200, 310), "Kablammo Palette", minSize=(100, 100))
    self.w.g1 = Group((10, 10, -10, -10))

    bHeight = 27
    bSize = "small"
    margin = 10 + bHeight
    y = 0

    self.w.g1.collapseHandles = SquareButton((0, y, 0, bHeight), "Collapse Handles", sizeStyle=bSize, callback=CollapseHandles)

    y+=margin

    self.w.g1.collapseShape = SquareButton((0, y, 0, bHeight), "Collapse Shape", sizeStyle=bSize, callback=CollapseShape)

    y+=margin

    self.w.g1.UseLayerForAllMasters = SquareButton((0, y, 0, bHeight), "Use Current Layer for All", sizeStyle=bSize, callback=UseLayerForAllMasters)

    y+=margin

    self.w.g1.copyFirstLayerToAllSelected = SquareButton((0, y, 0, bHeight), "Use 1st Layer for All, Selected Glyphs", sizeStyle=bSize, callback=SyncToFirstLayerSelected)

    y+=margin

    self.w.g1.CopySelectionToOtherMasters = SquareButton((0, y, 0, bHeight), "Copy Selection to All Masters", sizeStyle=bSize, callback=CopySelectionToOtherMasters)

    y+=margin

    self.w.g1.DeleteSelectionInAllMasters = SquareButton((0, y, 0, bHeight), "Delete Selection in All Masters", sizeStyle=bSize, callback=DeleteSelectionInAllMasters)

    y+=margin


    self.w.g1.SynchronizeNodeSelection = SquareButton((0, y, 0, bHeight), "Sync Node Selection", sizeStyle=bSize, callback=SynchronizeNodeSelection)

    y+=margin

    self.w.g1.duplexWarnings = SquareButton((0, y, 0, bHeight), "Duplex Warnings", sizeStyle=bSize, callback=DuplexWarnings)
    
    y+=margin

    


    self.w.open()

  def test(self, v):
    DuplexWarnings()

KablammoPalette()