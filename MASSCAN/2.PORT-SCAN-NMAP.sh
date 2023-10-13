rm ./!!!PortScanNmap!!!.txt
for list in `cat !!!END-PING!!!.txt`; do echo $list >> !!!PortScanNmap!!!.txt && nmap -p 21,22,23,110,80,8291 $list | grep 'open' >> !!!PortScanNmap!!!.txt && echo '' >> !!!PortScanNmap!!!.txt; done
cat ./!!!PortScanNmap!!!.txt