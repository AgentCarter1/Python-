#include <stdio.h>
#include <stdlib.h>
#include <pcap.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <arpa/inet.h>

#define ETHERNET_HEADER_SIZE 14

void processIEC104Packet(const u_char *payload, int length, const char *srcIP, const char *dstIP) {
    // IEC 104 paketinin verilerini burada ayrıştırabilir ve ekrana yazabilirsiniz
    // payload: IEC 104 paketinin veri bölümü
    // length: IEC 104 paketinin veri bölümü uzunluğu
    // srcIP: Kaynak IP adresi
    // dstIP: Hedef IP adresi

    // Başlangıç, uzunluk, kontrol, adres, tip, veri ve özet (checksum) bilgilerini ayrıştırarak terminale yazdırma
    unsigned char start = payload[0];
    unsigned char packetLength = payload[1];
    unsigned char control = payload[2];
    unsigned char address = payload[3];
    unsigned char asduType = payload[5];
    unsigned short asduAddress = (payload[6] << 8) | payload[7];
    unsigned short ioAddress = (payload[8] << 8) | payload[9];
    unsigned short checksum = (payload[length - 2] << 8) | payload[length - 1];

    printf("Source IP: %s\n", srcIP);
    printf("Destination IP: %s\n", dstIP);
    printf("Start: 0x%02X\n", start);
    printf("Length: %d\n", packetLength);
    printf("Control: 0x%02X\n", control);
    printf("Address: 0x%02X\n", address);
    printf("ASDU Type: 0x%02X\n", asduType);
    printf("ASDU Address: %d\n", asduAddress);
    printf("IO Address: %d\n", ioAddress);
    printf("Checksum: 0x%04X\n", checksum);
    printf("\n");
}

int main() {
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct pcap_pkthdr *header;
    const u_char *packet;
    char *dev;
    struct ip *iph;
    struct tcphdr *tcph;
    const u_char *payload;

    // Ağ arabirimini belirleme
    dev = "lo";

    // Ağ arabirimini açma
    handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
        printf("Ağ arabirimini açma hatası: %s\n", errbuf);
        return 1;
    }

    // Paketleri dinleme
    while (1) {
        int res = pcap_next_ex(handle, &header, &packet);
        if (res == 0)
            continue;
        else if (res == -1 || res == -2) {
            printf("Paket alma hatası: %s\n", pcap_geterr(handle));
            break;
        }

        // Ethernet başlığını atla
        packet += ETHERNET_HEADER_SIZE;

        // IP başlığını al
        iph = (struct ip *)packet;

        // TCP başlığını al
        tcph = (struct tcphdr *)(packet + iph->ip_hl * 4);

        // Payload (veri) bölümünü al
        payload = packet + iph->ip_hl * 4 + tcph->doff * 4;

        // Sadece IEC 104 paketlerini işle
        if (tcph->dest == htons(2404)) {
            int payloadLength = ntohs(iph->ip_len) - (iph->ip_hl * 4 + tcph->doff * 4);
            char srcIP[INET_ADDRSTRLEN];
            char dstIP[INET_ADDRSTRLEN];
            inet_ntop(AF_INET, &(iph->ip_src), srcIP, INET_ADDRSTRLEN);
            inet_ntop(AF_INET, &(iph->ip_dst), dstIP, INET_ADDRSTRLEN);
            processIEC104Packet(payload, payloadLength, srcIP, dstIP);
        }
    }

    // Ağ arabirimini kapatma
    pcap_close(handle);

    return 0;
}