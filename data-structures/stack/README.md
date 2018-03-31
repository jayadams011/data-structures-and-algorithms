## Implement a Stack and a Queue
This is a solo assignment

Specification
Create a new branch in your data-structures-and-algorithms repository called stack-queue. If you call it anything else, you will get ZERO CREDIT with NO COMMENTS

Create two separate directories: stack and queue respectively, with all of your standard module configuration for each directory

__init__.py, README.md, etc.
Create two files in each called node.py and stack.py, queue.py respectively

In node.py:

Create a Class for a Node which is aware of the value as val and next as _next
Ensure that you have a __repr__ method defined to return the value of the node when printed
In stack.py:

Create a Class for a Stack which creates an empty Stack when instantiated
This class should be aware of a default None value assigned to top when the isntance is created
This class should be aware of the len of the stack, which represents the count of Nodes in the stack at any time
This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the stack for each value in the iterable
Define any further magic methods such as len and str to support user functionality and informative responses
Define a method called push which takes any value as an argument and adds that value to the top of the stack with an O(1) Time performance
Define a method called pop which takes no arguments and removes / returns the Node at the top of the stack
Define a method called peek which takes no arguments and returns the Node at the top of the stack
At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.