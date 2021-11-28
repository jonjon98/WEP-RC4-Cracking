# WEP_RC4_Cracking_App


## Contents
1. [Background](#background)
2. [Motivation](#motivation)
3. [Research](#research)
4. [Design](#design)
5. [Development](#development)
6. [Code Usage](#code-usage)
7. [References](#references)


## Background
Wired Equivalent Policy (WEP) come out as part of the original 802.11 standard in 1997. It has seen a huge decrease in usage however due to weaknesses of the cipher that is incorporated in it being widely known. WEP uses the Alleged Rivest Cipher 4 (ARC4) algorithm for confidentiality and Cyclic Redundancy Check-32 (CRC-32) for integrity. 

![how_WEP_works](/Images/how_WEP_works.PNG)

In the snippet above, we can see how WEP works in general. The ARC4 algorithm used in WEP uses a combination of IV and pre-shared key as the input key. Assuming Alice wants to send a message to Bob over the WEP, she would first have to decide on a pre-shared key to be shared with Bob, then generate a keystream using ARC4, with the input key as the Initialization vector concatenated with the pre-shared key. The key stream will then XOR with the original message to produce a ciphertext. The IV and CT is then transmitted to Bob. With the pre-shared key on hand, Bob is able to generate the same keystream and decrypt the message by simply XOR-ing the cipher text to retrieve the plain text. One thing to note is that since the IV is sequential, each packet will be encrypted using a different ARC4 key due to the changing IV.

In this project, we would be focusing on cracking the ARC4 cipher in order to obtain the secret WEP key. This would allow us to demostrate the weakness of WEP and why most routers today default to other protocols such as WPA/WPA2.


## Motivation
**Why do we have to be concern over the vulnerabilities of WEP?**
As mentioned in the Alice and Bob scenario, the router encrypts the packet before sending over to the intended recipient. Even if there is a man in the middle attack, the attacker will only get the encrypted packet and they are unable to view the contents of the packet without the key. However, it is proven that there are severe vulnerabilities in WEP and the key can be easily obtained! With the shared key known, the encrypted messages now lose its secrecy and attackers can perform packets sniffing to observe their victim's network activities. This results in a severe bridge of privacy as well as confidentiality of the message sent, hence necessitate a stronger network security protocol.

Even though WEP cracking has been attempted before, and there are even industry standard tools to make cracking it simple for everyone, the concept behind the weaknesses of WEP, and by extension ARC4, is still an interesting one to explore further. We decided to choose this topic for our project as it can give us somemore insights as to why WEP is being phased out by other protocols and learn what weakness a seemingly strong cipher like ARC4 has. This can be linked to real life situations where we should be cautious of what we implement and do our due diligence.

## Research
We have started out by studying the WEP protocol, the ciphers it uses and the types of packets it would send. As our goal is to obtain the key of the WEP network, our study is more focused on the confidentiality of the WEP protocol which would be the ARC4 cipher, and the potential attacks against it. In the end we decided to go ahead with the Fluhrer, Mantin and Shamir (FMS) attack. The FMS attack in summary is an attack which exploits weaknesses in the initialisation vectors (IVs) of the WEP protocol using statistical analysis.

***For more details on FMS attack, refer to our presentation video***: https://youtu.be/mEKRhGqt4j0


## Design
Our project consists of 2 parts, a Jupyter Notebook file and a small application for anyone to use. The contents in both the parts are similar, consisting of the ARC4 algorithm, as well as the FMS attack algorithm. For the application, abstraction is used to make the design clean and user friendly such that even a person with no coding experience could successfully use the application. The actual WEP packet has the format shown below:

![WEP_packet_format](/Images/WEP_packet_format.gif)

However, for our own generated WEP packets, we would not need the "Header", "Key number" and "ICV" fields. Our packets only has the IV with the encrypted payload, the first byte of the payload is also our encrypted SNAP header of value 0xAA. This would be sufficient to demostrate the FMS attack.

*Disclaimer*: We did not manage to obtain a suitable WIFI adapter to be used to capture the WEP packets required to crack the ARC4 algorithm, so as an alternative, we decided to incorporate our own WEP packet generator which generates WEP packets in a csv file that would be later used to crack the ARC4 algorithm.


## Development
This section details the **tools and libraries** used in this project.

- **Jupyter Notebook**: pandas, numpy, csv
- **IDLE Python 3**: tkinter, csv


## Code Usage
This section serves as a guide and include **2 methods** to observe the demonstration of WEP password cracking.

### Jupyter Notebook
1. Download the ```ipynb Codes``` folder and run the ```RC4_encryption.ipynb``` file.
2. Run the codes line by line.
3. The codes are split into 2 sections: ***ARC4 Encryption and Decryption*** & ***Decryption of key using simulated WEP packets***.
  - ***ARC4 Encryption and Decryption***: 
    - Input the key and plain text.
    ```
    # Choose your key and plaintext
    key = "a1b2c3d4e5f6"
    plainText = "This is a plaintext."
    ```
    
    - Outcome
    
    ![ARC4 implementation image](/Images/rc4_implementation_output.jpg)

  - ***Decryption of key using simulated WEP packets***: 
    - Input the chosen key
    ```
    # Choose your key
    #Only accept hexadecimals as key & multiple of 2 chars
    WEP_key = "a1c24d3ce2"
    ```
    
    - Simulate the generation of the packets
   
    ![Generated packets image](/Images/generated_packets.jpg)
    
    - Retrieval of the key by exploiting ARC4 vulnerabilities.

    ![Retrieve key out](/Images/retrieve_key_output.jpg)

### Application
1. Download the ```Application Codes``` folder and run the ```Main.py``` file with the command prompt or your preferred Python IDE.
2. A new application window with the title "Attack on WEP wtih ARC4 encryption"_ should appear.
3. Input the chosen **key** and **plain text** and hit the **enter** button.
4. To observe the ARC4 implementation alone, utilize the **"Encrypt"** and **"Decrypt"** buttons.
5. To observe the decryption of key over the WEP network, utilize the **"Generate"** button to simulate the generation of filtered WEP packets with ARC4 encryption and the **"Retrieve key"** button to decrypt the key from analysing the simulated packets.
6. Observe the results displayed in the bottom frame.

**Snippet of demo application**

![Demo application snippet](/Images/demo_application.jpg)


## References
WEP protocol: https://www.techtarget.com/searchsecurity/definition/Wired-Equivalent-Privacy

FMS attack: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.16.2068&rep=rep1&type=pdf

WEP packet format: https://flylib.com/books/en/2.519.1/wep_cryptographic_operations.html

Tkinter: https://www.sourcecodester.com/tutorials/python/12494/python-import-csv-file-tkinter-table.html
