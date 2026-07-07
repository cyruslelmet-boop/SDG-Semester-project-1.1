# Ushuru Wangu - Fuel Tax Transparency Tool
# Strathmore University, ICS 1102 End of Semester Project
# Group Members: Cyrus Lelmet - 226606, Henry Olunga - 193987,
#                Johnson Ngala - 228086, Collins Mwangi - 213454,
#                Linda Chepchieng - 213976

import os
from datetime import datetime


# ============================
# TAX CONSTANTS
# ============================
TAX_RATES = {
    "petrol": {
        "road_maintenance_levy": 25.0,
        "excise_duty": 21.95,
        "petroleum_development_levy": 0.40,
        "petroleum_regulatory_levy": 0.25,
        "vat_rate": 0.16
    },
    "diesel": {
        "road_maintenance_levy": 25.0,
        "excise_duty": 11.37,
        "petroleum_development_levy": 0.40,
        "petroleum_regulatory_levy": 0.25,
        "vat_rate": 0.16
    }
}

COUNTRY_COMPARISON = {
    "Kenya": 70.0,
    "Uganda": 55.0,
    "Tanzania": 50.0,
    "Rwanda": 48.0,
    "Ghana": 45.0
}


# ============================
# CORE FUNCTIONS
# ============================
def calculate_tax(fuel_type, litres):
    """Compute detailed tax breakdown for a fuel purchase."""
    if fuel_type not in TAX_RATES:
        return None

    rates = TAX_RATES[fuel_type]
    breakdown = {}
    subtotal = 0.0

    for levy, amount in rates.items():
        if levy == "vat_rate":
            continue
        tax = amount * litres
        breakdown[levy] = tax
        subtotal += tax

    vat = subtotal * rates["vat_rate"]
    breakdown["vat"] = vat
    breakdown["total_tax"] = subtotal + vat
    return breakdown


def display_receipt(breakdown, fuel_type, litres):
    """Print a formatted tax receipt to the console."""
    print("\n" + "=" * 50)
    print("       USHURU WANGU - TAX RECEIPT")
    print("=" * 50)
    print(f"Fuel Type:      {fuel_type.capitalize()}")
    print(f"Litres Purchased: {litres:.2f} L")
    print("-" * 50)

    for levy, amount in breakdown.items():
        if levy != "total_tax":
            name = levy.replace("_", " ").title()
            print(f"{name:<30} KES {amount:>8.2f}")

    print("-" * 50)
    print(f"{'TOTAL TAX PAID':<30} KES {breakdown['total_tax']:>8.2f}")
    print("=" * 50 + "\n")


def compare_with_neighbours(total_tax, litres):
    """Display per-litre tax comparison with neighbouring countries."""
    effective = total_tax / litres
    print("--- Tax Comparison (per litre) ---")
    for country, rate in COUNTRY_COMPARISON.items():
        print(f"{country}: ~KES {rate:.2f}")
    print(f"Your effective tax per litre: KES {effective:.2f}\n")


def save_receipt(breakdown, fuel_type, litres):
    """Append the tax receipt to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (f"{timestamp} | {fuel_type} | {litres:.2f} L | "
            f"Total Tax KES {breakdown['total_tax']:.2f}\n")
    try:
        with open("tax_receipts.txt", "a") as f:
            f.write(line)
    except Exception as e:
        print(f"Error saving receipt: {e}")


def add_pothole_report():
    """Collect a pothole report from the user and save it to a file."""
    print("\n=== REPORT A POTHOLE ===")

    while True:
        location = input("Enter location: ").strip()
        if location == "":
            print("Location cannot be empty.")
            continue
        break

    while True:
        try:
            severity = int(input("Severity (1=small, 2=medium, 3=large): "))
            if severity < 1 or severity > 3:
                print("Must be 1-3.")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    desc = input("Brief description (optional): ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"{timestamp} | {location} | Severity {severity}"
    if desc:
        report += f" | {desc}"
    report += "\n"

    try:
        with open("pothole_reports.txt", "a") as f:
            f.write(report)
        print("Report saved. Asante!")
    except Exception as e:
        print(f"Error saving report: {e}")


# ============================
# MAIN MENU
# ============================
def main():
    while True:
        print("\n===== USHURU WANGU =====")
        print("1. Calculate my fuel tax receipt")
        print("2. Report a pothole / road condition")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            fuel = input("Fuel type (petrol/diesel): ").strip().lower()
            if fuel not in TAX_RATES:
                print("Invalid fuel type.")
                continue

            try:
                litres = float(input("Litres purchased: "))
                if litres <= 0:
                    print("Litres must be positive.")
                    continue
            except ValueError:
                print("Enter a valid number.")
                continue

            breakdown = calculate_tax(fuel, litres)
            if breakdown is None:
                print("Error computing tax.")
                continue

            display_receipt(breakdown, fuel, litres)
            save_receipt(breakdown, fuel, litres)
            compare_with_neighbours(breakdown["total_tax"], litres)

        elif choice == "2":
            add_pothole_report()

        elif choice == "3":
            print("Asante kwa kutumia Ushuru Wangu. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()