# Week 2 – Footprinting: GHDB & Maltego

**Cybersecurity Internship B084F · Networkwalks · Report W2-PM-FINAL**
Author: Karsten Krawutschke · 22 November 2026

> Educational lab work. Only publicly indexed sources and the domain assigned in the module task were used. No logins, no exploitation.

## 📄 Report

**[`report/W2-PM-FINAL-Report-PM2-PM3.pdf`](report/W2-PM-FINAL-Report-PM2-PM3.pdf)** – 6 pages, structured like the course sample report (disclaimer, introduction, tools, activities, risk analysis, recommendations, conclusion, evidence).

## 🧩 Modules

| Module | Topic | Result |
|---|---|---|
| **W2-PM1** | Footprinting with the Recon-Utilities | Used against networkwalks.com |
| **W2-PM2** | Footprinting with the Google Hacking Database (GHDB) | 10 exposed webcam pages + 10 public PDF listings, each with the dork used |
| **W2-PM3** | Footprinting with Maltego | `networkwalks.com` → e-mail `info@networkwalks.com`, MX host `mail.networkwalks.com` |

## 🔎 Method in short

**W2-PM2 – GHDB**
1. Open the GHDB on exploit-db.com and search for `cam`.
2. Copy dorks one by one into Google.
3. Open the results, check whether they are reachable, record link + dork.
4. Repeat with `filetype:pdf` / "index of" dorks for the ebook listings.

5. Start thinking... are there more useful combinations of params?

**W2-PM3 – Maltego** (Desktop 4.13.0)
1. Install and register, create a new graph.
2. Drag a *Domain* entity, rename it to `networkwalks.com`.
3. Run e-mail and DNS transforms (`To Email Addresses [PGP]`, `Search Web`, `To DNS Name – MX`).

## 📁 Structure

```
.
├── README.md
├── report/
│   ├── W2-PM-FINAL-Report-PM2-PM3.pdf   ← the deliverable
│   └── report.html                       ← PDF source
├── data/
│   ├── List_webcams.odt                  ← Task 1 table (source)
│   └── List_ebooks.odt                   ← Task 2 table (source)
├── evidence/
│   ├── maltego_graph.png                 ← Maltego result
│   └── kali_env.png                      ← lab environment (Kali, VirtualBox)
└── tools/                                ← rebuilds the PDF from data/
```

## 🔁 Rebuild the PDF

The tables in the report are read directly from the `.odt` files in `data/`.

```bash
./tools/build.sh      # needs python3 and chromium
```

## 🛡️ Key takeaways

- Exposed cameras and open directories are found with plain Google searches – the target is never contacted.
- Defenders can run the same dorks on their own domains to find leaks first.
- Contact addresses and mail servers are easy to map with Maltego and feed phishing and social engineering.

## ⚖️ Disclaimer

For education and research only. Unauthorised access to systems is illegal. Test only systems you own or have written permission for.
