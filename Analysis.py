from nltk.sentiment import SentimentIntensityAnalyzer as sa
from nltk.tokenize import sent_tokenize
import pyphen
import string
from nltk.corpus import stopwords
import re


#calling the text files, stop words, postive and negative words into python
text=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\39.txt',encoding='utf-8').read()
textsplit=text.split()

positive_wordstext=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\positive-words.txt').read()
positivewords=positive_wordstext.split()

negative_wordstext=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\negative-words.txt').read()
negativewords=negative_wordstext.split()

stopwords_auditor=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_Auditor.txt').read()
auditor=stopwords_auditor.split()

stopwords_currencies=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_Currencies.txt').read()
currencies=stopwords_currencies.split()

stopwords_datenumbers=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_DatesandNumbers.txt').read()
datenumbers=stopwords_datenumbers.split()

stopwords_generic=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_Generic.txt').read()
generic=stopwords_generic.split()

stopwords_genericlong=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_GenericLong.txt').read()
genericlong=stopwords_genericlong.split()

stopwords_names=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_Names.txt').read()
names=stopwords_names.split()

stopwords_geographic=open('C:\\Users\\vishv\\Desktop\\VS PYTHON\\StopWords_Geographic.txt').read()
geographic=stopwords_geographic.split()


no_stopwords=set(textsplit)-set(auditor)-set(currencies)-set(datenumbers)-set(generic)-set(genericlong)-set(names)-set(geographic)

#print(no_stopwords)

#simple test of sentiment analyzer
s=sa()
v=s.polarity_scores(text)
print(v)

################################################1.Sentimental Analysis################################################################


positive_score=[]
negative_score=[]


for word in no_stopwords:
    if word not in negativewords:
        positive_score.append(word)
    elif word not in positivewords:
        negative_score.append(word)    

print('positive score =',len(positive_score)) 
print('negative score =',len(negative_score))


#polarity score
polarity_score=(len(positive_score)-len(negative_score))/((len(positive_score)+len(negative_score)+0.000001))
print("polarity score = ",polarity_score)

#Subjectivity Score
subjectivity_score=(len(positive_score)+len(negative_score))/((len(no_stopwords))+0.000001)
print('Subjectivity Score = ',subjectivity_score)

#################################################2.Analysis of Readability####################################################
# Identify the average sentence length ==== average number of words per sentence

noof_sentences=text.split('.')
print('number of sentences in article = ',len(noof_sentences))
print('article words = ',len(textsplit))
numberofwordspersentence=len(textsplit)/len(noof_sentences)
print('average sentence length = ',numberofwordspersentence)
# Identify the complex words

dic = pyphen.Pyphen(lang='en')
def count_syllables(word):
    return len(dic.inserted(word).split('-'))

complex_words = []  
for c_word in textsplit:
    syllable_count = count_syllables(c_word)
    if syllable_count > 2:
        complex_words.append(c_word)


percofcomplexwords=(len(complex_words)/len(textsplit))*100       #### Finding the percentage of complex words####
print('percentage of complex words = ', percofcomplexwords)
fogindex=0.4*((len(textsplit)/len(noof_sentences)+(len(complex_words)/len(textsplit))*100))
print('fog index = ',fogindex)


##############################################3. Average Number of Words Per Sentence#########################

print('Average Number of Words Per Sentence = ',numberofwordspersentence)

##############################################4.Complex Word Count#############################################

print('complex words = ',len(complex_words))


##############################################5.Word Count##################################################

word_text=text.translate(str.maketrans(' ',' ',string.punctuation ))  ####here removing punctuations####
word_count=word_text.split()

set_stopwords = set(stopwords.words('english'))                       ####here I am using stopwords from nltk stopwords####
print('word count = ',len(word_count)-len(set_stopwords))


###############################################6.Syllable Count Per Word######################################

def syllables(word):
    
    vowel_pattern = re.compile(r'[aeiouy]+', re.IGNORECASE) ####  regular expression to match vowels#####
    
    
    num_vowels = len(vowel_pattern.findall(word))           #### Count the number of matches of the vowel pattern in the word####
    
   
    if word.endswith('es') or word.endswith('ed'):
        num_vowels -= 1
    
    
    return max(num_vowels, 1)                                #### Return the number of syllables####
    

syllable_counts = [count_syllables(syll) for syll in textsplit]
print('syllable count per word = ',len(syllable_counts))




###############################################7.Personal Pronouns##############################################

pronoun_pattern = re.compile(r'\b(I|we|my|ours|us)\b', re.IGNORECASE)    ####regular expression to match the personal pronouns####


num_pronouns = len(pronoun_pattern.findall(text))                        ####Count the number of matches of the pronoun pattern in the text####


print("number of personal pronouns:", num_pronouns)                      #### Print the result#####


###############################################8.Average Word Length##############################################

total_characters = sum(len(textsplit) for wordchar in textsplit)
print('average Word Length = ',(total_characters) / len(textsplit))



####################################################################################################################
##############################################     Thank You    ####################################################
####################################################################################################################



    










    








  
  



