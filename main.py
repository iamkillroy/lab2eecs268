#!/usr/bin/env python3
#By Lucas Frias KU EECS 268
# Lab 2 - Dated Feb 2nd 2026
#       <@
#       (KU//
#        "
# Rock Chalk!
import sys
#you might wonder why there's so many comments and the reason is because i'm getting really really bored
#waiting for this lab to start so i'm going to overexplain everything in the hopes that
#this terrible code is educational? maybe? dude idk 

class Function:
    """Class to model functions and their output"""
    #this class pretty much exclusively exists to model data
    #i call them data classes. they're useful because in an instance
    #they will model instructions and they're easier to manage
    #then like a dictionary which would be comparable
    def __init__(self, name, canHandleExceptions):
        self.name = name #set the name and boolean into the class
        self.canHandleExceptions = canHandleExceptions
	#i wanna check to make sure that these really are booleans or strings
        if type(self.name) != type("birds") or type(self.canHandleExceptions) != type(True):
            #I like birds, and this error handles incorrect inputs
            raise TypeError("Incorrect initialisation variables!")
#Let's define some Gibbons data type constructs
class Process:
    """Simulate computer program with process"""
    def __init__(self, name):
        self.name = name #sets name for parent process
        self.callStack = LinkedStack() #sets callstack as linkedstckmethod
	#so the idea behind this lab is to kinda abstract and show how program flow works ig
	#but the thing about program flow is that it's lowkey not like this at all
	#anyways we're pushing to the stack, but the process spawns these "tasks" that come 
	#recursively so like
	# Process main:
	# 	pow()
	#		a * a
	# 		return
	#	sin()
	# 		2pi something
	#		return
	#so basically we're simulating where the program counter would be "executing" based off of the object
	#now real live computers would have a reference object but really be pointing to binary instructions
	#or to code runtime and jump back (like even Python would abstract and tokenize python while running)
	#but i think the big thing it to represent recursion in programming which is a good lesson
class SimulatedComputer:
    """To kind of simulate the main running of this comptuer"""
    def __init__(self):
        self.fileText = open(input("File >"), "r").read()
        self.process = None #there's only one process
	#okay we're just turning fileText to be a string by opening the input given (also a string, prob in the CWD)
	#and then reading all of the values as utf-8 string text dat
	#also process doesn't exist yet
    def command(self, command):
        """Processes command from file format given"""
	#so strings are also arrays and you can just access them
	#arrays lists same thing in python
	#"ABCDEF" [:3] is ABCD because remember we start at 0!!!
	#duh but just remember this because concatination is a large part
	#of programming
        if command[:5] == "START":
            #The process is created
            #there's this weird scary thing in the instructions that 
	    #makes it sound like there can only be one process so i'm gonna
	    #error check here
            if self.process != None:
                 return Exception("Not a multiprocess system")
            print(command[5:] + " Process started")
	    #HEY kids take a look we're using the other side of the string again
            self.process = Process(name=command[5:]) #make a process with that name
            #add main as the first function
            self.process.callStack.push(Function("main", False)) #you never specify
            #if this function has an error handler so i'm assuming nah
        if command[:4] == "CALL":
            funcName = command.split(" ")[1] #string split and 1st term is the function name
            funcCHE = True if "yes" in command.split(" ")[2] else False #i like these statement but maybe it makes code less
	    #readable. i think that it depends on the type of person you are and like how you approach these things
	    # i think it's more concise because otherwise i would use five lines to do something i could in one 
	    #and this is concise but not as readable. it's a simple statement though and python uses clear wording
	    #like it's True if yes is in command.split(" ")[2] and that part might be more confusing but we're just checking the 
	    #second parameter in the function CALL and we're just evaluating if that's the string yes because that matters for me
	    #to make sre the function can get called so okay cool fine rad nice fire gas
            #CHE = can handle exceptions
            #function's bool (tertiary) which examines using in to avoid
            #string concat errors, resolves as boolean
            #then init a new function that pushes itself to the 
            #process call stack in the SIM
            self.process.callStack.push(Function(funcName, funcCHE))
            #terminal output
            print(self.process.name + " calls " + funcName + " function")
        if command [:6] == "RETURN":
            #removes a function from the callstack without error
	    #i think this is the equivalent of just like a return 0 or just a normal
            #a normal operation return status
            poppedFunc = self.process.callStack.pop() #just pop the functon
            print(self.process.name + " has " + poppedFunc.entry.name + " return")
            #if we're at the end STOP LETS STOP 
            if self.process.callStack.is_empty(): #handles exitting
                              print(self.process.name + " Process ended.")
                              sys.exit(0) #STOPS THE PROGRAM (woah)
        if command[:5] == "RAISE":
            #as lane lamping says "oh boy"
            #this function is complicated
            self.process.hasException = True
            #now we go through all processes until we find
            #if and where there's an exception handler
	    #so basically there's two types of return types but we just say that there's an error type
	    #and if a function is built to handle errors then it does!
            while not self.process.callStack.is_empty(): #make sure we don't read nothing
                if self.process.callStack.peek().entry.canHandleExceptions: #() returns the func
                    #and then we can access the values inside of the init class
                    print(self.process.name + " has "+ self.process.callStack.peek().entry.name + " handle the exception and keep running")
                    break
                else: #the function can't handle exceptions, pop off of stack and announce it
                    self.process.callStack.pop() #remove it
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
		#Tim Peters my pookie <3
		#please tell me if i write good python
        if returnValue == None: #to make tim peters happy
            raise RuntimError("Can't remove from an empty stack")
        self._top = self._top.next #remove the top index
        return returnValue
    def peek(self):
        """Return value at the top of the stack otherwise RuntimeError"""
        return self._top if self._top != None else RuntimeError("Can't remove from an empty stack")
        #returns it as an entry (from Node) unless it's None, which means a RuntimeError
    def is_empty(self):
        """Returns true if stack is empty, false otherwise"""
        return True if self._top == None else False #if the top is None, then it's empty. Else, it's not empty
	#the reason we know this is that popping, as long as there's a node, makes sure that the next node
	#is the node's .next, and the topmost node will always have a None type

if __name__ == "__main__":
    #someone's running this as a lab
    sim = SimulatedComputer()
    #we mighta shoulda done this in sim but whateverr
    commands = sim.fileText.split("\n")
    #for every command let's run it!!!
    for command in commands:
        sim.command(command)
    sys.exit(0) #redundant cool code
