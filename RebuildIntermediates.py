# Abandoned, because found a native way to do this in Glyphs. But keeping here for reference.
# Might be nice to write a script that is able to reinterpolate a specific contour, while leaving everything else. Or to do this in bulk.



# font = Glyphs.font
        
# def masterAxesVals(master):
#   return [{'Tag': font.axes[i]['Tag'], 'value': x} for i,x in enumerate(master.axes)]

# def getIntermediateMasters():
#   for master in font.masters:
#     if master.customParameters['isIntermediate'] == 'True':
#       print(masterAxesVals(master))

# def main():
#   getIntermediateMasters()
#   # for glyph in font.selection:
#   #   print(glyph.name)


# main()