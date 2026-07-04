# Ushuru Wangu - Fuel Tax Transparency Tool
# Initial constants definition

# TAX RATES (all amounts in KES per litre, except VAT which is a decimal rate)
TAX_RATES = {
    "petrol": {
        "road_maintenance_levy": 25.0,
        "excise_duty": 21.95,
        "petroleum_development_levy": 0.40,
        "petroleum_regulatory_levy": 0.25,
        "vat_rate": 0.16          # 16%
    },
    "diesel": {
        "road_maintenance_levy": 25.0,
        "excise_duty": 11.37,
        "petroleum_development_levy": 0.40,
        "petroleum_regulatory_levy": 0.25,
        "vat_rate": 0.16
    }
}

# COMPARISON DATA (approximate total tax per litre for each country)
COUNTRY_COMPARISON = {
    "Kenya": 70.0,
    "Uganda": 55.0,
    "Tanzania": 50.0
}

# FILE NAMES (used for saving receipts and reports)
RECEIPTS_FILE = "tax_receipts.txt"
POTHOLE_REPORTS_FILE = "pothole_reports.txt"



# CORE FUNCTIONS
def calculate_tax(fuel_type, litres):
    """
    Computes a detailed tax breakdown for a fuel purchase.
    Returns a dictionary with each levy amount and the total tax.
    Returns None if the fuel type is invalid.
    """
    # Validate fuel type (Week 6: conditional structure)
    if fuel_type not in TAX_RATES:
        return None

    rates = TAX_RATES[fuel_type]
    breakdown = {}
    subtotal_before_vat = 0.0

    # Week 7/8: for-loop to iterate over each levy
    for levy_name, amount_per_litre in rates.items():
        if levy_name == "vat_rate":
            continue   # VAT handled separately
        tax_amount = amount_per_litre * litres
        breakdown[levy_name] = tax_amount
        subtotal_before_vat += tax_amount

    # Calculate VAT on the subtotal of all other levies
    vat = subtotal_before_vat * rates["vat_rate"]
    breakdown["vat"] = vat

    total_tax = subtotal_before_vat + vat
    breakdown["total_tax"] = total_tax
    return breakdown



# TEMPORARY TEST (remove or comment out after testing)
# if __name__ == "__main__":
    # Quick test
    result = calculate_tax("petrol", 20.0)
    if result:
        print("TAX BREAKDOWN FOR 20L PETROL:")
        for levy, amount in result.items():
            print(f"{levy}: KES {amount:.2f}")
    else:
        print("Invalid fuel type test failed.")