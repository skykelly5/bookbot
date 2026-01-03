def get_num_words(text):
    return len(text.split())

def count_num_words(text):
    result = {}
    for char in text:
        check_word = char.lower()
        if char.lower() in result:
            result[check_word] += 1
        else:
            result[check_word] = 1  
    return result


def display_words_count(text_dictionary):
    result = []
    for k, v in text_dictionary.items():
        result.append({"char": k, "num": v})
    result.sort(reverse=True, key=lambda x: x["num"])
    return result
