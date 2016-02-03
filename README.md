# poavp
Public opinion analysis visualization platform

## Part 1
nativesentiment(朴素情感分析) 是一个朴素的情感分析工具，它依据字典，结合程度词、感叹词等，通过一个权值模型来决定句子中正面和负面情绪的得分，从而得出情感倾向

## Part 2
fiisio (https://github.com/wgliang/fiisio) 根据snownlp而修改的，只针对情感分析，用到BM25、朴素贝叶斯原理,可以完成分词、词性标注、情感分析等功能

## Part 3
panvisual(泛可视化) (https://github.com/wgliang/panvisual) 基于d3实现的一个数据可视化工具，主要用于舆情分析平台的可视化功能，基于爬虫抓取到的数据、情感分析的结果及中间结果、舆情和情感的不同维度数据模型构建图表