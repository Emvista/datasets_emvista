"""
Author @ Sylvain Verdy Mars 2023
"""

import argparse
from datasets import load_dataset
dataset = load_dataset("Jean-Baptiste/wikiner_fr")


def main(type_data):    

    dict_labels = {
        0 : "O",
        1 : "Location",
        2 : "Person",
        3 : "Misc",
        4 : "Organization"
    }

    list_of_list_labels = []
    labels = dataset[str(type_data.replace(".txt",""))]["ner_tags"]
    for i in range(0, len(labels)):
        list_labels = []
        for label in labels[i]:
            list_labels.append(dict_labels[label])
        list_of_list_labels.append(list_labels)
    list_of_sentences = dataset[str(type_data.replace(".txt",""))]["tokens"]


    list_of_tags = []
    assert len(list_of_sentences) == len(list_of_list_labels)
    for i, sentence in enumerate(list_of_sentences):
        labels_sentence = list_of_list_labels[i]
        for a, word in enumerate(sentence):
            list_of_tags.append(word + "\t" + labels_sentence[a])
        list_of_tags.append("")

    n_names = ["{}\n".format(i) for i in list_of_tags ]


    with open(params["output_path"] + type_data, "w") as file:
        file.writelines(n_names)
        file.close()    



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Arguments for the DWIE Preprocessing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


    parser.add_argument(
        "-o",
        "--output_path",
        help="Path to the dwie content directory",
        default="./new_data/",
    )

    args = parser.parse_args()
    params = vars(args)
    print("build data to tsv format")
    main("train.txt")
    main("test.txt")




        