import re

def parse_speed_to_mbps(speed_str):
   
    match = re.match(r'(\d+)([KkMmGg])bps', speed_str)
    if match:
        speed = float(match.group(1))
        unit = match.group(2).upper()

        
        if unit == 'K':
            speed /= 1000
        elif unit == 'G':
            speed *= 1000

        return speed
    else:
        return None


tx_speed_str = "90Mbps-40MHz/1S/SGI"
rx_speed_str = "243Mbps-40MHz/2S"


tx_speed_mbps = parse_speed_to_mbps(tx_speed_str)
rx_speed_mbps = parse_speed_to_mbps(rx_speed_str)

print("Швидкість передачі даних (Mbps):", tx_speed_mbps)
print("Швидкість прийому даних (Mbps):", rx_speed_mbps)
