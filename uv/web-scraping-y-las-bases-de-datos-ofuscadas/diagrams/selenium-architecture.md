```mermaid
flowchart LR
    A[Driver API - 'Selenium']-->|Simplifica|B[Driver - 'Kernel' del browser]
    B-->|Se conecta con|C[Headless Browser]
    C-->|Puede ser|D[Chromium]
    C-->|Puede ser|E[Firefox Gecko]
```
