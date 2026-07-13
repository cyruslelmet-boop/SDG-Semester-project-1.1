# Ushuru Wangu - Fuel Tax Transparency Tool
# Strathmore University, ICS 1102 End of Semester Project
# Group Members: Cyrus Lelmet - 226606, Henry Olunga - 193987,
#                Johnson Ngala - 228086, Collins Mwangi - 213454,
#                Linda Chepchieng - 213976

import os
from datetime import datetime


RECEIPTS_FILE = "tax_receipts.txt"


# ============================
# EPRA FUEL PRICING CONSTANTS (June–July 2026)
# ============================
RETAIL_PRICE = {
    "petrol": 214.03,   # Super Petrol retail price in KSh/litre (Nairobi)
    "diesel": 222.86    # Diesel retail price in KSh/litre (Nairobi)
}

# Individual per-litre taxes/levies (EPRA schedule)
TAX_RATES = {
    "petrol": {
        "excise_duty": 21.95,
        "road_maintenance_levy": 25.00,
        "railway_development_levy": 2.05,
        "import_declaration_fee": 2.56,
        "petroleum_regulatory_levy": 0.75,
        "merchant_shipping_levy": 0.03
    },
    "diesel": {
        "excise_duty": 11.37,
        "road_maintenance_levy": 25.00,
        "railway_development_levy": 2.58,
        "import_declaration_fee": 3.22,
        "petroleum_regulatory_levy": 0.75,
        "merchant_shipping_levy": 0.03
    }
}

VAT_RATE = 0.08  # 8% VAT (reduced from 16% in April 2026)

