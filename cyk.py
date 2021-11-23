import os

# Read grammar
def read_cnf():
    """ 
    Membaca file cnf.txt di folder yang sama dan mengubah jadi list v_rules dan t_rules
    v_rules adalah list rule yang menghasilkan non-terminal symbol
    t_rules adalah list rule yang menghasilkan terminal symbol 
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
def read_input():
    """
    Membaca file input.py di folder yang sama dan mengubahnya menjadi sebuah string
    """

    filename = os.path.join(os.curdir, "./test/raise.py")
    with open(filename) as input_file:
        lines = input_file.readlines()
        input_string = ''

        for line in lines:
            input_string += line.strip('\t').strip(' ')
        
        input_string += '\n'
    return input_string


def make_pairs(set_a, set_b):
    pairs_list = []
    for a in set_a:
        for b in set_b:
            pairs_list.append([a,b])

    return pairs_list


# Cyk
def make_cyk_table(v_rules, t_rules, input_string):
    string_length = len(input_string)

    # Buat tabel
    table = [[set() for _ in range(string_length - i)] for i in range(string_length)]

    # Proses baris pertama tabel (terminal symbol)
    for i in range(string_length):
        for rules in t_rules:
            if input_string[i] == rules[1]:
                table[0][i].add(rules[0])
    
    # Proses sisa baris pada tabel (non-terminal symbol)
    for i in range(1, string_length):
        for j in range(0,string_length-i):
            for k in range(i):
                pairs = make_pairs(table[k][j], table[i-k-1][j+k+1])
                for rules in v_rules:
                    if rules[1] in pairs:
                        table[i][j].add(rules[0])

    for i in table:
        for j in i:
            print(j)
        print("\n")

    return table


if __name__ == '__main__':
    v_rules, t_rules = read_cnf()
    input_string = read_input()
    print([input_string])
    table = make_cyk_table(v_rules, t_rules, input_string)
    if len(input_string) > 0:
        if 'S0' in table[len(input_string)-1][0]:
            print("Accepted!")
        else:
            print("Syntax Error!")
    else:
        print("File kosong!")

