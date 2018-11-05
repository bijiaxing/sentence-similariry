import numpy as np
import argparse
import random
import jieba



#词向量字典模型建模
vectors = {}#词向量
def read_vectors(path, topn):  # read top n word vectors
    lines_num, dim = 0, 0
    with open(path, encoding='utf-8', errors='ignore') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                dim = int(line.rstrip().split()[1])#因为是第一行
                continue
            lines_num += 1
            tokens = line.rstrip().split(' ')
            vectors[tokens[0]] = np.asarray([float(x) for x in tokens[1:]])
            if topn != 0 and lines_num >= topn:
                break
    return vectors, dim

read_vectors('C:\\Users\\datab\\Downloads\\embedding', 635973)
#print('数据读取完成')

#将句子转化为向量
def sentence_vector(s):#该函数用于计算句子向量
        words = jieba.lcut(s)
        v = np.zeros(300)
        for word in words:
            if word in vectors.keys():#如果表中有则加入
                v += vectors[word]
            else:
                for tmp in word:#如果表中没有则分成单个字后加入
                    v+=vectors[tmp]
        v /= len(words)
        return v



#用于计算句子相似度，即输入两个句子计算其cos
def vector_similarity(s1, s2):
    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


queList=["如何新建仓库？","如何提升品牌关注度","资产负债表的用途","流量规则是什么","你好"]
ansList=["在地图要建立仓库的地方单击，在弹出窗口中选择新建仓库。",
"我建议你通过参考市场调研报告，在流量比较大的平台加大广告的投入",
"资产负债表表示企业在一定日期（通常为各会计期末）的财务状况（即资产、负债和业主权益的状况）的主要会计报表。资产负债表利用会计平衡原则，将合乎会计原则的资产、负债、股东权益”交易科目分为“资产”和“负债及股东权益”两大区块，在经过分录、转帐、分类帐、试算、调整等等会计程序后，以特定日期的静态企业情况为基准，浓缩成一张报表。其报表功用除了企业内部除错、经营方向、防止弊端外，也可让所有阅读者于最短时间了解企业经营状况。",
"整个市场的流量规则包含了整体流量市场的变化，网站流量的争夺，注册用户的争夺",
"你好，我是沙盘精灵，我能给你介绍电商沙盘的一些基本功能,如介绍一些常见的规则，介绍一些常见的角色，介绍一些常见的策略，和一些电商相关的评价。"]

def similarityCheck(s):
    #vectemp=sentence_vector(s)
    finalsimiar=0
    for index in range(len(queList)):
        tmpsimilar=vector_similarity(s,queList[index])
        if tmpsimilar>finalsimiar:
            finalsimiar=tmpsimilar
            flag=index
    answer=ansList[flag]
    print("问题同语料库相似度:")
    print(finalsimiar)
    print("相近答案是:")
    print(answer)

sen1=' '
while sen1 != 'stop':
    sen1=input('请输入问题:')
    similarityCheck(sen1)

    # sen2=input('请输入第二句话:')
    # print('相似度是:')
    # print(vector_similarity(sen1,sen2))
