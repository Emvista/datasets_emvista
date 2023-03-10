#Run wikiner-fr data preprocessing!

echo "Run wikipedia-ner -fr data preprocessing!"
PATH_DATA="./wikpedia-ner/"


START=$(date +%s)
python ./utils/prepare_data_emvista_wikipedia-ner.py -i $PATH_DATA'wikipedia-ner-emvista.txt' -o $PATH_DATA'wikipedia-ner-emvista_bio.txt'
#python ./utils/convert_to_bio.py -i $PATH_DATA'wikipedia-ner-emvista_conll.txt' -o $PATH_DATA'wikipedia-ner-emvista_conll_bio.txt'

END=$(date +%s)
echo "preprocessing finished!"
echo Execution time was `expr $END - $START` seconds.