


def get_numbers_of_words(text_book):
    return len(text_book.split())

def num_of_characters(text_book = ""):
    freq = {}
    tl = text_book.lower()
    for ch in set(tl):
        freq[ch] = tl.count(ch)
    return freq

def sort_on(dict):
    return dict["count"]

def sorted_dict(dict = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494}):
    list_pares = list(dict.items())
    list_dict = []
    for key, value in list_pares:
        list_dict.append({"character": key, "count": value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict