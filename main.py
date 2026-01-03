from stats import count_num_words as count_num_words, get_num_words as get_num_words, display_words_count as display_words_count  
import sys


def get_book_text(filepath): 
    with open(filepath) as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)  


    filepath = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    # Get text and count words
    text = get_book_text(filepath)
    word_count = get_num_words(text)
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Count characters
    char_dict = count_num_words(text)
    sorted_chars = display_words_count(char_dict)
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")

main()

