# Regional tax burden database (as specified in your project outline)
NEIGHBOUR_TAX_BURDEN = {
    "Tanzania": 34.0,
    "Uganda": 36.5,
    "Rwanda": 39.0,
    "Ghana": 42.0
}

def display_receipt(fuel_type, litres, tax_data):
    """
    Formats the tax calculation dictionary into a readable console receipt
    and compares Kenya's tax burden regionally.
    """
    if not tax_data:
        print("[ERROR] No tax data available to display.")
        return

    # --- SECTION 1: CONSOLE RECEIPT LAYOUT ---
    print("\n==================================================")
    print("           USHURU WANGU - OFFICIAL TAX RECEIPT   ")
    print("==================================================")
    print(f"Fuel Type:      {fuel_type.capitalize()}")
    print(f"Volume Bought:  {litres:.2f} Litres")
    print("--------------------------------------------------")
    print("STATUTORY TAX & LEVY BREAKDOWN:")

    # Dynamically print flat levies
    print(f"  - Road Maintenance Levy:       KSh {tax_data.get('road_maintenance_levy', 0):.2f}")
    print(f"  - Excise Duty:                 KSh {tax_data.get('excise_duty', 0):.2f}")
    print(f"  - Petroleum Development Levy:  KSh {tax_data.get('petroleum_development_levy', 0):.2f}")
    print(f"  - Petroleum Regulatory Levy:   KSh {tax_data.get('petroleum_regulatory_levy', 0):.2f}")

    # Dynamically print percentage levies (using the cleaned names from your fixed loop)
    print(f"  - Railway Development Levy:    KSh {tax_data.get('railway_development_levy', 0):.2f}")
    print(f"  - Import Declaration Fee:      KSh {tax_data.get('import_declaration_fee', 0):.2f}")
    print(f"  - Merchant Shipping Levy:      KSh {tax_data.get('merchant_shipping_levy', 0):.2f}")

    print(f"  - Value Added Tax (VAT 8%):    KSh {tax_data.get('vat', 0):.2f}")
    print("--------------------------------------------------")
    print(f"TOTAL PRICE PAID AT PUMP:        KSh {tax_data.get('total_cost', 0):.2f}")
    print(f"TOTAL TAXES CONTRIBUTED:         KSh {tax_data.get('total_tax', 0):.2f}")
    print(f"YOUR PERSONAL TAX BURDEN:        {tax_data.get('tax_percentage', 0):.1f}%")
    print("==================================================\n")

    # --- SECTION 2: REGIONAL CONTEXT COMPARISON ---
    print("REGIONAL CONTEXT COMPARISON:")
    print(f"  * Kenya (Your Burden):  {tax_data.get('tax_percentage', 0):.1f}%")

    for country, rate in NEIGHBOUR_TAX_BURDEN.items():
        diff = tax_data['tax_percentage'] - rate
        if diff > 0:
            comparison_text = f"({diff:+.1f}% HIGHER than Kenya)"
        else:
            comparison_text = f"({abs(diff):.1f}% LOWER than Kenya)"
        print(f"  * {country}:               {rate:.1f}% {comparison_text}")
    print("==================================================\n")