import os

# Read grammar
def read_cnf():
    """ 
    Membaca file cnf.txt di folder yang sama dan mengubah jadi list v_rules dan t_rules.
    v_rules adalah list rule yang menghasilkan non-terminal symbol.
    t_rules adalah list rule yang menghasilkan terminal symbol.
    """

    filename = os.path.join(os.curdir, "./cnf.txt")
    with open(filename) as grammar:
        # Baca file CNF
        rules = grammar.read().splitlines()
        v_rules = []
        t_rules = []
        
        # Proses tiap baris file CNF
        for rule in rules:
            # Pisahkan bagian kanan panah dan bagian kiri panah
            rule = rule.split(" -> ")
            current_var = rule[0]

            # Pisahkan tiap product dari bagian kiri
            products = rule[1].split(" | ")

            # Proses tiap product
            for product in products:
                product = product.split()

                # Terminal symbol
                if product[0][0] == "'":
                    if product[0] == "'space'":
                        product[0] = "' '"
                    elif product[0] == "'newline'":
                        product[0] = "'\n'"

                    terminal = product[0][1]
                    t_rules.append([current_var, terminal])

                # Non terminal symbol
                else:
                    v_rules.append([current_var, product])

    return v_rules, t_rules


# Read input
def read_input(filename):
    """
    Membaca file input.py di folder yang sama dan mengubahnya menjadi sebuah string.
    """

    filename = os.path.join(os.curdir, ("./test/" + filename))
    with open(filename) as input_file:
        lines = input_file.readlines()
        input_string = ''

        for line in lines:
            input_string += line.strip('\t').strip(' ')
        
        input_string += '\n'
    return input_string


# FA
def is_possible_variable(input_string):
    """
    Finite Automata untuk menentukan apakah suatu frase merupakan variabel yang valid namanya.
    """
    keywords = ['False', 'class', 'is', 'return', 'None', 'continue', 'for', 'True', 'def', 'from', 'while', 'and', 'not', 'with', 'as', 'elif', 'if', 'or', 'else', 'import', 'pass', 'break', 'in', 'raise']
    Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if input_string in keywords:
        # String merupakan salah satu reserved keywords
        return False
    else:
        # State (S: Start state, A: Accepting state, D: Dead state)
        currentState = 'S'

        for i in input_string:
            if currentState == 'S':
                if i in Alphabets or i == '_':
                    currentState = 'A'
                else:
                    currentState = 'D'
            elif currentState == 'A':
                if not(i in Alphabets or i in Numbers or i == '_'):
                    currentState = 'D'
                # Jika termasuk alphabet, angka, atau '_' tidak berubah state
            else:
                break

        if currentState == 'A' :   
            return True
        else:
            return False


def checkForIdentifierNames(v_rules, input_string, table):
    """
    Mengecek setiap kombinasi input_string untuk mencari frase yang bisa menjadi suatu identifier / variabel.
    Jika ya, cell CYK untuk frase tersebut akan diisi.
    """
    IdentifierRules = set()
    for rules in v_rules:
        if rules[1] == ['IdentifierName']:
            IdentifierRules.add(rules[0])
    IdentifierRules.add('IdentifierName')

    for i in range(len(input_string)-1,-1,-1):
        for j in range(len(input_string)-i):
            if len(table[i][j]) != 1:
                if is_possible_variable(input_string[j:j+i+1]):
                    table[i][j] = IdentifierRules
                    if i != 0:
                        for k in range(i):
                            for l in range(j, j+i-k+1):
                                table[k][l] = {'d'}
                        
    for i in range(len(input_string)):
        for j in range(len(input_string)-i):
            if len(table[i][j]) == 1:
                table[i][j] = set()

    return table

# CYK
def make_pairs(set_a, set_b):
    """
    Menerima 2 buah set dan mengembalikan array yang berisi setiap pasangan yang dapat dibentuk
    oleh kedua set tersebut.
    """
    pairs_list = []
    for a in set_a:
        for b in set_b:
            pairs_list.append([a,b])

    return pairs_list


def process_cyk_table(v_rules, t_rules, input_string, table):
    """
    Menerapkan algoritma CYK pada tabel
    """
    string_length = len(input_string)

    # Proses baris pertama tabel (terminal symbol)
    for i in range(string_length):
        for rules in t_rules:
            if input_string[i] == rules[1]:
                table[0][i].add(rules[0])
        print(table[0][i])
    
    print("\n\n")
    # Proses sisa baris pada tabel (non-terminal symbol)
    for i in range(1, string_length):
        for j in range(string_length-i):
            for k in range(i):
                pairs = make_pairs(table[k][j], table[i-k-1][j+k+1])
                for rules in v_rules:
                    if rules[1] in pairs:
                        table[i][j].add(rules[0])
            print(table[i][j])
        print("\n\n")
    return table


if __name__ == '__main__':
    # Pembacaan CNF
    v_rules, t_rules = read_cnf()

    # Input nama file masukan
    filename = input("Masukkan nama file: ")

    # Pembacaan file masukan
    input_string = read_input(filename)
    
    # Buat tabel
    table = [[set() for _ in range(len(input_string) - i)] for i in range(len(input_string))]

    # Cek Identifier / Variabel
    table = checkForIdentifierNames(v_rules, input_string, table)

    # Lakukan Algoritma CYK
    table = process_cyk_table(v_rules, t_rules, input_string, table)

    # Output hasil pengecekan syntax
    if 'S0' in table[len(input_string)-1][0]:
        print("Accepted!")
    else:
        print("Syntax Error!")
