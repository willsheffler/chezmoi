from typing import List
from kitty.boss import Boss
from kittens.tui.handler import result_handler

def main():
    pass

@result_handler(no_ui=True)
def handle_result(args: List[str], answer: str, target_window_id: int, boss: Boss) -> None:
    # get the kitty window into which to paste answer
    w = boss.window_id_map.get(target_window_id)
    w.paste_text('ldisndk020\n')
