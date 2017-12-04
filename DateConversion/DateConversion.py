import sublime
import sublime_plugin
import datetime

class UnixTimeConvert(sublime_plugin.TextCommand):
    def run(self, edit):
        for curSel in self.view.sel():
            inputRegion = self.view.expand_by_class(curSel, sublime.CLASS_WORD_START | sublime.CLASS_WORD_END, " ,\"")
            startingPoint = inputRegion.a
            inputStr = self.view.substr(inputRegion)
            print("input string:" + inputStr)
            outputStr = datetime.datetime.fromtimestamp(int(inputStr)).strftime('%Y-%m-%d %H:%M:%S')
            self.view.erase(edit, inputRegion)
            self.view.insert(edit, startingPoint, outputStr)

