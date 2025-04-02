import sublime
import sublime_plugin


class show_hover_text(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime_plugin.on_hover(self.view.id(), self.view.sel()[0].begin(), sublime.HOVER_TEXT)
