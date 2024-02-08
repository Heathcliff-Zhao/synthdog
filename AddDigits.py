
import random


def generate_ndigits(n):
    r = random.randint(10**(n-1), 10**n-1)
    return ' ' + str(r) + ' '



origin_wiki_corpus = './resources/corpus/enwiki.txt'

def read_corpus(corpus_file):
    all_lines = []
    with open(corpus_file, 'r') as f:
        for line in f.readlines():
            all_lines.append(line.strip())
    return all_lines

def write_corpus(corpus_file, all_lines):
    with open(corpus_file, 'w') as f:
        for line in all_lines:
            f.write(line + '\n')

# print(read_corpus(origin_wiki_corpus)[0])
def random_add_digits_to_line(line, ratio=0.1):
    length = len(line)
    # sorted_index = random.sample(range(length), length // 50)
    sorted_index = list(range(0, length, 500))
    sorted_index.sort()
    # print(sorted_index)
    real_insert_index = []
    real_insert_digits = []
    diff_list = []
    for i in range(len(sorted_index)):
        if i == 0:
            diff_list.append(sorted_index[i])
        else:
            diff_list.append(sorted_index[i] - sorted_index[i-1])
    # print(diff_list)
    for i in range(len(diff_list)):
        # if diff_list[i] > 150:
        try:
            inter = []
            while len(''.join(inter)) < diff_list[i] * ratio:
                inter.append(generate_ndigits(random.randint(1, 10)))
            # print(sorted_index[i-1], sorted_index[i], (sorted_index[i] - sorted_index[i-1]) // (len(inter) + 1))
            real_insert_index.extend(list(range(sorted_index[i-1], sorted_index[i], (sorted_index[i] - sorted_index[i-1]) // (len(inter) + 1)))[1:])
            real_insert_digits.extend(inter)
        except:
            pass
        # else:
        #     real_insert_digits.append(generate_ndigits(random.randint(1, 10)))
        #     real_insert_index.append(sorted_index[i])
    
    seged_origin_by_index = []
    for idx in range(len(real_insert_index)):
        if real_insert_index[idx] >= len(line):
            real_insert_index[idx] = len(line) - 50
    # print(real_insert_index)
    seged_origin_by_index.append(line[:real_insert_index[0]])
    for i in range(len(real_insert_index)):
        if i == 0:
            continue
        else:
            seged_origin_by_index.append(line[real_insert_index[i-1]:real_insert_index[i]])
    seged_origin_by_index.append(line[real_insert_index[-1]:])
    # assert len(seged_origin_by_index) == len(real_insert_digits) + 1, (len(seged_origin_by_index), len(real_insert_digits))
    # do insert
    ret_str_list = []
    for i in range(len(seged_origin_by_index)):
        ret_str_list.append(seged_origin_by_index[i])
        if i < len(real_insert_digits):
            ret_str_list.append(real_insert_digits[i])

    return ''.join(ret_str_list)

if __name__ == '__main__':
    # while True:
    #     idx = int(input('input idx: '))
    #     cps = read_corpus(origin_wiki_corpus)
    #     ori_len = len(cps[idx])
    #     added = random_add_digits_to_line(cps[idx])
    #     added_len = len(added)
    #     print(added)
    #     print((added_len - ori_len) / ori_len)
    from tqdm import tqdm
    cps = read_corpus(origin_wiki_corpus)
    for i in tqdm(range(len(cps))):
        cps[i] = random_add_digits_to_line(cps[i])
    write_corpus('./resources/corpus/enwiki_add_digits.txt', cps)

