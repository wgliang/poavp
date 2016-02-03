# poavp
Public opinion analysis visualization platform

## Part 1
nativesentiment(朴素情感分析) 这是一个正在写的朴素的情感分析工具，说它朴素是因为在此只是从词的角度来分析情感，不使用任何已有的分类器和算法,它依据字典，结合程度词、感叹词等，通过建立的一个权值模型来决定句子中正面和负面情绪的得分，从而得出情感倾向.当然，它的准确性和健壮性与模型紧密相关，我会不断的优化.在此我认为任何分类算法和流行的机器学习只是来提高分析的准确性，一个好的字典才是关键

## Part 2
fiisio (https://github.com/wgliang/fiisio) 是我根据一个不错的中文分析工具snownlp而修改的，只针对情感分析，用到BM25、朴素贝叶斯原理,可以完成分词、词性标注、情感分析等功能

## Part 3
panvisual(泛可视化) (https://github.com/wgliang/panvisual) 基于d3实现的一个数据可视化工具，主要用于舆情分析平台的可视化功能，基于爬虫抓取到的数据、情感分析的结果及中间结果、舆情和情感的不同维度数据模型构建图表