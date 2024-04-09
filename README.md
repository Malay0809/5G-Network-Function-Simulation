"# 5G-Network-Function-Simulation" 
5G Network functions (Control Plane) like AMF, SMF, AUSF, NEF etc are simulated using Python.
Purpose- These simulation files will be helpful in Testing NF without deploying the real NF.

NF in 5G and their Work: 
1. Access and Mobility Management Function (AMF): Manages user equipment (UE) access and mobility. It handles UE registration, authentication, mobility management, and session management functions.
2. Session Management Function (SMF): Handles session-related functionalities, including session establishment, modification, and termination. It is responsible for assigning IP addresses to UEs, establishing Quality of Service (QoS) policies, and managing data flows within the session
3. User Plane Function (UPF): Handles user data forwarding in the data plane. It is responsible for packet routing, forwarding, and encapsulation/decapsulation. The UPF ensures efficient data transfer between UEs and external networks (e.g., the internet).
4. Authentication Server Function (AUSF): Provides authentication services for UEs. It validates the credentials of UEs during registration and authentication processes. It may also interact with external databases (such as Home Subscriber Server - HSS) to retrieve user authentication information
5. Unified Data Management (UDM): Manages user-related data and provides services such as user profile management, subscription management, and authentication credentials storage. It stores user-related data securely and ensures its availability to other network functions as needed
6. Network Slice Selection Function (NSSF): Determines the appropriate network slice for a given UE based on policy, QoS requirements, and other parameters. It selects and configures network slices to meet the specific needs of UEs or services
7. Policy Control Function (PCF): Enforces network policies related to QoS, traffic management, and access control. It interacts with other NFs to enforce policies based on service requirements, subscriber profiles, and network conditions
8. Network Exposure Function (NEF): Provides APIs (Application Programming Interfaces) to enable interaction between the 5G network and external services or applications. It facilitates service innovation, allowing third-party developers to access network capabilities securely
9. Network Repository Function (NRF): NRF serves as a critical component in 5G Core networks, enabling efficient resource discovery, service provisioning, and network management. Its role is essential for supporting the dynamic and flexible nature of 5G networks, where services and functions may be deployed and scaled dynamically to meet evolving demands
