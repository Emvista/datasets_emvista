import logging
import argparse
import os
import json
from tqdm import tqdm
import re, string
from collections import deque




def prepare_data(data):
    list_elements = deque()
    list_labels = deque()
    list_labels_by_sentences = []
    list_sentences = []
    for row in tqdm(range(0, len(data)), disable=False):
        if data[row] != '\n':
            sentence = data[row].split('\t')
            if len(sentence[0].split()) > 1:
                for i in sentence[0].split(" "):

                    list_elements.append(i.split('\n')[0])
                    if len(sentence)>1 :
                        list_labels.append(sentence[1].split('\n')[0])
                    else:
                        list_labels.append("O")
                    #list_labels.append(sentence[1].split('\n')[0]) #.split('\n')[0])
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
    
    if len(list_sentences) == 0:
        list_sentences.append(' '.join(list_elements))
        list_labels_by_sentences.append(' '.join(list_labels))
    assert len(list_labels_by_sentences) ==len(list_sentences)

    return list_labels_by_sentences, list_sentences



class BIO_convertor:
    def __init__(self, path_file_origin, save_file) -> None:
        self.path_file_origin = self.read_file(path_file_origin)
        self.labels, self.origin = prepare_data(self.path_file_origin)
        self.save_file = save_file
        self.save_file_data()
        
        
    def read_file(self, path):
        data = open(path, 'r').readlines()
        return data

    def save_file_data(self,):
        
        list_word_tag = []
        prev_label = "O"
        for i in tqdm(range(0, len(self.origin))):
            sentence = self.origin[i].split()
            labels = self.labels[i].split()
            for a in tqdm(range(0, len(sentence)), disable=True):
                label = labels[a]
                if label == 'O':
                    list_word_tag.append(sentence[a] + '\t' + 'O')
                    prev_label = label
                elif label == "":
                    prev_label = "O"
                else:
                    if prev_label == 'O' or label != prev_label.split("-")[1] :
                        label = f'B-{label}'
                        list_word_tag.append(sentence[a] + '\t' + label)

                    else:
                        if prev_label !="O":
                            label = f'I-{label}'
                            list_word_tag.append(sentence[a] + '\t' + label)
                        else:
                            print("here")
                    prev_label = label

            list_word_tag.append("")

        n_names = ["{}\n".format(i) for i in list_word_tag]

        with open(self.save_file, "w") as file:
            file.writelines(n_names)
            file.close()    

def main():

    convert = BIO_convertor(params['input_path'], params['output_path'])


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




        