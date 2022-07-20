import re
import jieba
import jieba.posseg as pseg
from tqdm import tqdm
from pypinyin import lazy_pinyin

def tagging(text):
    # text = pseg.cut(text)
    text = [char for char in text]
    ptext = []
    # for word, pos in text:
    #     pinyin = ''.join(lazy_pinyin(word))
    #     ptext.append('/'.join((word, pinyin, pos)))
    for char in text:
        pinyin = ''.join(lazy_pinyin(char))
        ptext.append('/'.join((char, pinyin, 'c')))
    line = ' '.join(ptext)
    return line

if __name__ == '__main__':
    # jieba.dt.tmp_dir = ('/public/home/rhj/.cache/jieba')
    # jieba.enable_parallel(8)
    with open('data/zhwiki-20220101.txt', 'r', encoding='utf-8') as fin, \
         open('data/zhwiki-split-miu-char.txt', 'w', encoding='utf-8') as fmiu:
         # open('data/zhwiki-split-1s1l.txt', 'w', encoding='utf-8') as fsl, \
        for line in tqdm(fin.readlines()):
            # 去掉各级标题和平行关系的星号
            line = re.sub('^【', '', line)
            line = re.sub('】$', '', line)
            line = re.sub('^====', '', line)
            line = re.sub('====$', '', line)
            line = re.sub('^===', '', line)
            line = re.sub('===$', '', line)
            line = re.sub('^==', '', line)
            line = re.sub('==$', '', line)
            line = re.sub('^\*', '', line)

            # line_sl = re.split('[。？！]', line)
            # for l in line_sl:
            #     l = l.strip()
            #     if l != '' and re.match('[\u4E00-\u9FFF]', l):
            #         l = tagging(l)
            #         l += '\n'
            #         fsl.write(l)

            line_miu = re.split('[^\u4E00-\u9FFF]', line)
            for l in line_miu:
                if l != '':
                    l = tagging(l)
                    l += '\n'
                    fmiu.write(l)
