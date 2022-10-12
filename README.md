# Hbnb console

![airbnb_img](https://i.imgur.com/symULZt.png)

The AirBnB clone goal of the project is to deploy on your server a simple copy of the AirBnB website.
After 4 projects, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

![steps](https://i.imgur.com/9WkM9nn.png)

And the final data diagram looks like this:

![data_diagram](https://i.imgur.com/I7VURNR.jpg)

## First step and GOAl of this repository: Write a command interpreter to manage your AirBnB objects.

## What’s a command interpreter?

We want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Resources
Read or watch:

* cmd module
* packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet


## Learning Objectives

-   How to create a Python package
-   How to create a command interpreter in Python using the  `cmd`  module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage  `datetime`
-   What is an  `UUID`
-   What is  `*args`  and how to use it
-   What is  `**kwargs`  and how to use it
-   How to handle named arguments in a function

## Execution

The hbnb command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: ``` $ echo "python3 -m unittest discover tests" | bash ```

## Authors:
* Sara Cruz |   <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" /> [GitHub](https://github.com/spcruz5) | 
* Angeira Quiles | <img alt="GitHub" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" />[GitHub](https://github.com/AngeiraT) | 
