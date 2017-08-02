# coding=utf-8
import os


datafile = 'data.txt'
problem_with = 'problem_with.txt'
problem_without = 'problem_without.txt'
suggestion = 'suggestion.txt'
meaningless = 'meaning_less.txt'


def sort():
    data_fptr = open(datafile, 'r', encoding='utf-8')
    meaningless_fptr = open(meaningless, 'a', encoding='utf-8')
    suggestion_fptr = open(suggestion, 'a', encoding='utf-8')
    problem_with_fptr = open(problem_with, 'a', encoding='utf-8')
    problem_without_fptr = open(problem_without, 'a', encoding='utf-8')
    total_lines = data_fptr.readlines()
    lines_num = len(total_lines)
    startline = int(input('起始评论行号[1~%d] : ' % lines_num))
    for x in range(startline - 1, lines_num):
        print('------(%d,%d)------\n%s\nOperation:0(退出),1(无意义),2(建议),3(详细问题),4(问题),其他(忽略):' % (x + 1, lines_num, total_lines[x]))
        optcode = input()
        if optcode == '0':
            insist = input('确实要退出（y/n）？请记住当前的行号"%d"！' % (x + 1))
            if str.lower(insist) == 'y':
                break
        elif optcode == '1':
            meaningless_fptr.write(total_lines[x])
        elif optcode == '2':
            suggestion_fptr.write(total_lines[x])
        elif optcode == '3':
            problem_with_fptr.write(total_lines[x])
        elif optcode == '4':
            problem_without_fptr.write(total_lines[x])
        else:
            pass
        os.system('cls')
    data_fptr.close()
    meaningless_fptr.close()
    suggestion_fptr.close()
    problem_with_fptr.close()
    problem_without_fptr.close()


if __name__ == '__main__':
    sort()
