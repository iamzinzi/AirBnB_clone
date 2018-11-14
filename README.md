# 0x00. AirBnB clone - The console

## Description

This project is the first step towards building our first full web application: an AirBnB clone. In this project, we wrote a command interpreter to manage our AirBnB objects. 
* A parent class (called `BaseModel`) was put in place to take care of the initialization, serialization and deserialization of future instances.
* Created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Created all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
* Created the first abstracted storage engine of the project: File storage.
* Created all unittests to validate all our classes and storage engine

## Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the `cmd` module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Requirements for Python scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation
* All your classes should have a documentation
* All your functions (inside and outside a class) should have a documentation

## How to Use it
* To install the console, clone our repository by running the command `git clone https://github.com/TrieToSucceed/AirBnB_clone.git`
* To start the console, run the command `./console.py` in the main directory (`AirBnB_clone`) for interactive mode.
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb)
```
* Our console also works in non-interactive mode as such:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```
For help on syntax, type the command `help <command>` into the console.

## Examples
Starting with no objects, we will create a BaseModel instance, update it with the key-value pair `first_name: "Betty"`, and then prove our instance has changed.
```
(hbnb) all
(hbnb) create BaseModel
bca8ad60-bf0e-4d4f-9264-24944d8c6672
(hbnb) show BaseModel bca8ad60-bf0e-4d4f-9264-24944d8c6672
[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241)}
(hbnb) 
(hbnb) update BaseModel bca8ad60-bf0e-4d4f-9264-24944d8c6672 first_name "Betty"
(hbnb) show BaseModel bca8ad60-bf0e-4d4f-9264-24944d8c6672
[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'first_name': 'Betty'}
(hbnb) 
Now let's create a few more objects to demonstrate how all, count, and destroy work.
```
(hbnb) create BaseModel
d98de563-89c7-4dc3-9f46-e087911813f6
(hbnb) create BaseModel
9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02
(hbnb) create User
a83cba86-f7ce-470f-89f8-85af656bc6df
(hbnb) count BaseModel
3
(hbnb) count User
1
(hbnb) count City
0
(hbnb) all BaseModel
["[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'first_name': 'Betty'}", "[BaseModel] (9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 44, 205574), 'id': '9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 44, 205618)}", "[BaseModel] (d98de563-89c7-4dc3-9f46-e087911813f6) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668384), 'id': 'd98de563-89c7-4dc3-9f46-e087911813f6', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668408)}"]
(hbnb) all
["[BaseModel] (bca8ad60-bf0e-4d4f-9264-24944d8c6672) {'created_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43214), 'updated_at': datetime.datetime(2018, 11, 14, 18, 42, 54, 43241), 'id': 'bca8ad60-bf0e-4d4f-9264-24944d8c6672', 'first_name': 'Betty'}", "[BaseModel] (9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 44, 205574), 'id': '9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 44, 205618)}", "[BaseModel] (d98de563-89c7-4dc3-9f46-e087911813f6) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668384), 'id': 'd98de563-89c7-4dc3-9f46-e087911813f6', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 40, 668408)}", "[User] (a83cba86-f7ce-470f-89f8-85af656bc6df) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112270), 'id': 'a83cba86-f7ce-470f-89f8-85af656bc6df', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112295)}"]
(hbnb) destroy BaseModel 9a5eaa2c-3aa3-4df9-bfdb-1f8d4c7b1a02
(hbnb) count BaseModel
2
(hbnb) 
```
In addition, all of our commands work with Object method notation as such:
```
(hbnb) BaseModel.count()
2
(hbnb) User.all()
["[User] (cbde29bc-7dbb-45d5-b6b3-54afaf953cb3) {'created_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362051), 'updated_at': datetime.datetime(2018, 11, 14, 18, 54, 20, 362076), 'id': 'cbde29bc-7dbb-45d5-b6b3-54afaf953cb3', 'stars': 5.5}", "[User] (a83cba86-f7ce-470f-89f8-85af656bc6df) {'created_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112270), 'id': 'a83cba86-f7ce-470f-89f8-85af656bc6df', 'updated_at': datetime.datetime(2018, 11, 14, 18, 50, 49, 112295)}"]
```


## Files
---
File|Task
---|---
console.py | Program that contains the entry point of the command interpreter
models/amenity.py | A class called `Amenity` that inherits from `BaseModel`
models/base_model.py | A parent class called `BaseModel` that takes care of the initialization, serialization and deserialization of our future instances
models/city.py | A class called `City` that inherits from `BaseModel`
models/place.py | A class called `Place` that inherits from `BaseModel`
models/review.py | A class called `Review` that inherits from `BaseModel`
models/state.py | A class called `State` that inherits from `BaseModel`
models/user.py | A class called `User` that inherits from `BaseModel`
models/\_\_init\_\_.py | An init file that makes `models` a package and declares an instance of class `FileStorage` called `storage` that reloads/deserializes all serialized object instances from the filename held in private class attribute `__file_path`
models/engine/file_storage.py | A class called `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances
models/engine/\_\_init\_\_.py | Empty init file that makes `engine` a module

## Directories
---
Directory Name | Description
---|---
models/ | Contains all model files where classes are defined
models/engine/ | Contains file where class `FileStorage` is defined
tests/test_models/ | Contains unittests files to test classes in dir `models/`
tests/test_models/test_engine | Contains unittest files to test classes in dir `engine/`

### Our command interpreter is able to:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object


## Authors
[Jian Huang](http://github.com/trieToSucceed/) 
[Jinji Zhang](https://github.com/iamzinzi/)
