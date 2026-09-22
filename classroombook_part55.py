# === Stage 55: Add a setting to disable colorized output ===
# Project: ClassroomBook
import os

class Settings:
    def __init__(self):
        self.colorize = os.environ.get("CLASSROOMBOOK_COLOR", "auto") == "auto"
        self.debug = os.environ.get("CLASSROOMBOOK_DEBUG", "false") == "true"
        self.quiet = os.environ.get("CLASSROOMBOOK_QUIET", "false") == "true"

    def set_colorize(self, enabled):
        self.colorize = enabled

    def set_debug(self, enabled):
        self.debug = enabled

    def set_quiet(self, enabled):
        self.quiet = enabled

    def is_colorized(self):
        if self.colorize == "auto":
            return os.environ.get("TERM", "") not in ("dumb", "") and sys.platform != "win32"
        return self.colorize

    def log(self, msg):
        if self.quiet:
            return
        if not self.colorize:
            print(msg)
        else:
            print("\033[32m" + msg + "\033[0m")

    def debug_log(self, msg):
        if not self.debug:
            return
        if not self.colorize:
            print("[DEBUG] " + msg)
        else:
            print("\033[36m[DEBUG] " + msg + "\033[0m")
