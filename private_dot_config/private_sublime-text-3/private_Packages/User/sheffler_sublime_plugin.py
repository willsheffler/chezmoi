import sublime
import sublime_plugin
import subprocess
import os

def get_project_root(path: str) -> str:
    # Search upward for pyproject.toml to detect project root
    current = os.path.abspath(path)
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return current
        current = os.path.dirname(current)
    return '/'

class WhsFormatPythonCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return self.view.match_selector(0, 'source.python')

    def run(self, edit):
        print('[WhsFormatPythonCommand] Running format on Python code', flush=True)
        region = sublime.Region(0, self.view.size())
        buffer_content = self.view.substr(region)
        old_sel = list(self.view.sel())
        old_viewport = self.view.viewport_position()
        # formatted_content = self.format_code(["ruff", "format", "-"], buffer_content)

        formatted_content = self.format_code(["/home/sheffler/.local/bin/evn", "-"], buffer_content)
        print(f'[WhsFormatPythonCommand] len: {len(formatted_content)}', flush=True)
        # formatted_content = 'iaeornoira'

        if formatted_content is not None and formatted_content != buffer_content:
            self.view.replace(edit, region, formatted_content)
            # self.view.sel().clear()
            # for sel in old_sel:
            # self.view.sel().add(sel)
            # self.view.set_viewport_position(old_viewport, False)

    def format_code(self, command, code):
        process = subprocess.run(command, input=code, text=True, capture_output=True, check=True)
        formatted_content = process.stdout
        return formatted_content

class AutoFoldOnLoad(sublime_plugin.EventListener):

    def on_load(self, view):
        if view.match_selector(0, "source.python"):
            # view.run_command("toggle_fold_comments")
            view.run_command("unfold_all")
            # view.run_command("fold_by_level", {"level": 3})
            view.run_command("fold_python_docstrings")
            # view.run_command("fold_comments")

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

class WhsOpenPyprojectCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file: return
        project_root = get_project_root(current_file)
        pyproj = os.path.join(project_root, 'pyproject.toml')
        if os.path.exists(pyproj):
            self.view.window().open_file(pyproj)

class WhsSwapSourceTestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file: return
        project_root = get_project_root(current_file)
        if not project_root: return
        relative_path = os.path.relpath(current_file, project_root)
        parts = relative_path.split(os.sep)
        if "tests" in parts:
            parts.remove("tests")
            parts[-1] = parts[-1].replace("test_", "")
        else:
            parts.insert(1, "tests")
            parts[-1] = f"test_{parts[-1]}"
        related_path = os.path.join(*parts)
        related_file = os.path.join(project_root, related_path)
        if os.path.exists(related_file): self.view.window().open_file(related_file)

    def is_enabled(self):
        return self.view.file_name() is not None

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

class WhsScrollAdjacentPaneCommand(sublime_plugin.WindowCommand):

    def run(self, direction="right", amount=10.0):
        assert 0
        window = self.window
        current_group = window.active_group()
        target_group = self._get_neighboring_group(direction)

        if target_group is None:
            return

        # Temporarily focus the target group to scroll it
        window.focus_group(target_group)
        view = window.active_view_in_group(target_group)

        if view: safe_scroll(view, amount)
            # view.run_command("scroll_lines", {"amount": amount})

        # Restore original group focus
        window.focus_group(current_group)

    def _get_neighboring_group(self, direction):
        layout = self.window.get_layout()
        cells = layout.get("cells", [])
        num_groups = len(cells)
        current_group = self.window.active_group()
        current_cell = cells[current_group]

        x1, y1, x2, y2 = current_cell

        def match(cell):
            cx1, cy1, cx2, cy2 = cell
            if direction == "right" and cy1 == y1 and cx1 == x2:
                return True
            if direction == "left" and cy1 == y1 and cx2 == x1:
                return True
            if direction == "down" and cx1 == x1 and cy1 == y2:
                return True
            if direction == "up" and cx1 == x1 and cy2 == y1:
                return True
            return False

        for idx, cell in enumerate(cells):
            if idx != current_group and match(cell):
                return idx
        return None

def safe_scroll(view, amount):
    """
    Scroll the view by a given number of visual lines, but not past the bottom
    of the buffer. Visual lines (wrapped lines) are respected.

    Parameters:
        view (sublime.View): The view to scroll.
        amount (int): The number of visual lines to scroll. Positive scrolls down.
    """
    layout_x, layout_y = view.viewport_position()
    line_height = view.line_height()
    viewport_height = view.viewport_extent()[1]

    # Total scrollable height is content height minus viewport
    content_height = view.layout_extent()[1]
    max_scroll_y = max(0, content_height - viewport_height)

    # Compute new y position and clamp it to max_scroll_y
    new_y = layout_y + amount * line_height
    new_y = max(0, min(new_y, max_scroll_y))

    view.set_viewport_position((layout_x, new_y), animate=False)


# WATCHED_FILE = "/home/sheffler/evn/ide/sublime_build.log"
#
# class FilePoller(sublime_plugin.EventListener):
    # last_mtime = None
    # timeout
    # def on_activated_async(self, view):
        # def poll():
            # try:
                # mtime = os.path.getmtime(WATCHED_FILE)
                # if self.last_mtime is None:
                    # self.last_mtime = mtime
                # elif mtime - self.last_mtime > 250:
                    # self.last_mtime = mtime
                    # for window in sublime.windows():
                        # for v in window.views():
                            # if v.file_name() == WATCHED_FILE:
                                # window.focus_view(v)
                                # v.run_command("revert")
            # finally:
                # sublime.set_timeout_async(poll, 50)
#
        # poll()
#
