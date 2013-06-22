#encoding=utf-8
#Pause the command window
raw_input("Press any key to start.") 
#@see:https://github.com/fxsjy/jieba
#@see:http://ddtcms.com/blog/archive/2013/2/4/69/jieba-fenci-suanfa-lijie/
#@see:ICTCLAS http://hi.baidu.com/streamlinlin/item/1978d2ead3d08f3987d9de15
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
import os
def include(filename):
    if os.path.exists(filename): 
        execfile(filename)
include('prob_start.py')
#Load file for testing
FILE_NAME = "Test2TestData.txt"
#FILE_NAME = "assets/Test2TestData_simple.txt"
#print(open(FILE_NAME).read())
#open_read_file = open(FILE_NAME).read()
open_read_files = open(FILE_NAME).readlines()
#Load user dictionary file
import jieba
jieba.load_userdict("userdict.txt")
#ICTCLAS dictionary
ICTCLAS_DICT = {'':'','uj':'助略词','ul':'助词习语','Ag':'形语素','a':'形容词','ad':'副形词','ag':'形容词量词','an':'名形词','b':'区别词','c':'连词','Dg':'副语素','d':'副词','df':'副词方位词','e':'叹词','eng':'English','f':'方位词','g':'语素','h':'前接成分','i':'成语','j':'略语 ','k':'后接成分','l':'习用语','m':'数词','mq':'数量词','Ng':'名语素','n':'名词','ng':'名词语素','nr':'人名','ns':'地名','nt':'机构团体','nrt':'人名机构团体','nz':'其他专名','o':'拟声词 ','p':'介词 ','q':'量词 ','r':'代词 ','s':'处所词','Tg':'时语素','t':'时间词','tg':'时间量词','uz':'助状态词 ','u':'助词 ','ud':'助副词 ','ug':'助词语素 ','Vg':'动语素','v':'动词 ','vd':'副动词 ','vg':'动词语素 ','vn':'名动词','vq':'动量词','w':'标点符号','x':'非语素字','y':'语气词','z':'状态词','zg':'状态词语素'}
#Final results
final_results = []
#Testing
#print ICTCLAS_DICT['c']
#seg_list = jieba.cut("坑爹麻烦给力不行", cut_all=False)
#print "Default Mode:", "/ ".join(seg_list)
#import jieba.posseg as pseg
#words = pseg.cut(open_read_file)
#for w in words:
#    print w.word.encode("utf-8"), w.flag.encode("utf-8")
#    
import jieba.posseg as pseg
def cut_and_print(text):
#    print "text_before filtered:"+text
    text_filtered = filter_url(text)
    text_filtered = filter_network_emoticonal_symbol(text_filtered)
    text_filtered = filter_name_list(text_filtered)
#    text_filtered = filter_interpunction(text_filtered)
#    print "text_filtered:"+text_filtered
    words =pseg.cut(text_filtered)
    pseg_cut_result = ",".join(["%s[%s]" % (word.word, ICTCLAS_DICT[word.flag]) for word in words]).encode("utf-8")
    pseg_cut_result = pseg_cut_result.strip()
    pseg_cut_result = re.sub(r'\[x\]', '', pseg_cut_result)
#    print "pseg_cut_result:"+pseg_cut_result
#    print "final output:"
    nice_output(pseg_cut_result)
#Sort of filters using Python regexp
import re
def filter_url(text):
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
#    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    return text
#network emoticonal symbol [xxx]
def filter_network_emoticonal_symbol(text):
    text = re.sub(r'\[.*?\]', '', text)
    return text
#name list after the character "@"
def filter_name_list(text):
    text = re.sub(r'@.*?[ \n]', '', text)
    return text
# punctuation ,:?!
#@see: http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
import string
table = string.maketrans("", "")
exclude = set(string.punctuation)
#from unicodedata import category
def filter_interpunction(text):
    return re.sub(r'[,.!~！]+', '', text)
#    return ''.join(ch for ch in text if category(ch)[0] != 'P')
#    return re.sub('[%s]' % re.escape(string.punctuation), '', text)
#    return ''.join(ch for ch in text if ch not in exclude)
#    return text.translate(table,string.punctuation)
# Nice output
def nice_output(text):
    #String split []
    text = filter_interpunction(text)
#    print "raw result:"+text
    #Write to file
    output_file = open('Tokenization_output.txt','r+')
    output_file.write(text)
    output_file.close()
    #
    texts = text.split('[]')
    textsIndex = str(texts[0]).split('[')[0]
    texts.remove(texts[0])#remove the first item
#    print "textsIndex:"+textsIndex+" texts:"+str(texts)
    elements = []
    if len(texts)>=2:#Remove null value item
        for text in texts:
            elements  = text.split(']')
    #        print len(elements)
            for element in elements:
                element = re.sub(r'\[', '                         ', element)#replace string
                print textsIndex+"            "+element#nice out put
    #            final_results.append(element)
    #    print final_results        
            
#Entry call
print "原文id            词汇                               词性                    "
print "------------------------------------------"
for open_read_file in open_read_files:
    cut_and_print(open_read_file)
#Pause the command window
raw_input("Press any key to exit.") 