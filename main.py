#By Lucas Frias KU EECS 268
# Lab 2 - Dated Feb 2nd 2026
#       <@
#       (KU//
#        "
# Rock Chalk!
# Home grown, no AI code with lots of comments

class Function:
    """Class to model functions and their output"""
    def __init__(self, name, canHandleExceptions):
        self.name = name
        self.canHandleExceptions = canHandleExceptions
        if type(self.name) != type("birds") or type(self.canHandleExceptions) != type(True):
            #I like birds, and this error handles incorrect inputs
            raise TypeError("Incorrect initialisation variables!")
#Let's define some Gibbons data type constructs
class Process:
    """Simulate computer program with process"""
    def __init__(self, name):
        self.name = name
        self.callStack = LinkedStack()





class SimulatedComputer:
    """To kind of simulate the main running of this comptuer"""
    def __init__(self):
        self.fileText = open(input("File >"), "r").read()
        self.process = None #there's only one process

    def command(self, command):
        """Processes command from file format given"""
        if command[:5] == "START":
            print(command[5:] + " Process started")
            self.process = Process(name=command[5:]) #make a process with that name
class Node:
    """Gibbons-styled Node"""
    def __init__(self, entry):
        """Creates a node"""
        self.entry = entry #set the node and by default next has no value
        self.next = None

class LinkedStack:
    """268 Required Stack that interacts with Gibbons Nodes"""
    def __init__(self):
        self._myNodes = [] #make it "hidden"
    def push(self, entry):
        """Put the entry at the top of the Stack."""
        self._myNodes[0:0] = [entry] #set the entry at a : iterator in a list at the zeroeth place zero times and set it equal to copy each value of entry
    def pop():
        """Remove and return the value at the top of the stack, 
        raise RuntimeError otherwise"""
        try:
            returnValue = self._myNodes[0] #save the value
            self._myNodes.pop(0)#remove the top index
            return returnValue
        except IndexError:
            raise RuntimeError("Stack is empty")
    def peek():
        """Return value at the top of the stack otherwise RuntimeError"""
        try:
            return self._myNodes[0]
        except IndexError:
            raise RuntimError("Stack is empty")
    def is_empty():
        """Returns true if stack is empty, false otherwise"""
        return True if len(self._myNodes) == 0 else False

if __name__ == "__main__":
    #someone's running this as a lab
    sim = SimulatedComputer()
    commands = sim.fileText.split("\n")
    for command in commands:
        sim.command(command)
