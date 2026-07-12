#Starting by declaring the retail price per litre in Nairobi
RETAIL_PRICE={
    "petrol":214.03, 
    "diesel":222.86  
}

ESTIMATED_CIF=120.00 #Estimated landing cost per litre-This is an estimated value to simplify the tax calculation

#The levies as per EPRA(Energy and petroleum regulatory authority)
TAX_RATES = {
    "petrol": {
        #KSh per litre based levies:
        "excise_duty": 21.95,
        "road_maintenance_levy": 25.00,
        "petroleum_development_levy": 5.40,
        "petroleum_regulatory_levy": 0.75,

        # Percentage-based levies — calculated as percentage of CIF (landed cost)
        "railway_development_levy": 0.02,     # 2% of CIF 
        "import_declaration_fee": 0.035,       # 3.5% of CIF 
        "merchant_shipping_levy": 0.0005,      # 0.05% of CIF

        
    },
    "diesel": {
        #ksh per litre levies
        "excise_duty": 11.37,
        "road_maintenance_levy": 25.00,
        "petroleum_development_levy": 5.40,
        "petroleum_regulatory_levy": 0.75,

         #Percentage of CIF levies:
        "railway_development_levy": 0.02,
        "import_declaration_fee": 0.035,
        "merchant_shipping_levy": 0.0005,

        
    }
}


VAT_RATE=0.08 #as per april 2026

#the  function which computes tax
def calculate_tax(fuel_type,litres):
    if fuel_type not in TAX_RATES:
        return None
    
    rates=TAX_RATES[fuel_type]
    breakdown={}
    subtotal=0.0


    #Total estimated CIF value for this purchase
    cif_total=ESTIMATED_CIF*litres
    #calculate each levy
    for levy,amount in rates.items():
        #percentage based levies
        if levy.endswith("_rate"):
            tax=cif_total*amount
            #flat levies(kesh per litre)
        else:
            tax=amount*litres
        
        breakdown[levy]=tax
        subtotal+=tax


        
    #calculating VAT:
    total_pump=RETAIL_PRICE[fuel_type]*litres
    vat=total_pump*VAT_RATE
    breakdown["vat"]=vat

    #calculating total tax paid
    total_tax=vat+subtotal
    breakdown["total_tax"]=total_tax
    return breakdown


