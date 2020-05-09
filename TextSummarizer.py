from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

from tika import parser

pdf = "C:\\Users\\jenni\\PycharmProjects\\TextSummarizer\\Article4-4.txt"
f = open(pdf, "r", encoding='utf8')
fileData = parser.from_file(pdf)
text = fileData['content']


# Meant to stem words
def _dictionary_table(text_string) -> dict:
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    stemWord = PorterStemmer()

    frequencyTable = dict()
    for i in words:
        i = stemWord.stem(i)
        if i in stopWords:
            continue
        if i in frequencyTable:
            frequencyTable[i] += 1
        else:
            frequencyTable[i] = 1
    return frequencyTable


def _sentence_scores(sentences, frequency_table) -> dict:
    sentenceWeight = dict()

    for ste in sentences:
        sentenceWordcount = (len(word_tokenize(ste)))
        sentence_without_stop_words = 0
        for wordWeight in frequency_table:
            if wordWeight in ste.lower():
                sentence_without_stop_words = +1
                if ste[:10] in sentenceWeight:
                    sentenceWeight[ste[:10]] += frequency_table[wordWeight]
                else:
                    sentenceWeight[ste[:10]] = frequency_table[wordWeight]
        sentenceWeight[ste[:10]] = sentenceWeight[ste[:10]]

    return sentenceWeight


def _average_score(sentence_weight) -> int:
    sumValues = 0
    for entry in sentence_weight:
        sumValues += sentence_weight[entry]

    averageScore = (sumValues / len(sentence_weight))

    return averageScore


def _article_summary(sentences, sentence_weight, limit):
    sentenceCounter = 0;
    articleSummary = ''

    for ste in sentences:
        if ste[:10] in sentence_weight and sentence_weight[ste[:10]] >= (limit):
            articleSummary += "" + ste
            sentenceCounter += 1
    return articleSummary


def _run_article_summary(nyarticle):
    frequencyTable = _dictionary_table(nyarticle)
    sentences = sent_tokenize(nyarticle)
    sentences_scores = _sentence_scores(sentences, frequencyTable)
    limit = _average_score(sentences_scores)
    articleSummary = _article_summary(sentences, sentences_scores, 1.3 * limit)

    return articleSummary


if __name__ == '__main__':
    f2 = open("C:\\Users\\jenni\\PycharmProjects\\TextSummarizer\\Article1Summary4-1.txt", "w+", encoding='utf8')
    summary_results = _run_article_summary(text)
#  print(summary_results)
#    text2 = fileData[summary_results]  # Get files text content
    f2.write(summary_results)
    f2.close()

# First need to clean the document
# then an algorithm that will calculate each weight of the word in a sentence
# the lowest weighted words are to be chosen to make a sentence
