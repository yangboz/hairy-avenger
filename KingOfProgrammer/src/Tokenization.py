#@see:https://github.com/fxsjy/jieba
#encoding=utf-8
#1.       输入文本文件格式见附件，评委会使用相同格式、不同数据进行评判。
#2.       输出文本文件格式以范例为准。
#3.       词性不作为比赛评分标准，但属于加分项。
#4.       所使用的语言，工具不限，允许使用第三方开源组件。
#5.       能够准确分辨最新的网络流行语，例如坑爹，给力等。
#6.       能够去除文本中的噪音，例如url链接,@符号之后的人名清单，网络表情例如[嘻嘻]、[哈哈]，标点符号等。
#7.       提交清单包括源代码以及编译好的可执行程序文件（如果需要编译），词库文件，分词结果文件以及说明文件（内容包括所使用的工具名称，工具版本，如何运行所提交的代码或程序）。
#encoding=utf-8
import jieba

#Load file for testing
print(open("assets/Test2TestData.txt").read())

seg_list = jieba.cut("I come from China!", cut_all=False)
print("Default mode:",",".join(seg_list))

import jieba.posseg as pseg
words = pseg.cut(u"我爱北京天安门")
for w in words:
    print(w.word, w.flag)