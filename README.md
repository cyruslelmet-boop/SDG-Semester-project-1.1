# Ushuru Wangu (My Tax) – Fuel Tax Transparency Tool

**Ushuru Wangu** is a console-based Python application that gives Kenyan citizens a clear, personalised breakdown of the taxes embedded in every litre of fuel they buy. It also lets them report potholes and poor road conditions, bridging the gap between tax payment and road accountability.

---

## SDG Alignment

This project directly supports **SDG 16: Peace, Justice and Strong Institutions**, especially:
- **Target 16.6** – Develop effective, accountable and transparent institutions.
- **Target 16.5** – Substantially reduce corruption and bribery.

It also contributes to **SDG 9.1** (Quality, reliable, sustainable infrastructure) as a secondary goal.

---

## Problem Statement

Over 40% of the pump price of fuel in Kenya consists of government taxes and levies: the Road Maintenance Levy (KES 25/L), Excise Duty, VAT, and several smaller charges. These funds are meant to build and maintain roads, yet opaque financial management, securitisation of future levies, and reported misappropriation mean ordinary citizens rarely see a direct link between the taxes they pay and the quality of roads in their neighbourhoods. No simple, accessible tool exists to show a citizen exactly how much tax they contribute or to let them report local infrastructure failures.

---

## Our Solution

Ushuru Wangu provides two core functions through a simple text menu:

1. **Tax Receipt Calculator**
   - Select fuel type (petrol or diesel) and enter the number of litres purchased.
   - Instantly see a detailed breakdown of every levy: Road Maintenance Levy, Excise Duty, Petroleum Development Levy, Petroleum Regulatory Levy, VAT, and the total tax paid.
   - Compare Kenya’s effective fuel tax rate with approximate rates in Uganda and Tanzania.
   - Automatically save the receipt to a local file for future reference.

2. **Community Road Reporter**
   - Report a pothole by entering a location name and a severity rating from 1 (small) to 3 (large).
   - Add an optional brief description.
   - All reports are timestamped and stored in a plain text file, creating a permanent record that citizens can use to demand action from their leaders.

The application runs **completely offline**, requires no internet connection, and stores all data on the user's own computer.

---

## Technologies and Concepts Used

- **Language:** Python3 (no external libraries required)
- **Core Programming Concepts:** Variables, data types, conditional statements (`if/elif/else`), iterative structures (`while`, `for`), user-defined functions, parameter passing, string formatting, file input/output, exception handling, and dictionaries
- **Development Tools:** Visual Studio Code, Git, GitHub
- **Alignment with CSE 1213 / ICS 1102:** This project applies every major topic covered up to Week 10 of the Introduction to Computer Programming course, with a gentle introduction to file I/O and data structures from Week 12

---

## How to Run the Program

1. **Clone the repository**
   ```bash
   git clone https://github.com/cyruslelmet-boop/SDG-Semester-project-1.1.git

2.**Run the Script**
   Make sure python 3 is installed in your system.No extra libraries are needed.

   bash
   python3 ushuru_wangu.py

3.**Use the Menu**
  Option 1-Calculate a fuel tax receipt
  Option 2-Report a pothole/road condition
  Option 3-Exit

  The program creates two text files in the same folder :
   tax_receipts.txt-stores all generated receipts.
   pothole_reports.txt-stores all submitted road reports.

**FILE STRUCTURE**

  ushuru-wangu/
│
├── ushuru_wangu.py          # Main application (all source code)
├── tax_receipts.txt          # Saved receipts (auto-generated on first use)
├── pothole_reports.txt       # Saved road reports (auto-generated on first use)
└── README.md                 # This file

**EXAMPLE USAGE**

  Tax receipt Calculation

   ===== USHURU WANGU =====
1. Calculate my fuel tax receipt
2. Report a pothole / road condition
3. Exit
Enter your choice (1-3): 1
Fuel type (petrol/diesel): petrol
Litres purchased: 20

==================================================
       USHURU WANGU - TAX RECEIPT
==================================================
Fuel Type:      Petrol
Litres Purchased: 20.00 L
--------------------------------------------------
Road Maintenance Levy           KES   500.00
Excise Duty                     KES   439.00
Petroleum Development Levy      KES     8.00
Petroleum Regulatory Levy       KES     5.00
Vat                             KES   152.32
--------------------------------------------------
TOTAL TAX PAID                  KES  1104.32
==================================================

--- Tax Comparison (per litre) ---
Kenya: ~KES 70.00
Uganda: ~KES 55.00
Tanzania: ~KES 50.00
Your effective tax per litre: KES 55.22


Pothole Reporting

===== USHURU WANGU =====
1. Calculate my fuel tax receipt
2. Report a pothole / road condition
3. Exit
Enter your choice (1-3): 2

=== REPORT A POTHOLE ===
Enter location: Moi Avenue, near Hilton
Severity (1=small, 2=medium, 3=large): 3
Brief description (optional): Deep hole, damaged two tyres yesterday
Report saved. Asante!


**CONTRIBUTORS**
NAME               GITHUB USERNAME           ROLE
cyruslelmet 
