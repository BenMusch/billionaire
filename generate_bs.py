from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file(file_path='data/tweets.txt', num_epochs=5)
for _ in range(100):
    print(textgen.generate())
