import sublime_plugin

class WhsMoveLineCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10, extend=False):
        # row, col = self.view.rowcol(self.view.sel()[0].begin())
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("move", {'by': 'lines', 'forward': fwd, 'extend': extend})

class WhsSelectLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10):
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("select_lines", {'forward': fwd})

class WhsLastResultCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=True, num_steps=10):
        window = self.view.window()
        if not window:
            print("[WhsLastResult] No window found")
            return
        for _ in range(num_steps):
            if forward:
                window.run_command("next_result")
            else:
                window.run_command("prev_result")
