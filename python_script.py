import nltk
from nltk.corpus import stopwords
nltk.download('punkt')

with open('paragraphs.txt', 'r') as file:
    main_file = file.read()

nltk.download('stopwords')

stop_words= set(stopwords.words('english'))

#tokenizes string into a list of words or tokens
word_tokens = nltk.word_tokenize(main_file)

#filter stopwords
filtered_text = []
for word in word_tokens:
    if word.lower() not in stop_words:
        filtered_text.append(word)

#joins words back into a single string separated by spaces
clean_text = ' '.join(filtered_text)

words = main_file.split()
num_words = len(words)
print("number of words before removing stopwords",num_words)

clean_words = len(filtered_text)
print("number of words after removing stopwords",clean_words)

word_freq = {}

# Count the frequency of each word
for word in filtered_text:
    # Increment the count for each word
    word_freq[word] = word_freq.get(word, 0) + 1

# Print the word frequencies
for word, freq in word_freq.items():
    print(f"Word: {word}, Frequency: {freq}")
