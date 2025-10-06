def get_num_words(text):
    return len(text.split())

def get_letter_count(text):
    lowered = text.lower()
    letter_counts = {}
    for ch in lowered:
        if  ch not in letter_counts:
            letter_counts[ch] = 0
        letter_counts[ch] += 1
    return letter_counts

def get_sorted_list(dictionary):
    sorted_list = []
    for k, v in dictionary.items():
        sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(item):
    return item["num"]