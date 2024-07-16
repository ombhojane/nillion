from nada_dsl import *

def nada_main():
    # Define parties involved
    manufacturer = Party(name="Manufacturer")
    distributor = Party(name="Distributor")
    retailer = Party(name="Retailer")
    auditor = Party(name="Auditor")

    # Define inputs
    production_time = SecretInteger(Input(name="production_time", party=manufacturer))
    production_cost = SecretInteger(Input(name="production_cost", party=manufacturer))
    
    transport_time = SecretInteger(Input(name="transport_time", party=distributor))
    transport_cost = SecretInteger(Input(name="transport_cost", party=distributor))
    
    shelf_time = SecretInteger(Input(name="shelf_time", party=retailer))
    retail_price = SecretInteger(Input(name="retail_price", party=retailer))

    # Calculate total times and costs
    total_time = production_time + transport_time + shelf_time
    total_cost = production_cost + transport_cost
    profit_margin = retail_price - total_cost

    # Output the results to the auditor
    outputs = [
        Output(total_time, "total_supply_chain_time", auditor),
        Output(total_cost, "total_supply_chain_cost", auditor),
        Output(profit_margin, "overall_profit_margin", auditor)
    ]

    return outputs
