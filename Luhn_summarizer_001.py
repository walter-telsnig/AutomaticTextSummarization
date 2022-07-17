# from bs4 import BeautifulSoup
# import requests
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import re

word_limit = 300

raw_text = "In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched to empower the next generation " \
           "of students with AI-ready skills. Envisioned as a three-year collaborative program, Intelligent Cloud Hub will support around 100 institutions " \
           "with AI infrastructure, course content and curriculum, developer support, development tools and give students access to cloud and AI services. " \
           "As part of the program, the Redmond giant which wants to expand its reach and is planning to build a strong developer ecosystem in India with the " \
           "program will set up the core AI infrastructure and IoT Hub for the selected campuses. The company will provide AI development tools and Azure AI " \
           "services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning.According to Manish Prakash, Country General Manager-PS, " \
           "Health and Education, Microsoft India, said, 'With AI being the defining technology of our time, it is transforming lives and industry and the " \
           "jobs of tomorrow will require a different skillset. This will require more collaborations and training and working with AI. That’s why it has " \
           "become more critical than ever for educational institutions to integrate new cloud and AI technologies. The program is an attempt to ramp up " \
           "the institutional set-up and build capabilities among the educators to educate the workforce of tomorrow.' The program aims to build up the " \
           "cognitive skills and in-depth understanding of developing intelligent cloud connected solutions for applications across industry. Earlier in " \
           "April this year, the company announced Microsoft Professional Program In AI as a learning track open to the public. The program was developed " \
           "to provide job ready skills to programmers who wanted to hone their skills in AI and data science with a series of online courses which featured " \
           "hands-on labs and expert instructors as well. This program also included developer-focused AI school that provided a bunch of assets to help build " \
           "AI skills."

output = "The company will provide AI development tools and Azure AI services such as Microsoft Cognitive Services, Bot Services and Azure Machine Learning." \
         "According to Manish Prakash, Country General Manager-PS, Health and Education, Microsoft India, said, 'With AI being the defining technology of our " \
         "time, it is transforming lives and industry and the jobs of tomorrow will require a different skillset. Envisioned as a three-year collaborative program, " \
         "Intelligent Cloud Hub will support around 100 institutions with AI infrastructure, course content and curriculum, developer support, development tools and " \
         "give students access to cloud and AI services. The program was developed to provide job ready skills to programmers who wanted to hone their skills in AI " \
         "and data science with a series of online courses which featured hands-on labs and expert instructors as well. As part of the program, the Redmond giant " \
         "which wants to expand its reach and is planning to build a strong developer ecosystem in India with the program will set up the core AI infrastructure " \
         "and IoT Hub for the selected campuses. In an attempt to build an AI-ready workforce, Microsoft announced Intelligent Cloud Hub which has been launched " \
         "to empower the next generation of students with AI-ready skills. The program aims to build up the cognitive skills and in-depth understanding of " \
         "developing intelligent cloud connected solutions for applications across industry. This program also included developer-focused AI school that " \
         "provided a bunch of assets to help build AI skills. Earlier in April this year, the company announced Microsoft Professional Program In AI as a " \
         "learning track open to the public. That’s why it has become more critical than ever for educational institutions to integrate new cloud and AI " \
         "technologies. The program is an attempt to ramp up the institutional set-up and build capabilities among the educators to educate the workforce " \
         "of tomorrow."


# def get_content(topic):
#     base_url = "https://en.wikipedia.org/wiki/" + topic
#     page = requests.get(base_url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     paragraphs = soup.find_all('p')
#     content = ""
#     for para in paragraphs:
#         content += para.text
#     return content

def hello_luhn(text):
    summary = text.upper()
    return summary



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


def main():
    # topic_name = input("Enter the topic name for wikipedia article")
    content = raw_text
    cleaned_content = clean(content)
    threshold = len(cleaned_content) // 40
    frequency_dictionary = get_frequency_dictionary(cleaned_content)
    sorted_dictionary = {key: frequency_dictionary[key] for key in
                         sorted(frequency_dictionary, key=frequency_dictionary.get, reverse=True)[:word_limit]}
    sentence_scores = get_score(cleaned_content, sorted_dictionary)
    summary = get_summary(sentence_scores, sent_tokenize(content), threshold)
    print(summary)


if __name__ == "__main__":
    main()
