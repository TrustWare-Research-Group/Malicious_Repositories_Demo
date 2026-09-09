#!/bin/bash
# usage: ./test.sh
# uses auto_receiver.sh (scripted commands) so this can run unattended -
# for a real interactive session, run receiver.sh yourself instead and skip this.

./auto_receiver.sh > /tmp/receiver_output.txt 2>&1 &
sleep 1

./monitor.sh torchsight-0669 &
sleep 2

python3 trigger.py 2>&1 | tee /tmp/run_output.txt

sleep 2
sudo pkill -INT -f "tcpdump -i lo"
sleep 1

LATEST=$(ls -t evidence/ | head -1)
sudo chown "$(id -u)":"$(id -g)" "evidence/$LATEST/capture.pcap"
cp /tmp/run_output.txt "evidence/$LATEST/run_output.txt"
cp /tmp/receiver_output.txt "evidence/$LATEST/receiver_output.txt"

echo "=== evidence dir: evidence/$LATEST ==="
ls -la "evidence/$LATEST"
echo
echo "=== what the reverse shell returned ==="
cat /tmp/receiver_output.txt
