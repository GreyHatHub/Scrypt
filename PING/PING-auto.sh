rm ./!!!END-PING!!!.txt
for list in `cat pinglist`; do ping -c 1 $list | grep 'ttl'|awk '{print $4}'| cut -d ":" -f 1 >> !!!END-PING!!!.txt; done 
cat ./!!!END-PING!!!.txt