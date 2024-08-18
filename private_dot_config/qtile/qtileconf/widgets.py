import subprocess
import math
import psutil
from qtile_extras import widget
from qtileconf.theme import colors

class CPU(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "{}%𒁈"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = int(psutil.cpu_percent())
        self.foreground = colors["red"] if data > 75 else colors["lightgreen"]
        return f'{data}'

class CPUFreq(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "{}㎓"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = psutil.cpu_freq().current / 1000
        self.foreground = colors["red"] if data > 3.5 else colors["lightgreen"]
        return f"{data:5.3f}"

def gpuinfo(data, field, flen):
    i = data.find(f"Attribute '{field}'".encode()) + len(field)
    return data[i:i + flen]

class GPU(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "𒁈{}"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        # UTILIZATION, ECC, TEMPERATURE, POWER, CLOCK,
        # COMPUTE, PIDS, PERFORMANCE, SUPPORTED_CLOCKS,
        # PAGE_RETIREMENT, ACCOUNTING, ENCODER_STATS,
        # SUPPORTED_GPU_TARGET_TEMP, VOLTAGE, FBC_STATS
        # ROW_REMAPPER, RESET_STATUS, GSP_FIRMWARE_VERSION
        data = subprocess.check_output([
            'nvidia-smi', '--query-gpu=utilization.gpu,utilization.memory,temperature.gpu,clocks.current.sm',
            '--format=csv'
        ]).decode().replace(' ', '').replace(',', ' ').split('\n')[1]
        return f"{data}"

class MEM(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "📟{}%"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = int(psutil.virtual_memory().percent)
        self.foreground = colors["red"] if data > 75 else colors["lightgreen"]
        return f'{data}'

class CPUTemp(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "🌡️{}°C"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = int(psutil.sensors_temperatures()["coretemp"][0].current)
        self.foreground = colors["red"] if data > 8 else colors["lightgreen"]
        return str(data)

class Disk(widget.GenPollText):
    def __init__(self, path, **config):
        self.path = path
        config['fmt'] = " 🖴{}%"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = psutil.disk_usage(self.path).percent
        self.foreground = colors["red"] if data > 80 else colors["lightgreen"]
        return f"{self.path}{int(math.ceil(data)):2}"

class Fan(widget.GenPollText):
    def __init__(self, **config):
        config['fmt'] = "𖣘{}"
        config['update_interval'] = 1
        widget.GenPollText.__init__(self, **config)

    def poll(self):
        data = subprocess.check_output(['razer-cli', 'read', 'fan', 'ac']).decode()
        data = data.split("\n")[1].split()[-2]
        if data != 'Auto':
            data = int(data)
            self.foreground = colors["red"] if data > 4000 else colors["lightgreen"]
            return f"{data:4}rpm"
        return data

class MouseOverClock(widget.Clock):
    defaults = [("long_format", "%Y-%m-%d %a %I:%M %p")]

    def __init__(self, **config):
        widget.Clock.__init__(self, **config)
        self.add_defaults(MouseOverClock.defaults)
        self.short_format = self.format

    def mouse_enter(self, *args):
        self.format = self.long_format
        self.bar.draw()

    def mouse_leave(self, *args):
        self.format = self.short_format
