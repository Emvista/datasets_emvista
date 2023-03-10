#Run wikiner-fr data preprocessing!

echo "Run wikipedia-ner -fr data preprocessing!"
PATH_DATA="./jules-verne/"


START=$(date +%s)
python ./utils/prepare_data_emvista_jules_verne.py -i $PATH_DATA'jules-verne.txt' -o $PATH_DATA'jules-verne_bio.txt'

END=$(date +%s)
echo "preprocessing finished!"
echo Execution time was `expr $END - $START` seconds.