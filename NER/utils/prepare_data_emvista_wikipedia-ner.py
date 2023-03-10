from __future__ import unicode_literals, print_function

from tqdm import tqdm
from collections import deque
import string
import argparse

def prepare_data(data):
    list_elements = deque()
    list_labels = deque()
    list_labels_by_sentences = []
    list_sentences = []
    for row in tqdm(range(0, len(data)), disable=True):
        if data[row] != '\n':
            sentence = data[row].split('\t')
            if len(sentence[0].split()) > 1:
                for i in sentence[0].split(" "):

                    list_elements.append(i.split('\n')[0])
                    
                    if len(sentence)>1 :
                        list_labels.append(sentence[1].split('\n')[0])
                    else:
                        list_labels.append("O")
            else:
                list_elements.append(sentence[0].split('\n')[0])
                if len(sentence)>1 :
                    list_labels.append(sentence[1].split('\n')[0])
                else:
                    list_labels.append("O")

        if data[row] == '\n':
            
            list_sentences.append(' '.join(list_elements))
            list_labels_by_sentences.append(' '.join(list_labels))
            assert len(list_elements) == len(list_labels)
            
            list_labels.clear(), list_elements.clear()


    list_elements_file = []

    for i, word in enumerate(list_elements):
        if word != "":
            list_elements_file.append(word +"\t" + list_labels[i].replace("nerd:", "")) 
        elif word =="":
            list_elements_file.append("") 


    n_names = ["{}\n".format(i) for i in list_elements_file] 

    with open(params["output_path"], "w") as file:
        file.writelines(n_names)
        file.close()    


def main():

    data = open(params["input_path"], 'r').readlines()
    prepare_data(data)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Arguments for the DWIE Preprocessing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--input_path",
        help="Path to the dwie content directory",
        default="./new_data/",
    )

    parser.add_argument(
        "-o",
        "--output_path",
        help="Path to the dwie content directory",
        default="./new_data/",
    )

    args = parser.parse_args()
    params = vars(args)
    main()

