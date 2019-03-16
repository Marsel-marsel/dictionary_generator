
def parse_operator_codes_file(input_file='indexmain.ru_collected_trunked.txt'):
    return [fetch_digits(line) for line in open(input_file, "r").readlines() if is_oper_code_line(line)]


def is_oper_code_line(input_line):
    if input_line.split(' ')[0] == '+7' and input_line.find("/") == -1:
        return True
    else:
        return False


#u'+7 916 99x-xx-xx\t0000000..9999999\t1' to u'91699'
def fetch_digits(input_line):
    region = [char for char in input_line.split('\t')[0].split(' ')[-1] if char.isdigit()]
    return ''.join(input_line.split(' ')[1] + ''.join(region))

# 7 - country_code
# 915 - operator_code
# 6783452 - postfix
def main(dict_file):
    country_codes = [7, 8]
    for operator_code in parse_operator_codes_file():
        digits_left = 11 - operator_code.__len__() - 1 #minus one digit for country_code
        for postfix in range(0, 10**digits_left - 1):
            for country_code in country_codes:
                phone_number = str(country_code) + str(operator_code) + str(postfix).zfill(digits_left) + '\n'
                dict_file.write(phone_number)
                # print phone_number


if __name__ == '__main__':
    dictionary = open("phone_num_dict.txt", 'w')
    main(dictionary)
    dictionary.close()


