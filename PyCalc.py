# coding: utf-8
# TBD: place some useful comment here!

from __future__ import division
import ui
import string
from math import pi, e, cos, sin

def media(*values):
        if (not values):
                return None
        else:
                _media = 0

                for value in values:
                        _media += value

                return _media / len(values)


class PyCalc(object):
        def __init__(self):
                self._ui = ui.load_view("PyCalc")
                self._formula = ""
                self._result = "0"

        def update_ui(self):
                self._ui["ui.widget.label.formula"].text = self._formula
                self._ui["ui.widget.label.result"].text = self._result

        def start(self):
                self.update_ui()
                self._ui.present("fullscreen")

        def button_tapped(self, sender):
                if (sender.title == "x"):
                        self._formula += "*"
                elif (sender.title == "^"):
                        self._formula += "**"
                elif (sender.title in "01234567890.+-/[()],"):
                        self._formula += sender.title
                elif (sender.title == "R"):
                        self._formula += self._result
                elif (sender.title == "C"):
                        self._formula = ""
                elif (sender.title == "AC"):
                        self._formula = ""
                        self._result = "0"
                elif (sender.title == "<"):
                        self._formula = self._formula[:-1]
                elif (sender.title == "="):
                        try:
                                if (self._formula):
                                        self._result = "{:.10f}".format(float(str(eval(self._formula))))
                                        splitIdx = string.find(self._result, ".")+2
                                        self._result = self._result[0:splitIdx] + string.rstrip(self._result[splitIdx:],"0")

                                        self._result = str(eval(self._formula))
                                        self._formula = ""
                        except:
                                self._result = "ERROR"
                else:
                        self._formula += sender.title

                self.update_ui()

if (__name__ == "__main__"):
        app = PyCalc()
        app.start()