# Retail prices in local currency per litre, with exchange rates to KES (July 2026)
# Sources: EPRA, UNOC, EWURA, RURA, NPA
COUNTRY_PRICES = {
    "Kenya": {
        "petrol_local": 214.03,
        "diesel_local": 222.86,
        "currency": "KSh",
        "rate_to_kes": 1.0
    },
    "Uganda": {
        "petrol_local": 6400.0,   # UGX (mid-range)
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
        "petrol_local": 13.40,    # GHS (mid-range)
        "diesel_local": 14.45,
        "currency": "GHS",
        "rate_to_kes": 11.32      # 1 GHS ≈ KSh 11.32
    }
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

    # Sum all fixed levies
    for levy, amount in rates.items():
        tax = amount * litres
        breakdown[levy] = tax
        subtotal += tax

    # VAT is 8% of the final pump price
    total_pump = RETAIL_PRICE[fuel_type] * litres
    vat = total_pump * VAT_RATE
    breakdown["vat"] = vat

    total_tax = subtotal + vat
    breakdown["total_tax"] = total_tax
    return breakdown


def display_receipt(breakdown, fuel_type, litres):
    """Print a formatted tax receipt with full cost breakdown."""
    pump_price = RETAIL_PRICE[fuel_type] * litres
    total_tax = breakdown["total_tax"]
    base_cost = pump_price - total_tax              # total cost without taxes
    base_cost_per_l = base_cost / litres             # per litre without taxes

    print("\n" + "=" * 50)
    print("       USHURU WANGU - TAX RECEIPT")
    print("=" * 50)
    print(f"Fuel Type:      {fuel_type.capitalize()}")
    print(f"Litres Purchased: {litres:.2f} L")
    print(f"Retail Price/L:  KES {RETAIL_PRICE[fuel_type]:.2f}")
    print(f"Total Price Paid: KES {pump_price:,.2f}")
    print("-" * 50)

    # Individual tax lines
    for levy, amount in breakdown.items():
        if levy == "total_tax":
            continue
        name = levy.replace("_", " ").title()
        print(f"{name:<30} KES {amount:>8,.2f}")

    print("-" * 50)
    print(f"{'TOTAL TAXES':<30} KES {total_tax:>8,.2f}")
    print(f"{'COST OF FUEL ONLY':<30} KES {base_cost:>8,.2f}")
    print(f"{'Cost/L (No Tax)':<30} KES {base_cost_per_l:>8,.2f}")
    print("=" * 50)
    print("  * 'Cost of Fuel Only' = landed cost + margins +")
    print("    variable levies (e.g. PDL). This is what")
    print("    the fuel would cost without the taxes above.")
    print("=" * 50 + "\n")


def compare_with_neighbours(total_tax, fuel_type, litres):
    """Display a cross-country pump price and tax comparison."""
    effective_tax_per_l = total_tax / litres
    kenya_pump_price = RETAIL_PRICE[fuel_type]
    tax_percent = (effective_tax_per_l / kenya_pump_price) * 100

    print("\n--- Cross-Country Comparison ---")
    print(f"Fuel Type: {fuel_type.capitalize()}")
    print(f"{'Country':<12} {'Pump Price (KES/L)':<20} {'Your Tax/L':<15}")
    print("-" * 50)

    for country, data in COUNTRY_PRICES.items():
        local_price = data["petrol_local"] if fuel_type == "petrol" else data["diesel_local"]
        price_kes = local_price * data["rate_to_kes"]

        if country == "Kenya":
            tax_display = f"KES {effective_tax_per_l:.2f}"
        else:
            tax_display = "—"

        print(f"{country:<12} KES {price_kes:<18.2f} {tax_display:<15}")

    print("-" * 50)
    print(f"Your effective tax per litre: KES {effective_tax_per_l:.2f}")
    print(f"That's {tax_percent:.1f}% of your pump price (KES {kenya_pump_price:.2f}/L).")
    print("Note: Tax breakdowns for other countries are not shown.\n")


def _ensure_receipts_file(file_path=RECEIPTS_FILE):
    """Create the receipts file with a header if it does not already exist."""
    if os.path.exists(file_path):
        return

    with open(file_path, "w") as f:
        f.write("# USHURU WANGU RECEIPTS\n")
        f.write("# Format: ReceiptID | Timestamp | Fuel | Litres | Price/L | Total Paid | Total Tax\n")


def _next_receipt_id(file_path=RECEIPTS_FILE):
    """Generate a sequential receipt id based on existing saved receipts."""
    _ensure_receipts_file(file_path)
    serial = 1

    try:
        with open(file_path, "r") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned and not cleaned.startswith("#"):
                    serial += 1
    except Exception:
        return "RCPT-000001"

    return f"RCPT-{serial:06d}"


def _build_receipt_record(breakdown, fuel_type, litres):
    """Build a structured receipt record for display and file storage."""
    pump_price = RETAIL_PRICE[fuel_type] * litres
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt_id = _next_receipt_id()

    return {
        "receipt_id": receipt_id,
        "timestamp": timestamp,
        "fuel_type": fuel_type.capitalize(),
        "litres": litres,
        "price_per_litre": RETAIL_PRICE[fuel_type],
        "total_paid": pump_price,
        "total_tax": breakdown["total_tax"]
    }


def save_receipt(breakdown, fuel_type, litres):
    """Append the tax receipt to a text file and return the saved record."""
    _ensure_receipts_file()
    record = _build_receipt_record(breakdown, fuel_type, litres)
    line = (
        f"{record['receipt_id']} | {record['timestamp']} | {record['fuel_type']} | "
        f"{record['litres']:.2f} L | KES {record['price_per_litre']:.2f}/L | "
        f"Total Paid KES {record['total_paid']:,.2f} | "
        f"Total Tax KES {record['total_tax']:,.2f}\n"
    )

    try:
        with open(RECEIPTS_FILE, "a") as f:
            f.write(line)
        return record
    except Exception as e:
        print(f"Error saving receipt: {e}")
        return None


def view_saved_receipts(limit=5):
    """Display the latest saved tax receipts from file."""
    if not os.path.exists(RECEIPTS_FILE):
        print("No receipts found yet. Generate a receipt first.")
        return

    try:
        with open(RECEIPTS_FILE, "r") as f:
            rows = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except Exception as e:
        print(f"Error reading receipts: {e}")
        return

    if not rows:
        print("No receipts found yet. Generate a receipt first.")
        return

    print("\n--- Latest Tax Receipts ---")
    for row in rows[-limit:]:
        print(row)
    print("-" * 50)


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
        print("2. View saved tax receipts")
        print("3. Report a pothole / road condition")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

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
            saved_receipt = save_receipt(breakdown, fuel, litres)
            if saved_receipt:
                print(
                    f"Receipt saved: {saved_receipt['receipt_id']} "
                    f"at {saved_receipt['timestamp']}"
                )
            compare_with_neighbours(breakdown["total_tax"], fuel, litres)

        elif choice == "2":
            view_saved_receipts()

        elif choice == "3":
            add_pothole_report()

        elif choice == "4":
            print("Asante kwa kutumia Ushuru Wangu. Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()