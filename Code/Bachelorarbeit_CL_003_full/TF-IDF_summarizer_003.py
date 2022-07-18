from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
from nltk.probability import FreqDist
import math
from heapq import nlargest


def processSentence(sents):
    stemmer = SnowballStemmer(language='english')
    setRemove = set(stopwords.words('english') + list(punctuation))
    processedSent = []
    processedWord = []
    for sent in sents:
        st = ""
        words = word_tokenize(sent)
        for word in words:
            if word not in setRemove:
                stemWord = stemmer.stem(word)
                st += stemWord + " "
                processedWord.append(stemWord)
        processedSent.append(st)
    return processedSent, processedWord


def createTF(freqList):
    tfDic = {}
    l = len(freqList)
    for key, value in freqList.items():
        tfDic[key] = value / l
    return tfDic


def createIDF(processedSent, freqList):
    idfDic = {}
    l = len(processedSent)
    for key, value in freqList.items():
        occurence = 0
        for sent in processedSent:
            sent = word_tokenize(sent)
            if key in sent:
                occurence += 1
        if occurence == 0:
            idfDic[key] = 0
        else:
            idfDic[key] = math.log10(l / occurence)
    #         idfDic[key]=(l/occurence)
    return idfDic


def createTF_IDF(freqList, dicTF, dicIDF):
    tfidfDic = {}
    for key, value in freqList.items():
        tfidfDic[key] = (dicTF.get(key) * dicIDF.get(key))
    return tfidfDic


def scoring(dicTFIDF, pr):
    score = []
    scoreDic = {}
    idx = 0
    for sent in pr:
        sent = word_tokenize(sent)
        sc = 0
        for word in sent:
            sc += dicTFIDF.get(word)
        score.append(sc)
        scoreDic[idx] = sc
        idx += 1
    return scoreDic


def arrange(score, n):
    return nlargest(n, score, key=score.get)


def show(finList, sents):
    finList.sort()
    st = ""
    for i in finList:
        st = st + (sents[i] + "\n")
    return st


def textSummarize(text, n):
    sents = sent_tokenize(text)
    if (len(sents) > n):
        processedSent, processedWords = processSentence(sents)
        freqList = FreqDist(processedWords)
        dicTF = createTF(freqList)
        dicIDF = createIDF(processedSent, freqList)
        dicTFIDF = createTF_IDF(freqList, dicTF, dicIDF)
        score = scoring(dicTFIDF, processedSent)
        finList = arrange(score, n)
        finpara = show(finList, sents)
        return finpara, text
    else:
        return "Number of sentence is less than number of sentence required in summary.", text


if __name__ == "__main__":
    #text3 = "tf-idf stands for Term frequency-inverse document frequency. The tf-idf weight is a weight often used in information retrieval and text mining. Variations of the tf-idf weighting scheme are often used by search engines in scoring and ranking a document’s relevance given a query. This weight is a statistical measure used to evaluate how important a word is to a document in a collection or corpus. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus (data-set)."
    text3 = "tf-idf stands for Term frequency-inverse document frequency. The tf-idf weight is a weight often used in information retrieval and text mining."
    print(textSummarize(text3, 2))


