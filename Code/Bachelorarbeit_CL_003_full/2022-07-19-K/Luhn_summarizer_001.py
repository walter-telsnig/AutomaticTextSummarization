# from bs4 import BeautifulSoup
# import requests
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import re

word_limit = 300

raw_text = "George Washington (1732-99) was commander in chief of the Continental Army during the American " \
            "Revolutionary War (1775-83) and served two terms as the first U.S. president, from 1789 to 1797. The son " \
            "of a prosperous planter, Washington was raised in colonial Virginia. As a young man, he worked as a " \
            "surveyor then fought in the French and Indian War (1754-63). During the American Revolution, he led the " \
            "colonial forces to victory over the British and became a national hero. In 1787, he was elected " \
            "president of the convention that wrote the U.S. Constitution. Two years later, Washington became " \
            "America’s first president. Realizing that the way he handled the job would impact how future presidents " \
            "approached the position, he handed down a legacy of strength, integrity and national purpose. Less than " \
            "three years after leaving office, he died at his Virginia plantation, Mount Vernon, at age 67. George " \
            "Washington was born on February 22, 1732, at his family’s plantation on Pope’s Creek in Westmoreland " \
            "County, in the British colony of Virginia, to Augustine Washington (1694-1743) and his second wife, " \
            "Mary Ball Washington (1708-89). George, the eldest of Augustine and Mary Washington’s six children, " \
            "spent much of his childhood at Ferry Farm, a plantation near Fredericksburg, Virginia. After " \
            "Washington’s father died when he was 11, it’s likely he helped him mother manage the plantation.Few " \
            "details about Washington’s early education are known, although children of prosperous families like his " \
            "typically were taught at home by private tutors or attended private schools. It’s believed he finished " \
            "his formal schooling at around age 15. As a teenager, Washington, who had shown an aptitude for " \
            "mathematics, became a successful surveyor. His surveying expeditions into the Virginia wilderness earned " \
            "him enough money to begin acquiring land of his own. "

def hello_luhn():
    return_test = "Hello, I'm from class Luhn"
    print(return_test)
    return return_test

def word_tokenizer(sent):
    words = word_tokenize(sent)
    #print(words)
    return words

def clean(article):
    lem = WordNetLemmatizer()
    article = re.sub(r'\[[^\]]*\]', '', article)
    article = sent_tokenize(article)
    cleaned_list = []
    for sent in article:
        sent = sent.lower()
        word_list = []
        words = word_tokenize(sent)
        for word in words:
            word_list.append(lem.lemmatize(word.lower()))
        cleaned_list.append(' '.join(word_list))
    return cleaned_list

def get_frequency_dictionary(content):
    frequency = {}
    for sentence in content:
        word_list = word_tokenize(sentence)
        for word in word_list:
            if word not in set(stopwords.words('english')).union({',', '.', ';', '%', ')', '(', '``'}):
                if frequency.get(word) is None:
                    frequency[word] = 1
                else:
                    frequency[word] += 1
    return frequency

def get_score(content, frequency_dictionary):
    sentence_score = {}
    for sentence in content:
        score = 0
        word_list = word_tokenize(sentence)
        start_idx, end_idx = -1, len(word_list) + 1
        index_list = []
        for word in word_list:
            if word not in set(stopwords.words('english')).union(
                    {',', '.', ';', '%', ')', '(', '``'}) and word in frequency_dictionary.keys():
                index_list.append(word_list.index(word))
        if index_list:
            score = len(index_list) ** 2 / (max(index_list) - min(index_list))
        sentence_score[content.index(sentence)] = score
    return sentence_score


def get_summary(sentence_scores, content, threshold):
    summary = ""
    sentence_indexes = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:threshold - 1]
    for index in sentence_indexes:
        summary += content[index] + " "
    return summary


def main(raw_text, max_words):
    # entry point from main.py, raw_text is the content of source/input QTextEdit
    content = raw_text
    max_words = max_words
    raw_text_words = str(word_tokenize(content))
    raw_text_sentences = str(sent_tokenize(content))
    cleaned_content = clean(content)
    threshold = len(cleaned_content) // 10 # Todo: static parameter change to parameter in function call
    frequency_dictionary = get_frequency_dictionary(cleaned_content)
    sorted_dictionary = {key: frequency_dictionary[key] for key in
                         sorted(frequency_dictionary, key=frequency_dictionary.get, reverse=True)[:word_limit]}
    sentence_scores = get_score(cleaned_content, sorted_dictionary)
    summary = get_summary(sentence_scores, sent_tokenize(content), threshold)
    # print("max words were: " +max_words)
    return summary, raw_text_words, raw_text_sentences, sentence_scores



if __name__ == "__main__":
    main()