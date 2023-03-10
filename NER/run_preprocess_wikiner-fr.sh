#Run wikiner-fr data preprocessing!

echo "Run wikiner-fr data preprocessing!"
PATH_DATA="./wikiner-fr/"


START=$(date +%s)
python ./utils/convert_wikiner_to_conll.py -o $PATH_DATA
python ./utils/convert_to_bio.py -i $PATH_DATA'train.txt' -o $PATH_DATA'train_bio.txt'
python ./utils/convert_to_bio.py -i $PATH_DATA'test.txt' -o $PATH_DATA'test_bio.txt'
END=$(date +%s)
echo "preprocessing finished!"
echo Execution time was `expr $END - $START` seconds.