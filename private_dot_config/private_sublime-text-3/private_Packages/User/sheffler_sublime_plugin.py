import sublime
import sublime_plugin
import subprocess
import os
import re
from typing import TYPE_CHECKING

def log(msg):
    with open('/home/sheffler/.local/log/sublime_plugin.log', 'a') as f:
        f.write(msg + '\n')

def get_project_root(path: str):
    # Search upward for pyproject.toml to detect project root
    current = os.path.abspath(path)
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return current, os.path.basename(current)
        current = os.path.dirname(current)
    return '/', ''

class WhsRunShellCommandCommand(sublime_plugin.WindowCommand):

    def run(self, cmd="echo Hello from shell"):
        log(f'shell run "{cmd}"')
        try:
            subprocess.Popen(cmd, shell=True)
        except Exception as e:
            sublime.error_message(f"Shell command failed: {e}")

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

class WhsSelectLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10):
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("select_lines", {'forward': fwd})

class WhsOpenProjectFileCommand(sublime_plugin.TextCommand):

    def run(self, edit, file):
        current_file = self.view.file_name()
        if not current_file: return
        projroot, projname = get_project_root(current_file)
        file = file.replace('[projname]', projname)
        projfile = os.path.join(projroot, file)
        if os.path.exists(projfile):
            self.view.window().open_file(projfile)

class WhsSwapSourceTestCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        current_file = self.view.file_name()
        if not current_file: return
        projroot, _projname = get_project_root(current_file)
        if not projroot: return
        relative_path = os.path.relpath(current_file, projroot)
        parts = relative_path.split(os.sep)
        if "tests" in parts:
            parts.remove("tests")
            parts[-1] = parts[-1].replace("test_", "")
        else:
            parts.insert(1, "tests")
            parts[-1] = f"test_{parts[-1]}"
        related_path = os.path.join(*parts)
        related_file = os.path.join(projroot, related_path)
        if os.path.exists(related_file): self.view.window().open_file(related_file)

    def is_enabled(self):
        return self.view.file_name() is not None

class WhsMoveLineCommand(sublime_plugin.TextCommand):

    def run(self, edit, lines=10, extend=False):
        # row, col = self.view.rowcol(self.view.sel()[0].begin())
        fwd, lines = lines > 0, abs(lines)
        for _ in range(lines):
            self.view.run_command("move", {'by': 'lines', 'forward': fwd, 'extend': extend})

class WhsLastResultCommand(sublime_plugin.TextCommand):

    def run(self, edit, forward=True, num_steps=30):
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
    new_y = layout_y + amount*line_height
    new_y = max(0, min(new_y, max_scroll_y))

    view.set_viewport_position((layout_x, new_y), animate=False)

# # WATCHED_FILE = "/home/sheffler/evn/ide/sublime_output.log"

# # class FilePoller(sublime_plugin.EventListener):
# #     last_mtime = None

# #     def on_activated_async(self, view):

# #         def poll():
# #             try:
# #                 mtime = os.path.getmtime(WATCHED_FILE)
# #                 if self.last_mtime is None:
# #                     self.last_mtime = mtime
# #                 elif mtime != self.last_mtime:
# #                     self.last_mtime = mtime
# #                     for window in sublime.windows():
# #                         for v in window.views():
# #                             if v.file_name() == WATCHED_FILE:
# #                                 window.focus_view(v)
# #                                 v.run_command("revert")
# #             finally:
# #                 sublime.set_timeout_async(poll, 50)

# #         poll()

# # class WhsMoveLineCommand(sublime_plugin.TextCommand):

# #     def run(self, edit, lines=10, extend=False):
# #         # row, col = self.view.rowcol(self.view.sel()[0].begin())
# #         fwd, lines = lines > 0, abs(lines)
# #         for _ in range(lines):
# #             self.view.run_command("move", {'by': 'lines', 'forward': fwd, 'extend': extend})

class AutoFoldOnLoad(sublime_plugin.EventListener):

    def on_load_async(self, view):
        self.fold(view)

    def on_activated_async(self, view):
        self.fold(view)

    def on_post_save_async(self, view):
        self.fold(view)

    def fold(self, view):
        # foo
        #
        #
        if view.match_selector(0, "source.python"):
            # view.run_command("toggle_fold_comments")
            view.run_command("unfold_all")
            # view.run_command("fold_by_level", {"level": 3})
            view.run_command("fold_python_docstrings")
            view.run_command("whs_fold_type_checking")
            # fold_type_checking_blocks(view)

# class WhsFoldTypeCheckingCommand(sublime_plugin.TextCommand):

#     def run(self, edit):
#         fold_type_checking_blocks(self.view)

# def fold_type_checking_blocks(view):
#     log('fold_type_checking_blocks')
#     regions_to_fold = []

#     # pattern = r"^\s*if\s+\S*TYPE_CHECKING\s*:\s*$"
#     pattern = r"^.*TYPE_CHECKING.*$"
#     matches = view.find_all(pattern)
#     for match in matches:
#         line = view.line(match)
#         line_start = line.begin()
#         block_start = line.end() + 1  # After the colon/newline
#         indent_level = get_indent_level(view, line_start)
#         block_end = block_start
#         prev_line = '             aeirstoiarn'
#         for _ in range(100):
#             current_line = view.line(block_end)
#             current_indent = get_indent_level(view, current_line.begin())
#             if (current_indent <= indent_level
#                     and (view.substr(current_line).strip() != "" or view.substr(prev_line).strip() != "")):
#                 break
#             block_end = current_line.end()
#             prev_line = current_line

#         if block_end > block_start:
#             fold_region = sublime.Region(block_start, block_end)
#             regions_to_fold.append(fold_region)

#     view.fold(regions_to_fold)

# def get_indent_level(view, point):
#     line = view.line(point)
#     line_text = view.substr(line)
#     return len(line_text) - len(line_text.lstrip())

# if TYPE_CHECKING:
#     1 + 1
#     1 + 1
#     1 + 1
