# VSSM
*Very Simple Sales Manager* 
*(Better Name can be proposed)*

#### *This program for now its in a pre-working state, its really not ready to use in a regular manner*

VSSM aims to help with keeping a control of the sales
by providing a client driven classification of data, 
somebasic inventory control and summarys of data.

For its initial development only cli will be used, without 
any fancy interface, after this a "front end" will be developed 
to use on cellphones and computers alike, adding support for connecting to "backend"
either to an internet server or to a local server, as well as adding more features.

*Initial development will be over when all inicial 
feauters are implemented*

>Note:
>
>     Me, the creator of this repository is just a computation student who would like to help his family in their bussiness while learning more general programming skills.
>     I dont have advanced programming skills or a deep database/bussiness knowledge, so if you se me doing something wrong or outright horrific, just tell me, i'll be glad to hear anything to improve.
---
## Initial Features

-   **Client list**
    -   Clients names, and optional information.
    -   basic info like current debt

-   **Client detailed info**
    -   Client purchases History and info
    -   on a purchase by purchase basis

    -   debt info
        -   specific products in debt

-   **Purchases interface**
    -   Purchasing client selection
        -   Easy client creation just by entering name or 
            some basic data
        -   Client search
        -   Anonymous client option
    -   Product to sell
        1.   Multiple product selection
        2.   Selectable quantity
        3.   Optional custom price
    - Modifiable purchase metadata (ie date)
    
- **Inventory**
    - Product adding
        - Name, price and optional description/metadata
    -   Product managing
    
     -   Price & stock properties
         -   Optional metadata (ie expiration date)
             -   Independent batch metadata
    
         -   Price and stock change 
         -   Batch adding/discarding 

-   **Storage**
    -   All data will be stored on a .VSSM file (refered as the 
        archive)
        -   any configuration
        -   Each entry will be an inventory product, client 
            or configuration file, stored inside the archive
    -   Optional encryption (no guarantees)
    -   (optional) extra parity checks to ensure data 
        integrity
    -   all data will be saved in xml format, trying to 
        keep things simple

## Other information
 - [Discord](https://discord.gg/VJd6X7)