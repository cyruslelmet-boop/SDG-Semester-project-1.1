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

- **Language:** Python 3 (no external libraries required)
- **Core Programming Concepts:** Variables, data types, conditional statements (`if/elif/else`), iterative structures (`while`, `for`), user-defined functions, parameter passing, string formatting, file input/output, exception handling, and dictionaries
- **Development Tools:** Visual Studio Code, Git, GitHub
- **Alignment with CSE 1213 / ICS 1102:** This project applies every major topic covered up to Week 10 of the Introduction to Computer Programming course, with a gentle introduction to file I/O and data structures from Week 12

---

## How to Run the Program

1. **Clone the repository**
   ```bash
   git clone https://github.com/cyruslelmet-boop/SDG-Semester-project-1.1.git