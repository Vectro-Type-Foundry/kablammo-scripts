#MenuTitle: Variable Animator (Kablammo)
# -*- coding: utf-8 -*-
__doc__="""
Plays a glyph in Preview.
"""
import vanilla, threading, time, os
import objc

# Modified version of Rainer's OT Var Player, to allow for multiple axes, custom keyframes, and multiple selectible animations to choose from.

# Define axes of the font here. Note that if axes don't match font, it may throw errors. Not much fallback and error handling has been added.
fontAxes = [
  {
    "axisIndex": 0,
    "tag": "move",
    "minVal": 1,
    "maxVal": 1000
  }
]

# List keyframes for the animation, similar to CSS animation. Use decimal percent for intermediate steps.
animation1 = list([
  {
    "pct": 0,
    "axes": {
      "move": 1
    }
  },
  {
    "pct": 1,
    "axes": {
      "move": 1000
    }
  }
])

# multiple animations can be added here, which will show up in dropdown
animationOptions = [
  {
    "name": "movement",
    "animation": animation1
  }
]

def saveFileInLocation( content="blabla", fileName="test.txt", filePath="~/Desktop" ):
  saveFileLocation = "%s/%s" % (filePath,fileName)
  saveFileLocation = saveFileLocation.replace( "//", "/" )
  f = open( saveFileLocation, 'w' )
  print "Exporting to:", f.name
  f.write( content )
  f.close()
  return True

