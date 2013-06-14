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
import sys
print("sys encoding:",sys.stdout.encoding)
#Load file for testing
#FILE_NAME = "assets/Test2TestData.txt"
FILE_NAME = "assets/Test2TestData_simple.txt"
#print(open(FILE_NAME).read())
open_read_file = open(FILE_NAME).read()
#Load user dictionary file
import jieba
jieba.load_userdict("assets/userdict.txt")
#Testing
#seg_list = jieba.cut("坑爹麻烦给力不行", cut_all=False)
#print "Default Mode:", "/ ".join(seg_list)
#import jieba.posseg as pseg
#words = pseg.cut(open_read_file)
#for w in words:
#    print w.word.encode("utf-8"), w.flag.encode("utf-8")
#    
import jieba.posseg as pseg
def cut_and_print(text):
    text_filter_url = filter_url(text)
    print "text_filter_url:\n"+text_filter_url
    words =pseg.cut(text_filter_url)
    raw_print_result = ", ".join(["%s[%s]" % (word.word, word.flag) for word in words]).encode("utf-8")
    print "raw_print_result:\n"+raw_print_result
#Sort of filters using Python regexp
import re
def filter_url(text):
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
#    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    return text
#network emoticonal symbol [xxx]
def filter_network_emoticonal_symbol(text):
    return text
#name list after the character "@"
def filter_name_list(text):
    return text
# interpunction ,:?!
def filter_interpunction(text):
    return text
#Entry call
cut_and_print(open_read_file)