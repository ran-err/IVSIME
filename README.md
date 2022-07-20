# IVSIME
递增词汇选择神经网络中文输入法

数据集：https://pan.baidu.com/s/1pf3iaoTwJX636Ufkggk_GA?pwd=sd5u

调用wiki_parser.py wiki_split.py生成MIU格式语料

data.py分割训练集、测试集、验证集，生成输入法词汇表

train.py训练模型

weight.py导出训练好的模型数据

eval.py计算评价指标

n-gram模型使用SRLILM进行训练
