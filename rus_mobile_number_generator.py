

def parse_operator_codes_file(input_file='indexmain.ru_collected.txt'):
    digits = [fetch_digits(line) for line in open(input_file, "r").readlines() if is_oper_code_line(line)]
    print digits


def is_oper_code_line(input_line):
    if input_line.split(' ')[0] == '+7' and input_line.find("/") == -1:
        return True
    else:
        return False


#u'+7 916 99x-xx-xx\t0000000..9999999\t1' to u'91699'
def fetch_digits(input_line):
    print input_line
    region = [char for char in input_line.split('\t')[0].split(' ')[-1] if char.isdigit()]
    return ''.join(input_line.split(' ')[1] + ''.join(region))


def main():
    parse_operator_codes_file()


if __name__ == '__main__':
    main()


