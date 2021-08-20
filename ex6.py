import pyshark

# packet capture

capture = pyshark.LiveCapture()
for packet in capture.sniff_continuously(packet_count=5):
    print(packet)