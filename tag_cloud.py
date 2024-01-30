import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Generate a word cloud
def tag_cloud(text, hasil=None):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_text(text)

    # Display the generated word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # Return the hasil variable (if used for a specific purpose)
    return hasil

if __name__ == '__main__':
    pesan = "saya Jenderal saya ikut berkali-kali dalam aksi-aksi pertempuran saya saksi Saya melihat pemimpin yang bisa ambil keputusan"
    hasil = tag_cloud(pesan)

# If you have a reason for using the `hasil` variable, make sure to use it accordingly.
