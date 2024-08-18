import os, glob, random
from libqtile.lazy import lazy

backends = [
    'schemer2',
    'colorz',
    'wal',
    'haishoku',
    'colorthief',
]

def set_random_wallpaper(qtile, backend=None, imgdir='/home/sheffler/.config/wallpaper', rand=True, **kw):
    if backend or not rand:
        set_wallpaper(qtile, glob.glob('/home/sheffler/.wallpaper.*')[0], backend, **kw)
    else:
        wallpapers = [os.path.join(imgdir, x) for x in os.listdir(imgdir)]
        fname = random.choice(wallpapers)
        ext = fname.split('.')[-1]
        os.system('rm -f /home/sheffler/.wallpaper.*')
        os.symlink(fname, f'/home/sheffler/.wallpaper.{ext}')
        set_wallpaper(qtile, f'/home/sheffler/.wallpaper.{ext}', **kw)

def set_wallpaper(qtile, fname, backend=None, mode='fill', **kw):
    if not backend:
        backend = random.choice(backends)
    os.system(f'wal -i {fname} -o /home/sheffler/.config/qtile/pywal_sublime.py --saturate 100 --cols16 --backend {backend}')
    for screen in qtile.screens:
        screen.set_wallpaper(fname, mode='fill', **kw)

@lazy.function
def lazy_set_wallpaper(qtile, backend=None, **kw):
    set_random_wallpaper(qtile, backend=None, **kw)
