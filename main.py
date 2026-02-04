#!/usr/bin/env python3
#By Lucas Frias KU EECS 268
# Lab 2 - Dated Feb 2nd 2026
#       <@
#       (KU//
#        "
# Rock Chalk!
# Home grown, no AI code with lots of comments
import sys

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
        self.name = name #sets name for parent process
        self.callStack = LinkedStack() #sets callstack as linkedstckmethod


class SimulatedComputer:
    """To kind of simulate the main running of this comptuer"""
    def __init__(self):
        self.fileText = open(input("File >"), "r").read()
        self.process = None #there's only one process

    def command(self, command):
        """Processes command from file format given"""
        if command[:5] == "START":
            #The process is created
            print(command[5:] + " Process started")
            self.process = Process(name=command[5:]) #make a process with that name
            #add main as the first function
            self.process.callStack.push(Function("main", False)) #you never specify
            #if this function has an error handler so i'm assuming nah
        if command[:4] == "CALL":
            funcName = command.split(" ")[1] #string split and 1st term is the function name
            funcCHE = True if "yes" in command.split(" ")[2] else False
            #CHE = can handle exceptions
            #function's bool (tertiary) which examines using in to avoid
            #string concat errors, resolves as boolean
            #then init a new function that pushes itself to the 
            #process call stack in the SIM
            self.process.callStack.push(Function(funcName, funcCHE))
            #terminal output
            print(self.process.name + " calls " + funcName + " function")
        if command [:6] == "RETURN":
            #removes a function from the callstack without erro
            poppedFunc = self.process.callStack.pop() #just pop the functon
            print(self.process.name + " has " + poppedFunc.entry.name + " return")
            #if we're at the end end it already
            if self.process.callStack.is_empty(): #handles exitting
                              print(self.process.name + " Process ended.")
                              sys.exit(0)
        if command[:5] == "RAISE":
            #as lane lamping says "oh boy"
            #this function is complicated
            self.process.hasException = True
            #now we go through all processes until we find
            #if and where there's an exception handler
            while not self.process.callStack.is_empty(): #make sure we don't read nothing
                if self.process.callStack.peek().entry.canHandleExceptions: #() returns the func
                    #and then we can access the values inside of the init class
                    print(self.process.name + " has "+ self.process.callStack.peek().entry.name + " handle the exception and keep running")
                    break
                else: #the function can't handle exceptions, pop off of stack and announce it
                    self.process.callStack.pop()
                    print(self.process.name + " pop " + self.process.callStack.peek().entry.name + " off call stack for unhanded exception")
                    #for the user to let me knowww let me knowwww




class Node:
    """Gibbons-styled Node"""
    def __init__(self, entry):
        """Creates a node"""
        self.entry = entry #set the node and by default next has no value
        self.next = None

class LinkedStack:
    """268 Required Stack that interacts with Gibbons Nodes"""
    def __init__(self):
        self._top = None
    def push(self, entry):
        """Put the entry at the top of the Stack."""
        previousNode = self._top #save the previous (formlery top) node
        self._top = Node(entry) #set the entry at a : iterator in a list at the zeroeth place zero times and set it equal to copy each value of entry
        self._top.next = previousNode
        #set previous node as next node fro linked list
    def pop(self):
        """Remove and return the value at the top of the stack, 
        raise RuntimeError otherwise"""
        returnValue = self._top #save the value
            #Errors should never be thrown silently
            #The Zen of Python
        if returnValue == None:
            raise RuntimError("Can't remove from an empty stack")
        self._top = self._top.next #remove the top index
        return returnValue
    def peek(self):
        """Return value at the top of the stack otherwise RuntimeError"""
        return self._top if self._top != None else RuntimeError("Can't remove from an empty stack")
        #returns it as an entry (from Node) unless it's None, which means a RuntimeError
    def is_empty(self):
        """Returns true if stack is empty, false otherwise"""
        return True if self._top == None else False

if __name__ == "__main__":
    #someone's running this as a lab
    sim = SimulatedComputer()
    commands = sim.fileText.split("\n")
    for command in commands:
        sim.command(command)
