import sublime, sublime_plugin

class HistoryManager():
    History = []
    def __init__(self):
        self.History = list()

    def pushToHistory(self, point):
        self.History.append(point)

    def clearHistory(self):
        del self.History[:]

    def getHistory(self):
        return self.History

HistoryMan = HistoryManager()

class CurSave(sublime_plugin.TextCommand):
    def run(self, edit, forward):
        for i in range(len(self.view.sel())):
            if forward:
                HistoryMan.pushToHistory(self.view.sel()[i].b)
            else:
                HistoryMan.pushToHistory(self.view.sel()[i].a)


class CurLoad(sublime_plugin.TextCommand):
    def run(self, edit):
        MyList = HistoryMan.getHistory()
        for i in range(len(MyList)):
            self.view.sel().add(sublime.Region(MyList[i], MyList[i]))
        HistoryMan.clearHistory()
