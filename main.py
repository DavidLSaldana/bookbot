

def main():

    path = "./books/frankenstein.txt"

    file_contents = get_file_text(path)
    number_of_words = count_words_in_book(file_contents)
    counter = count_characters_in_book(file_contents)
    report = get_list_from_dict(counter)
    output_report(path, number_of_words, report)


def count_characters_in_book(contents):
    contents = contents.lower()
    counter = {}
    words = contents.split()
    for word in words:
        for letter in range(0, len(word)):
            if str(word[letter]).isalpha():
                if word[letter] not in counter:
                    counter[word[letter]] = 1
                else:
                    counter[word[letter]] +=1
    return counter
    

def get_file_text(path):
    with open(path) as book:
        return book.read()

def count_words_in_book(contents):
    words = contents.split()
    return len(words)
    
def get_list_from_dict(counter_dictionary):
    list = []
    for dict in counter_dictionary:
        list.append({"letter":dict, "count":counter_dictionary[dict]})
    return list

def sort_on(dict):
    return dict["count"]

def output_report(path, number_of_words, report):
    report.sort(reverse=True,key=sort_on)
    print (f"--- Begin report of {path} ---")
    print(f"{number_of_words} words found in the document\n\n")
    for letter in range(0,len(report)):
        current = report[letter]
        letter_key = "letter"
        count_key = "count"
        print (f"The '{current[letter_key]}' character was found {current[count_key]} times")
    print (f"--- End report of {path} ---")

main()
