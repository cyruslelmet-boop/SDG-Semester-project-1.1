# Ushuru Wangu - Fuel Tax Transparency Tool
# Strathmore University, ICS 1102 End of Semester Project
# Group Members: Cyrus Lelmet - 226606, Henry Olunga - 193987,
#                Johnson Ngala - 228086, Collins Mwangi - 213454,
#                Linda Chepchieng - 213976

import os
from datetime import datetime

# ==================================================
# EPRA FUEL PRICING & STATUTORY CONSTANTS (July 2026)
# ==================================================
RETAIL_PRICE = {
    "petrol": 214.03,   # Super Petrol retail price in KSh/litre (Nairobi)
    "diesel": 222.86    # Diesel retail price in KSh/litre (Nairobi)
}

# Unified EPRA rates combining flat and percentage-based CIF calculations
TAX_RATES = {
    "petrol": {
        # Flat rates (KES per litre)
        "excise_duty": 21.95,
        "road_maintenance_levy": 25.00,
        "petroleum_regulatory_levy": 0.75,
        "petroleum_development_levy": 5.40,

        # Percentage rates (calculated off Estimated CIF)
        "railway_development_levy_rate": 0.02,       # 2.0% of CIF
        "import_declaration_fee_rate": 0.035,        # 3.5% of CIF
        "merchant_shipping_levy_rate": 0.0005        # 0.05% of CIF
    },
    "diesel": {
        # Flat rates (KES per litre)
        "excise_duty": 11.37,
        "road_maintenance_levy": 25.00,
        "petroleum_regulatory_levy": 0.75,
        "petroleum_development_levy": 5.40,

        # Percentage rates (calculated off Estimated CIF)
        "railway_development_levy_rate": 0.02,       # 2.0% of CIF
        "import_declaration_fee_rate": 0.035,        # 3.5% of CIF
        "merchant_shipping_levy_rate": 0.0005        # 0.05% of CIF
    }
}

ESTIMATED_CIF = 120.00   # Estimated Cost, Insurance, and Freight base value (KES per litre)
VAT_RATE = 0.08          # 8% VAT (statutory fuel rate)

# Retail prices in local currency with current exchange rates to KES
COUNTRY_PRICES = {
    "Kenya": {
        "petrol_local": 214.03,
        "diesel_local": 222.86,
        "currency": "KSh",
        "rate_to_kes": 1.0
    },
    "Uganda": {
        "petrol_local": 6400.0,   # UGX
        "diesel_local": 6250.0,
        "currency": "UGX",
        "rate_to_kes": 0.0354     # 1 UGX ≈ KSh 0.0354
    },
    "Tanzania": {
        "petrol_local": 3990.0,   # TZS
        "diesel_local": 4182.0,
        "currency": "TZS",
        "rate_to_kes": 0.0493     # 1 TZS ≈ KSh 0.0493
    },
    "Rwanda": {
        "petrol_local": 2938.0,   # RWF
        "diesel_local": 2927.0,
        "currency": "RWF",
        "rate_to_kes": 0.0882     # 1 RWF ≈ KSh 0.0882
    },
    "Ghana": {
        "petrol_local": 13.40,    # GHS
        "diesel_local": 14.45,
        "currency": "GHS",
        "rate_to_kes": 11.32      # 1 GHS ≈ KSh 11.32
    }
}


# ==================================================
# CORE LOGIC MODULES
# ==================================================

def calculate_tax(fuel_type, litres):
    """Compute detailed tax breakdown for a fuel purchase (Branch 2)."""
    if fuel_type not in TAX_RATES:
        return None

    rates = TAX_RATES[fuel_type]
    breakdown = {}
    subtotal = 0.0
    cif_total = ESTIMATED_CIF * litres

    # Compute both flat rates and percentage-based CIF rates
    for levy, amount in rates.items():
        if levy.endswith("_rate"):
            tax = cif_total * amount
            display_name = levy.replace("_rate", "")
            breakdown[display_name] = tax
        else:
            tax = amount * litres
            breakdown[levy] = tax
        subtotal += tax

    # VAT is calculated as 8% of the final retail cost
    total_pump = RETAIL_PRICE[fuel_type] * litres
    vat = total_pump * VAT_RATE
    breakdown["vat"] = vat

    total_tax = subtotal + vat
    breakdown["total_tax"] = total_tax
    return breakdown


def display_receipt(breakdown, fuel_type, litres):
    """Print formatted tax receipt with structural clean names (Branch 3)."""
    pump_price = RETAIL_PRICE[fuel_type] * litres
    total_tax = breakdown["total_tax"]
    base_cost = pump_price - total_tax              # Actual cost without taxes
    base_cost_per_l = base_cost / litres             # Per litre price without taxes

    print("\n" + "=" * 50)
    print("       USHURU WANGU - OFFICIAL TAX RECEIPT")
    print("=" * 50)
    print(f"Fuel Type:        {fuel_type.capitalize()}")
    print(f"Litres Purchased: {litres:.2f} L")
    print(f"Retail Price/L:   KES {RETAIL_PRICE[fuel_type]:.2f}")
    print(f"Total Price Paid: KES {pump_price:,.2f}")
    print("-" * 50)

    # Dynamic generation of tax names while stripping structural underscores
    for levy, amount in breakdown.items():
        if levy == "total_tax":
            continue

        # Keep VAT formatted in uppercase, others in Title Case
        name = "VAT (8%)" if levy == "vat" else levy.replace("_", " ").title()
        print(f"  - {name:<30} KES {amount:>9,.2f}")

    print("-" * 50)
    print(f"{'TOTAL TAXES PAID':<32} KES {total_tax:>9,.2f}")
    print(f"{'NET ACTUAL FUEL VALUE':<32} KES {base_cost:>9,.2f}")
    print(f"{'Cost per Litre (No Tax)':<32} KES {base_cost_per_l:>9,.2f}")
    print("=" * 50)
    print(" * 'Net Actual Fuel Value' represents landed cost,")
    print("   oil marketer margins, and logistical handling.")
    print("=" * 50 + "\n")


