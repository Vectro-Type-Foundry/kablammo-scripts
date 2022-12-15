# Converts axis coordinates based on relationships outlined in top vars.
# To use, uncomment the method call at the bottom. Be careful, as this assumes the oldMinMax is the current value. Values could lose correct relationships if applied more than once, or with the wrong settings.

currentLayer = Glyphs.font.selectedLayers[0]
glyph = currentLayer.parent

oldMinMax = [1,1000]
newMinMax = [0,60]
oldRange = oldMinMax[1] - oldMinMax[0]
newRange = newMinMax[1] - newMinMax[0]

axisId = Glyphs.font.axes[0].axisId

def calcNewVal(oldVal):
	pct = (int(oldVal) - oldMinMax[0]) / (oldRange)
	return round((newRange * pct) + newMinMax[0])
	
def migrateSpecialLayerCoordinates():
	for glyph in Glyphs.font.glyphs:
		glyph.beginUndo()
		for layer in glyph.layers:
			if layer.isSpecialLayer:
				layerName = layer.name
				currentAxisVal = layerName[layerName.find("{")+1:layerName.find("}")]
				newAxisVal = calcNewVal(currentAxisVal)
				layer.attributes['coordinates'] = {axisId: newAxisVal }
				layer.name = '{'+ str(newAxisVal) +'}'
		glyph.endUndo()
			
#			

def showCurrentAxisVals():
	vals = []
	for glyph in Glyphs.font.glyphs:
		for layer in glyph.layers:
			if layer.isSpecialLayer:
				layerName = layer.name
				currentAxisVal = layerName[layerName.find("{")+1:layerName.find("}")]
				if currentAxisVal not in vals:
					vals.append(currentAxisVal)
	vals.sort()
	print(vals)


# migrateSpecialLayerCoordinates()
# showCurrentAxisVals()