# === Stage 19: Add undo support for the last simple mutation ===
# Project: ClassroomBook
import json

class UndoStack:
    def __init__(self):
        self.history = []
        self.index = -1

    def push(self, state):
        self.history.append(state)
        self.index += 1

    def undo(self):
        if self.index < 0:
            return None
        self.index -= 1
        return self.history[self.index]

    def redo(self):
        if self.index >= len(self.history) - 1:
            return None
        self.index += 1
        return self.history[self.index]

    def clear(self):
        self.history.clear()
        self.index = -1

    def snapshot(self, data):
        self.history = [json.loads(json.dumps(data))]
        self.index = 0
