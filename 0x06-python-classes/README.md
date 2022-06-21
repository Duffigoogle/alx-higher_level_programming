# 0x06 Python - Classes and Objects
## Tasks
## Task 0 - My first square
	* Write an empty class Square that defines a square:
		- You are not allowed to import any module

## Task 1 - Square with size
	* Write a class Square that defines a square by: (based on 0-square.py) 		- Private instance attribute: size
		- Instantiation with size (no type/value verification)
		- You are not allowed to import any module

	- Why?
	* Why size is private attribute?
		- The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

## Task 2 - Size validation
	* Write a class Square that defines a square by: (based on 1-square.py)
		- Private instance attribute: size
		- Instantiation with optional size: def __init__(self, size=0):
			- size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
			- if size is less than 0, raise a ValueError exception with the message size must be >= 0
		- You are not allowed to import any module
