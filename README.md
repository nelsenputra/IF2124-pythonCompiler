# Tubes TBFO by sipitBukanHalangan
> Python compiler written in Python. Based on the concept of Finite Automata and Context-Free Grammar with the use of Cocke–Younger–Kasami algorithm.


## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshot](#screenshot)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Python adalah bahasa interpreter tingkat tinggi (high-level), dan juga general-purpose. Python diciptakan oleh Guido van Rossum dan dirilis pertama kali pada tahun 1991. Filosofi desain pemrograman Python mengutamakan code readability dengan penggunaan whitespace-nya. Python adalah bahasa multiparadigma karena mengimplementasi paradigma fungsional, imperatif, berorientasi objek, dan reflektif.

Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks atau kompilasi bahasa yang dibuat oleh programmer. Kompilasi ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.

Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan kompilasi. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Compiler bahasa Python yang dibuat pada repository ini menggunakan konsep CFG yang digunakan untuk mengevaluasi syntax program serta FA untuk mengatur penamaan variabel. Dalam implementasinya, kami menggunakan algoritma CYK yang mengharuskan kami untuk melakukan konversi grammar CFG ke dalam grammar CNF terlebih dahulu agar grammar dapat dipakai sebagai masukan pada algoritma CYK.


## Technologies Used
The whole program was written in Python.


## Features
- [x] Receive an external file as an input that consists of source code written in Python
- [x] Evaluate the syntax of Python code with CFG
- [x] Evaluate the variable names with FA
- [x] Give an output as the program evaluation's product: "Accepted" if input is accepted or "Syntax Error" if it is rejected
- [ ] Tell the user about the location and the details of the error(s) if any


## Screenshot
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


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
    
3. Run `python ???.py` on the command line

## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _complete_

All the specifications, including bonus were implemented.

## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


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
