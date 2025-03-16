import sublime
import sublime_plugin

class MyMoveLineCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10, extend=False):
        # row, col = self.view.rowcol(self.view.sel()[0].begin())
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("move", {'by': 'lines', 'forward': fwd, 'extend': extend})

class MySelectLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10):
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("select_lines", {'forward': fwd})
