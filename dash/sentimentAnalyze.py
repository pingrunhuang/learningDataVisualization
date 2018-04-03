from textblob import TextBlob

analysis = TextBlob("TextBlob sure looks like it has some interesting features!")

print(analysis.translate(to="es"))