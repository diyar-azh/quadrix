op = True

def NewGame():
    board = quadboard()

def capture(rw, cl):
    board.capture(rw, cl, getOp())
    op = not op
    
def getOp():
    return 1 if op else -1