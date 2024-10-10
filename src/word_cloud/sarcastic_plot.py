import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
from nltk.corpus import stopwords

data = pd.read_csv('Sarcasm_data_1.csv')
print(data.head())
print(data.info())

# find stopwords
nltk.download('stopwords')
stopwords_list = stopwords.words('english')

Sarcastic_text=''.join(data['headline'][data['is_sarcastic']==1].tolist())
word_cloud = WordCloud(width=800,height=400, background_color='black').generate(Sarcastic_text)

plt.figure(num=1, figsize=(10,5))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.title('Sarcastic')
plt.show
