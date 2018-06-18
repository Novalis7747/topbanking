# -*- coding: UTF-8 -*-
# topbanking: a NVDA appModule for topbanking booking listviews
#Copyright (C) 2018 Ralf Kefferpuetz
# Released under GPL 2

import appModuleHandler
from NVDAObjects.IAccessible import IAccessible
import speech
import controlTypes
import ui
import scriptHandler

"""
topbanking enhanced Version 0.2 
Author: Ralf Kefferpuetz, June 2018
Features:
- reducing speaking of the cell grid to its value
- adds a hotkey Alt-1 to read the cell header and line number
"""

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		#if obj.windowClassName in ("WindowsForms10.Window.8.app.0.34dca42_r6_ad1", "WindowsForms10.Window.8.app.0.7f9478_r6_ad1"):
		if obj.windowClassName.startswith('WindowsForms10.Window.'):
			clsList.insert(0, TBGrid)

class TBGrid(IAccessible):

	def event_gainFocus(self):
		if self.windowClassName.startswith('WindowsForms10.Window.'):
			if self.IAccessibleRole == 29:
				ui.message(self.value)
				return
		super(TBGrid,self).event_gainFocus()

	def script_readActive(self, gesture):
		try:
			ui.message(self.name)
		except:
			pass
	# Translators: Documentation for Alt-1 script.
	script_readActive.__doc__=_("topbanking enhanced: speaks header and line number of the current cell.")

	__gestures = {
		"kb:alt+1": "readActive"
	}