class OTVarGlyphAnimator( object ):
  def __init__( self ):
    # Window 'self.w':
    windowWidth  = 350
    windowHeight = 90
    windowWidthResize  = 700 # user can resize width by this value
    windowHeightResize = 0   # user can resize height by this value

    self.w = vanilla.FloatingWindow(
      ( windowWidth, windowHeight ), # default window size
      "Kablammo Animation Player", # window title
      minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
      maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
      autosaveName = "com.mekkablue.OTVarGlyphAnimator.mainwindow" # stores last window position and size
    )
    
    # UI elements:
    self.w.slider = vanilla.Slider( (15,12,-15,15), tickMarkCount=None, callback=self.redrawPreview, continuous=True, sizeStyle="regular", minValue=0, maxValue=100 )
    self.w.slower = vanilla.Button((15, -20-15, 32, -15), u"🚶", sizeStyle='regular', callback=self.slower )
    self.w.slower.getNSButton().setToolTip_("Slower")
    self.w.faster = vanilla.Button((50, -20-15, 32, -15), u"🏃", sizeStyle='regular', callback=self.faster )
    self.w.faster.getNSButton().setToolTip_("Faster")
    self.w.backAndForth = vanilla.CheckBox( (90, -20-15, 50, -15), u"⇋", value=False, callback=self.SavePreferences, sizeStyle='small' )
    
    
    self.w.animationOption = vanilla.ComboBox((125,-35, 120,-15), map(lambda x: x["name"], animationOptions),
        callback=self.animationOptionSelect)
    self.w.animationOption.set("movement")

    # web button:
    # self.w.buildWeb = vanilla.Button((-140,-35, -100,-15), u"🌍", sizeStyle='regular', callback=self.buildWeb )
    
    # Run Button:
    self.w.runButton = vanilla.Button((-95, -35, -15, -15), "Play", sizeStyle='regular', callback=self.togglePlay )
    self.w.runButton.getNSButton().setToolTip_("Toggle Play/Pause")
    self.w.setDefaultButton( self.w.runButton )
    
    # Load Settings:
    if not self.LoadPreferences():
      print "Note: 'OTVar Glyph Animator' could not load preferences. Will resort to defaults"
    
    self.direction = 1
    self.font = Glyphs.font
    self.originalAxesValue = None
    self.isPlaying = False
    if self.font.instances:
      self.originalAxesValue = self.previewInstance().axes
    self.w.bind("close",self.restoreFont)

    
    # open and initialize the preview area at the bottom
    self.redrawPreview(None)
    
    # Open window and focus on it:
    self.w.open()
    self.w.makeKey()
  
  def windowIsClosing(self):
    try:
      self.isPlaying = False
      Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.slider"] = "0"
      return True
    except Exception as e:
      Glyphs.clearLog()
      Glyphs.showMacroWindow()
      print e
      print
      import traceback
      print traceback.format_exc()
      return False
    
  def SavePreferences( self, sender ):
    try:
      Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.slider"] = self.w.slider.get()
      Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.backAndForth"] = self.w.backAndForth.get()
    except:
      return False
      
    return True

  def LoadPreferences( self ):
    try:
      Glyphs.registerDefault("com.mekkablue.OTVarGlyphAnimator.slider", 0)
      Glyphs.registerDefault("com.mekkablue.OTVarGlyphAnimator.delay", 0.05)
      Glyphs.registerDefault("com.mekkablue.OTVarGlyphAnimator.backAndForth", False)
      self.w.slider.set( Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.slider"] )
      self.w.backAndForth.set( Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.backAndForth"] )
    except:
      return False
      
    return True
  
  def setupWindow(self):
    if not self.font.tabs:
      tabText = "a"
      if self.font.selectedLayers:
        tabText = "".join([l.parent.name for l in self.font.selectedLayers])
      self.font.newTab(tabText)
    if self.font.currentTab.previewHeight <= 1.0:
      self.font.currentTab.previewHeight = 200
    if not self.font.instances:
      newInstance = GSInstance()
      newInstance.name = "Preview"
      self.font.instances.append(newInstance)
    self.font.currentTab.previewInstances = self.previewInstance()
  
  def restoreFont(self, sender):
    if not self.originalAxesValue is None:
      self.previewInstance().axes = self.originalAxesValue
    else:
      self.font.instances = []
      
    # turn playing off when window is closed, otherwise it goes on forever:
    self.isPlaying = False
    
    # reset slider and redraw the preview area:
    Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.slider"] = 0
    Glyphs.redraw()

  def previewInstance(self):
    return next(i for i in self.font.instances if i.name == 'Preview')

  def animationOptionSelect(self, sender):
    self.w.animationOption.set(sender.get())

  def getSelectedAnimationOption(self):
    return next(opt for opt in animationOptions if opt["name"] == self.w.animationOption.get())

  def relevantKeyframes(self, sliderPos):
    animationOption = self.getSelectedAnimationOption()
    minKeyframe = list(filter(lambda x: x["pct"] <= sliderPos, animationOption["animation"]))
    maxKeyframe = list(filter(lambda x: x["pct"] >= sliderPos, animationOption["animation"]))
    return minKeyframe[len(minKeyframe)-1], maxKeyframe[0]

  def pctBetweenKeyframes(self, sliderPos, keyframes):
    frameSpan = keyframes[1]["pct"] - keyframes[0]["pct"]
    if frameSpan == 0:
        frameSpan = 1
    return (sliderPos - keyframes[0]["pct"]) / frameSpan

  def axisValsAtPct(self, pct, keyframes):
    axes = []
    for axis in keyframes[0]['axes']:
        minVal = keyframes[0]['axes'][axis]
        maxVal = keyframes[1]['axes'][axis]
        val = float((maxVal - minVal) * pct + minVal)
        axes.append({"tag": axis, "val": val})
    return axes

  def getAxisIndex(self, tag):
    axis = next(axis for axis in fontAxes if axis["tag"] == tag)
    return axis["axisIndex"]

  def setAxisVals(self, sliderPos):
    keyframes = self.relevantKeyframes(sliderPos)
    pct = self.pctBetweenKeyframes(sliderPos, keyframes)
    axisVals = self.axisValsAtPct(pct, keyframes)
    for axisVal in axisVals:
      axisIndex = self.getAxisIndex(axisVal["tag"])
      self.previewInstance().axes[axisIndex] = axisVal["val"]

  def redrawPreview( self, sender ):
    try:
      self.setupWindow()
      
      sliderPos = self.w.slider.get() / 100.0
      weights = [m.axes[0] for m in self.font.masters]
      if self.font.customParameters["Virtual Master"]:
        weights.append(self.font.customParameters["Virtual Master"][0]["Location"])
      minWt = min(weights) or 0
      maxWt = max(weights) or 0

      # print(minWt, sliderPos, maxWt, minWt)
      sliderWt = minWt + sliderPos * (maxWt - minWt)
      
      # apply to preview instance and redraw
      self.setAxisVals(sliderPos)
      self.font.currentTab.updatePreview()
      
      if not self.SavePreferences( self ):
        print "Note: 'OTVar Glyph Animator' could not write preferences."
    except Exception, e:
      # brings macro window to front and reports error:
      Glyphs.showMacroWindow()
      print "OTVar Glyph Animator Error: %s" % e
      import traceback
      print traceback.format_exc()

  def togglePlay(self, sender):
    self.w.makeKey()
    self.isPlaying = not self.isPlaying
    if self.isPlaying:
      self.w.runButton.setTitle("Pause")
      self.play_(None)
    else:
      self.w.runButton.setTitle("Play")
      self.font.currentTab.previewInstances = 'live'

  def play_( self, sender ):
    try:
      if not bool(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.backAndForth"]):
        self.direction = 1
      
      # finer steps when played slowly:
      smoothnessFactor = 1
      if float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"]) > 0.07:
        smoothnessFactor = 3
      elif float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"]) > 0.05:
        smoothnessFactor = 2
      
      # execute an animation step:
      if self.isPlaying:
        # Move Slider:
        sliderPos = self.w.slider.get()
        if sliderPos >= 100:
          if not bool(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.backAndForth"]):
            sliderPos = 0
          else:
            sliderPos = 99.9999
            self.direction = -1
        elif sliderPos <= 0:
          sliderPos = 0.0001
          if self.direction == -1:
            self.direction = 1
          
        else:
          sliderPos += self.direction * 2.0/smoothnessFactor
        self.w.slider.set( sliderPos )
        
        # Trigger Redraw:
        self.redrawPreview(None)
        self.font.currentTab.updatePreview()
        
        # Call this method again after a delay:
        playSignature = objc.selector(self.play_,signature='v@:')
        # self.timer = Timer(float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"])/smoothnessFactor, self.playSignature)

        self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
          float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"])/smoothnessFactor, # interval
          self, # target
          playSignature, # selector
          None, # userInfo
          False # repeat
        )
    except Exception, e:
      # brings macro window to front and reports error:
      Glyphs.showMacroWindow()
      print "OTVar Glyph Animator Error: %s" % e
      import traceback
      print traceback.format_exc()
      
  def slower(self, sender):
    delay = float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"])
    if delay <= 0.1:
      delay += 0.01
      self.w.faster.enable(onOff=True)
    else:
      # disable slower button at slowest setting:
      self.w.slower.enable(onOff=False)
    Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"] = delay
  
  def faster(self, sender):
    delay = float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"])
    if delay > 0.02:
      delay -= 0.01
      self.w.slower.enable(onOff=True)
    else:
      # disable faster button at fastest setting:
      self.w.faster.enable(onOff=False)
    Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"] = delay
  
  def buildWeb(self, sender):
    weightAxisPositions = []
    for m in self.font.masters:
      if m.customParameters["Axis Location"]:
        axisPos = m.customParameters["Axis Location"][0]["Location"]
      else:
        axisPos = m.axes[0]
      weightAxisPositions.append( int(axisPos) )
        
    if self.font.customParameters["Virtual Master"]:
      weightAxisPositions.append(self.font.customParameters["Virtual Master"][0]["Location"])
    
    firstAxisTag = "wght"
    if self.font.customParameters["Axes"]:
      firstAxisTag = self.font.customParameters["Axes"][0]["Tag"]

    htmlCode = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@font-face {
  font-family: "%s";
  src: url("%sGX.ttf");
}
@keyframes Looper {
  from {
    font-variation-settings: "%s" %i;
  }
  to {
    font-variation-settings: "%s" %i;
  }
}
body {
  font: 360px "%s";
  animation: Looper %.1fs linear 0s infinite;
}
</style>
</head>
<body>%s</body>
</html>""" % (
      self.font.familyName,
      self.font.familyName.replace(" ",""),
      firstAxisTag,
      min(weightAxisPositions),
      firstAxisTag,
      max(weightAxisPositions),
      self.font.familyName,
      float(Glyphs.defaults["com.mekkablue.OTVarGlyphAnimator.delay"]) * 50,
      " ".join( ["&#x%s;" % g.unicode for g in self.font.glyphs if g.unicode and g.export ] )
    )
    
    exportPath = None
    if bool(Glyphs.defaults["GXPluginUseExportPath"]):
      exportPath = Glyphs.defaults["GXExportPath"]
    else:
      exportPath = Glyphs.defaults["GXExportPathManual"]
      
    print "exportPath:", exportPath
    if exportPath:
      if saveFileInLocation( content=htmlCode, fileName="font_animation.html", filePath=exportPath ):
        print "Successfully wrote file to disk."
        terminalCommand = 'cd "%s"; open .' % exportPath
        os.system( terminalCommand )
      else:
        print "Error writing file to disk."
    else:
      Message( 
        title="Cannot Create HTML for OTVar",
        message="Could not determine export path of your OTVar font. Export an OTVar font first, the HTML will be saved next to it.",
        OKButton=None
      )
    
OTVarGlyphAnimator()