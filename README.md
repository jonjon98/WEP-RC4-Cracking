# WEP_RC4_Cracking_App

Video Presentation Link: https://youtu.be/mEKRhGqt4j0

## Background
Wired Equivalent Policy (WEP) come out as part of the original 802.11 standard in 1997. It has seen a huge decrease in usage however due to weaknesses of the cipher that is incorporated in it being widely known. WEP uses the Alleged Rivest Cipher 4 (ARC4) algorithm for confidentiality and Cyclic Redundancy Check-32 (CRC-32) for integrity. In this project, we would be focusing on cracking the ARC4 cipher in order to obtain the secret WEP key. This would allow us to demostrate the weakness of WEP and why most routers today default to other protocols such as WPA/WPA2.

## Motivation











## Development



## Code Usage
This section serves as a guide and include 2 methods to observe the demonstration of WEP password cracking.

### Jupyter Notebook
1. Download the _ipynb Codes_ folder and run the _RC4\_encryption.ipynb_ file.
2. Run the codes line by line.
3. The codes are split into 2 sections: **ARC4 Encryption and Decryption** & **Decryption of key over using simulated WEP packets**.
  - To observe the ARC4 implementation alone, input the key and plain text when required and observe the code line output.
  - To observe the decryption of key over the WEP network, we first simulate the generation of the packets, followed by the retrieval of the key by exploiting ARC4 vulnerabilities.

### Application
1. Download the _Application Codes_ folder and run the _Main.py_ file with the command prompt or your preferred Python IDE.
2. A new application window with the title _"Attack on WEP wtih ARC4 encryption"_ should appear.
3. Input the chosen **key** and **plain text** and hit **enter**.
4. To observe the ARC4 implementation alone, utilize the **"Encrypt"** and **"Decrypt"** buttons.
5. To observe the decryption of key over the WEP network, utilize the **"Generate"** button to simulate the generation of filtered WEP packets with ARC4 encryption and the **"Retrieve key"** button to decrypt the key from analysing the simulated packets.
6. Observe the results displayed in the bottom frame.
