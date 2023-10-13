rm ./!!!PortScanMasscan!!!.txt
masscan -p 21,22,23,161,80,8291 -iL '!!!END-PING!!!.txt' --rate=100 |awk '{print $6,$4}' | sort -nr >> '!!!PortScanMasscan!!!.txt'
cat ./!!!PortScanMasscan!!!.txt