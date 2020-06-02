from src.lib import *

# NLP and webscrapping based article/report creator
# author: Krzysztof Kramarz

# our hyperparameters
topic = 'machine learning basics' # Topic of an article
sentence_quality = 0.4 # variable describing quality of the sentence
number_of_articles = 10 # number of articles scipt will be scrapping
change_to_synonym_chance = 0.2
article_randomness = 0.2
max_word_len = 10

if len(argv) > 1:
    topic = argv[1]

start = time()

# first we need to get the urls from google search
urls = get_urls(topic = topic, number_of_articles = number_of_articles, article_randomness = article_randomness )

# next we have to download each of these pages and get text/images from them
articles, images = get_and_clean_response(urls)

# we download some hot images
download_images(images)

# cleaning articles from bad stuff
cleaned_articles = get_cleaned_articles(articles = articles, max_word_len = max_word_len, change_to_synonym_chance = change_to_synonym_chance, sentence_quality = sentence_quality)

# random article emarges
random_article = create_random_article(cleaned_articles)

# we save our article to the .docx file with some paragraphs, headers and images
create_document(random_article = random_article, topic = topic)

print('whole process took: ', (time()  - start)/60, 'min')