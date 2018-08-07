# Author: Jiaci LIU


def xie_zheng(infile, outfile):
    infopen = open(infile, 'r', encoding='utf-8')
    outopen = open(outfile, 'w', encoding='utf-8')
    lines = infopen.readlines()
    list_1 = []

    for line in lines:
        if line not in list_1:
            list_1.append(line)
            outopen.write(line)

    infopen.close()
    outopen.close()


if __name__ == '__main__':
    xie_zheng('D://Users//32861//Desktop//CostModel-V1//quan.txt',
              'D://Users//32861//Desktop//CostModel-V1//xiezheng.txt')
