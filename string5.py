from operator import itemgetter


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    nw = sorted(word_len, key=itemgetter(0))
    print(str(nw))
    return nw[-1][1]


print(find_longest_word(["PHP", "Exercises", "Backend"]))
