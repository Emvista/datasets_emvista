echo "start all preprocessing !"
START=$(date +%s)

echo "preprocess wikiner-fr dataset"
./run_preprocess_wikiner-fr.sh

echo "preprocess wikipedia-ner dataset"
./run_preprocess_wikipedia-ner.sh

echo "preprocess Jules-Verne dataset"
./run_preprocess_jules-verne.sh

END=$(date +%s)
echo "preprocessing for all dataset finished!"
echo Execution time was `expr $END - $START` seconds.