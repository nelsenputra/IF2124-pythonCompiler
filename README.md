# Tubes TBFO by sipitBukanHalangan
> Python compiler written in Python. Based on the concept of Finite Automata and Context-Free Grammar with the use of Cocke–Younger–Kasami algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to our Github Repository!
This project was created by the team you can see on the following table.
| No. | Name | Student ID |
| :---: | :---: | :---: |
| 1. | Johannes Winson Sukiatmodjo | 13520123 |
| 2. | Ignasius Ferry Priguna | 13520126 | 
| 3. | Nelsen Putra | 13520130 |


## General Information
Python is a high-level, as well as general-purpose interpreting language. Python was created by Guido van Rossum and was first released in 1991. The Python programming design philosophy prioritizes code readability with the use of whitespace. Python is a multiparadigm language because it implements functional, imperative, object-oriented, and reflective paradigms.

In the process of making a program from a language into instructions that can be executed by a machine, there is a syntax check or a compilation of the language created by the programmer. This compilation aims to ensure that the instructions made by the programmer follow the rules that have been determined by the language. Both interpreter and compiler-type languages must perform syntax checks. The difference lies in what is done after the inspection process (compile) is completed.

It needs grammar and parser algorithm to compile. Many grammars and algorithms have been developed to produce high-performance compilers. The Python compiler built in this repository uses the concept of CFG which is used to evaluate program syntax and FA to manage the variable naming. In its implementation, we use the CYK algorithm which requires us to convert the CFG grammar into CNF grammar firsthand so that the grammar can be used as an input to the CYK algorithm.


## Technologies Used
The whole program was written in Python.


## Features
- [x] Receive an external file as an input that consists of source code written in Python
- [x] Evaluate the syntax of Python code with CFG
- [x] Evaluate the variable names with FA
- [x] Give an output as the program evaluation's product: "Accepted" if input is accepted or "Syntax Error" if it is rejected
- [ ] Tell the user about the location and the details of the error(s) if any


## Setup
### Dependencies

### Installation
- Download and install [Python](https://www.python.org/downloads/)
- Install the whole modules and [libraries](#library) used in the source code
- Download the whole folders and files in this repository or do clone the repository

### Execution
1. Clone this repository in your own local directory

    `git clone https://github.com/nelsenputra/IF2124-pythonCompiler.git`

2. Open the command line and change the directory to '???'

    `cd IF2124-pythonCompiler/???`
    
3. Run `python cyk.py` on the command line


## Project Status
Project is: _complete_

All the specifications, excluding bonus were implemented.


## Room for Improvement
- A more advanced feature: telling the user about the location and the details of the error(s) if any
- A faster or more efficient algorithm to make the program run quicker


## Acknowledgements
- This project was based on [Spek Tugas Pemrograman TBFO](https://docs.google.com/document/d/1Fd8wLOP_GzJ66atpw1yK1_S1dLCFQcKFTgnePFHql7Y/edit#)
- Thanks to God
- Thanks to Mr. Judhi Santoso, Mrs. Ayu Purwarianti, and Mrs. Harlili as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Big Project for IF2124 Formal Languages and Automata Theory


## Library
- [os](https://docs.python.org/3/library/os.html)


## Contact
Created by sipitBukanHalangan. 2021 All Rights Reserved.
