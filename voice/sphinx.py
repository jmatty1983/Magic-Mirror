from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='hey otis', kws_threshold=1e-10)
for phrase in speech:
    print(phrase.segments(detailed=True))