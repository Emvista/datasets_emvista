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

                if list_elements[-1] in ["?", "!", "."] and list_labels[-1] == "O":
                    list_elements.append("")
                    list_labels.append("")
        if data[row] == '\n':
            

            list_sentences.append(' '.join(list_elements))
            list_labels_by_sentences.append(' '.join(list_labels))
            assert len(list_elements) == len(list_labels)
            
            list_labels.clear(), list_elements.clear()
    
    if len(list_sentences) == 0:
        list_sentences.append(' '.join(list_elements))
        list_labels_by_sentences.append(' '.join(list_labels))


    list_elements_file = []

    for i, word in enumerate(list_elements):
        if word != "":
            list_elements_file.append(word +"\t" + list_labels[i]) 
        elif word =="":
            list_elements_file.append("") 


    n_names = ["{}\n".format(i) for i in list_elements_file] 

    with open(params["output_path"], "w") as file:
        file.writelines(n_names)
        file.close()    

    return list_labels_by_sentences, list_sentences



def transforms_data_to_bio(labels, words):
    past_label = "O"
    list_elements = []
    for i, word in enumerate(words):
        if past_label == "O" and labels[i] != "O": 
            past_label = labels[i]
            labels[i] = labels[i].replace("nerd:", "B-")
            list_elements.append(words[i] + '\t' + labels[i])
        elif past_label == labels[i] and past_label !="O":
            past_label = labels[i]
            labels[i] = labels[i].replace("nerd:", "I-")
            list_elements.append(words[i] + '\t' + labels[i])

        else:
            list_elements.append(words[i] + "\t" +"O")

            if words[i] in ["?", "!", "."] and labels[i] == "O":

                list_elements.append("")

            past_label = "O"
    list_elements_file = []

    for i, word in enumerate(words):

        list_elements_file.append(word +"\t" + labels[i]) 
        if word =="":
            list_elements_file.append("") 


    n_names = ["{}\n".format(i) for i in list_elements ]


    with open(params["output_path"], "w") as file:
        file.writelines(n_names)
        file.close()    


def main():

    data = open(params["input_path"], 'r').readlines()
    labels, words = prepare_data(data)
    transforms_data_to_bio(labels[0].split(), words[0].split())




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

