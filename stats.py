def get_num_words(contents):
    return len(contents.split())


def count_chars(contents):
    contents = contents.lower()
    freq = {}

    for char in contents:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq



def sort_chars_freq(char_frequency_dict: dict):
    # sort_freq = dict(sorted(char_freq.items(), key=lambda item: item[1], reverse=True))
    sorted_items = sorted(char_frequency_dict.items(), key=lambda item: item[1], reverse=True)

    sorted_list_of_dicts = []
    for char, num in sorted_items:
        sorted_list_of_dicts.append({"char": char, "num": num})

    return sorted_list_of_dicts
