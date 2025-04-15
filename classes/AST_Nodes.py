# classes/AST_Nodes.py

class ASTNode:
    pass

class PlayNode(ASTNode):
    def __init__(self, note, duration):
        self.note = note
        self.duration = duration

    def __repr__(self):
        return f"PlayNode(note={self.note}, duration={self.duration})"

class SetTempoNode(ASTNode):
    def __init__(self, tempo):
        self.tempo = tempo

    def __repr__(self):
        return f"SetTempoNode(tempo={self.tempo})"

class LoopNode(ASTNode):
    def __init__(self, times, commands):
        self.times = times
        self.commands = commands

    def __repr__(self):
        return f"LoopNode(times={self.times}, commands={self.commands})"
