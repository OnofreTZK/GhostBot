import pandas as pd

emojiDF = pd.read_html('https://unicode.org/emoji/charts/full-emoji-list.html')[0]

emojiDF.to_csv('emojis.csv', sep=';', index=False)
