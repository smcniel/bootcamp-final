# Basic Idea
An experimental Search query tool using Word2Vec. Perhaps implemented as a game played in the browser.

# Word2Vec Intro
(Introduction borrowed from DL4J: https://deeplearning4j.org/word2vec)

Word2vec is a two-layer neural net that processes text. Its input is a text corpus and its output is a set of vectors: feature vectors for words in that corpus. While Word2vec is not a deep neural network, it turns text into a numerical form that deep nets can understand.

Word2vec’s applications extend beyond parsing sentences in the wild. It can be applied just as well to genes, code, likes, playlists, social media graphs and other verbal or symbolic series in which patterns may be discerned.

Why? Because words are simply discrete states like the other data mentioned above, and we are simply looking for the transitional probabilities between those states: the likelihood that they will co-occur.

The purpose and usefulness of Word2vec is to group the vectors of similar words together in vectorspace. That is, it detects similarities mathematically. Word2vec creates vectors that are distributed numerical representations of word features, features such as the context of individual words. It does so without human intervention.

# Project Details
Initial trained model will use Google's News Corpus dataset.
Future models trained on more biased text frameworks, similar to my master's thesis project.
Word2Vec model will use the Skip-Gram Negative Sampling.
Search queries from the browser via API calls.

# Basic Timeline
Week 1: Complete wireframe designs for both front and backend.
Week 2: Finish model training.
Week 3: Front end web development.
Week 4: Buffer for troubleshooting and luxury goals. Presentation finalize.

# Tech Dependencies
Python, Gensimm, Theano, Keras for training the NNs on CUDA enabled machine.
Flask or Django for API calls to final trained model.
Javascript, SASS, GULP for Web Development of User Interface.


Test performance time on NVIDIA GPU. Probably not necessary to set up distributed computing, as Word2Vec is trained sequentially.