def compare_with_neighbours(total_tax, fuel_type, litres):
    """Display cross-country pump price & tax comparison (Branch 3)."""
    effective_tax_per_l = total_tax / litres
    kenya_pump_price = RETAIL_PRICE[fuel_type]
    tax_percent = (effective_tax_per_l / kenya_pump_price) * 100

    print("-" * 50)
    print("            CROSS-COUNTRY COMPARISON")
    print("-" * 50)
    print(f"Fuel Type: {fuel_type.capitalize()}")
    print(f"{'Country':<12} {'Pump Price (KES/L)':<22} {'Your Tax/L (KES)':<15}")
    print("-" * 50)

    for country, data in COUNTRY_PRICES.items():
        local_price = data["petrol_local"] if fuel_type == "petrol" else data["diesel_local"]
        price_kes = local_price * data["rate_to_kes"]

        # Only display Kenya's localized tax contribution for comparison transparency
        if country == "Kenya":
            tax_display = f"KES {effective_tax_per_l:.2f}"
        else:
            tax_display = "—"

        print(f"{country:<12} KES {price_kes:<18.2f} {tax_display:<15}")

    print("-" * 50)
    print(f"Your effective tax per litre in Kenya: KES {effective_tax_per_l:.2f}")
    print(f"This accounts for {tax_percent:.1f}% of your pump price (KES {kenya_pump_price:.2f}/L).")
    print("Note: Tax rates in neighbouring countries are for benchmark comparisons.\n")


def save_receipt(breakdown, fuel_type, litres):
    """Append structural tax receipt records to file system (Branch 6)."""
    pump_price = RETAIL_PRICE[fuel_type] * litres
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = (f"{timestamp} | {fuel_type.capitalize()} | {litres:.2f} L | "
            f"Total Paid KES {pump_price:,.2f} | "
            f"Total Tax KES {breakdown['total_tax']:,.2f}\n")
    try:
        with open("tax_receipts.txt", "a") as f:
            f.write(line)
        print("[SYSTEM] Tax receipt safely logged in 'tax_receipts.txt'")
    except Exception as e:
        print(f"[ERROR] Failed to save receipt to disk: {e}")


def add_pothole_report():
    """Civic Infrastructure Reporting Utility supporting SDG 16 (Branch 4)."""
    print("\n" + "=" * 50)
    print("         CIVIC REPORT: POTHOLE & ROAD CONDITIONS")
    print("=" * 50)

    # Validate Location
    while True:
        location = input("Enter road or location name: ").strip()
        if not location:
            print("[ERROR] Location cannot be blank.")
            continue
        break

    # Validate Severity Scale
    while True:
        try:
            severity = int(input("Enter severity (1=Minor, 2=Moderate, 3=Severe): ").strip())
            if severity not in [1, 2, 3]:
                print("[ERROR] Severity ranking must be 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("[ERROR] Please input an integer (1, 2, or 3).")

    desc = input("Add a description/landmark (optional): ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    severity_labels = {1: "Minor", 2: "Moderate", 3: "Severe"}
    label = severity_labels[severity]

    # Structure report log
    report = f"{timestamp} | {location.upper()} | Severity: {severity} ({label})"
    if desc:
        report += f" | Details: {desc}"
    report += "\n"

    try:
        with open("pothole_reports.txt", "a") as f:
            f.write(report)
        print("\n[SUCCESS] Road report archived successfully in 'pothole_reports.txt'.")
        print("Thank you for fostering public civic accountability (SDG 16)!")
    except Exception as e:
        print(f"[ERROR] Failed to write report to disk: {e}")


# ==================================================
# MASTER CONTROLLER MENU
# ==================================================
def main():
    """The central routing loop of Ushuru Wangu (Branch 5)."""
    while True:
        print("\n" + "=" * 50)
        print("                 USHURU WANGU")
        print("=" * 50)
        print("1. Calculate my fuel tax receipt")
        print("2. Report a pothole / road condition")
        print("3. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\n--- Fuel Tax Calculator ---")

            # Fuel Type Loop
            while True:
                fuel = input("Fuel type (petrol/diesel): ").strip().lower()
                if fuel in TAX_RATES:
                    break
                print("[ERROR] Invalid fuel type. Please write 'petrol' or 'diesel'.")

            # Litres Loop
            while True:
                try:
                    litres = float(input("Litres purchased: ").strip())
                    if litres > 0:
                        break
                    print("[ERROR] Litres must be greater than zero.")
                except ValueError:
                    print("[ERROR] Please enter a valid number (e.g. 15.5).")

            # Execute Core Pipeline
            breakdown = calculate_tax(fuel, litres)
            if breakdown is None:
                print("[ERROR] Calculation failed.")
                continue

            display_receipt(breakdown, fuel, litres)
            save_receipt(breakdown, fuel, litres)
            compare_with_neighbours(breakdown["total_tax"], fuel, litres)

        elif choice == "2":
            add_pothole_report()

        elif choice == "3":
            print("\nAsante kwa kutumia Ushuru Wangu. Stay safe on the roads!\n")
            break

        else:
            print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()