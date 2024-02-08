import random

def generate_ndigits(n):
    ret = ''
    for i in range(n):
        ret += str(random.randint(0, 9))
        if random.random() < 0.1:
            ret += ' '
    return ret

def save_all_lines(all_lines, save_path):
    with open(save_path, 'w') as f:
        for line in all_lines:
            f.write(line + '\n')

if __name__ == '__main__':
    digit_lines = []
    for i in range(100):
        digit_lines.append(generate_ndigits(random.randint(5000, 30000)))
    save_all_lines(digit_lines, './resources/corpus/alldigits.txt')