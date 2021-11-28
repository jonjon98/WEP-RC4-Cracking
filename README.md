# WEP_RC4_Cracking_App

Video Presentation Link: https://youtu.be/mEKRhGqt4j0

## Background
Wired Equivalent Policy (WEP) come out as part of the original 802.11 standard in 1997. It has seen a huge decrease in usage however due to weaknesses of the cipher that is incorporated in it being widely known. WEP uses the Alleged Rivest Cipher 4 (ARC4) algorithm for confidentiality and Cyclic Redundancy Check-32 (CRC-32) for integrity. In this project, we would be focusing on cracking the ARC4 cipher in order to obtain the secret WEP key. This would allow us to demostrate the weakness of WEP and why most routers today default to other protocols such as WPA/WPA2.


## Motivation
Even though WEP cracking has been attempted before, and there are even industry standard tools to make cracking it simple for everyone, the concept behind the weaknesses of WEP, and by extension ARC4, is still an interesting one to explore further. We decided to choose this topic for our project as it can give us somemore insights as to why WEP is being phased out by other protocols and learn what weakness a seemingly strong cipher like ARC4 has. 


## Research
We have started out by studying the WEP protocol, the ciphers it uses and the types of packets it would send. As our goal is to obtain the key of the WEP network, our study is more focused on the confidentiality of the WEP protocol which would be the ARC4 cipher, and the potential attacks against it. In the end we decided to go ahead with the Fluhrer, Mantin and Shamir (FMS) attack. The FMS attack in summary is an attack which exploits weaknesses in the initialisation vectors (IVs) of the WEP protocol using statistical analysis.

***For more details on FMS attack, refer to our presentation video***: https://youtu.be/mEKRhGqt4j0
[Go to Real Cool Heading section](##background)


## Design
Our project consists of 2 parts, a Jupyter Notebook file and a small application for anyone to use. The contents in both the parts are similar, consisting of the ARC4 algorithm, as well as the FMS attack algorithm. For the application, abstraction is used to make the design clean and user friendly such that even a person with no coding experience could successfully use the application. 

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
    
    ![ARC4 implementation image](/rc4_implementation_output.JPG)

  - ***Decryption of key using simulated WEP packets***: 
    - Input the chosen key
    ```
    # Choose your key
    #Only accept hexadecimals as key & multiple of 2 chars
    WEP_key = "a1c24d3ce2"
    ```
    
    - Simulate the generation of the packets
   
    ![Generated packets image](/generated_packets.JPG)
    
    - Retrieval of the key by exploiting ARC4 vulnerabilities.

    ![Retrieve key out](/retrieve_key_output.JPG)

### Application
1. Download the ```Application Codes``` folder and run the ```Main.py``` file with the command prompt or your preferred Python IDE.
2. A new application window with the title "Attack on WEP wtih ARC4 encryption"_ should appear.
3. Input the chosen **key** and **plain text** and hit the **enter** button.
4. To observe the ARC4 implementation alone, utilize the **"Encrypt"** and **"Decrypt"** buttons.
5. To observe the decryption of key over the WEP network, utilize the **"Generate"** button to simulate the generation of filtered WEP packets with ARC4 encryption and the **"Retrieve key"** button to decrypt the key from analysing the simulated packets.
6. Observe the results displayed in the bottom frame.

**Snippet of demo application**

![Demo application snippet](/demo_application.JPG)
