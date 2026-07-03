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