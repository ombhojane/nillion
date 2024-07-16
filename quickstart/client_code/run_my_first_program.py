import os
from dotenv import load_dotenv
from py_nillion_client import (
    NillionClient,
    ComputeRequest,
    SecretInput,
    SecretInputType,
    StoreRequest,
)

# Load environment variables
load_dotenv("/root/.config/nillion/nillion-devnet.env")

# Set up the Nillion client
nillion_client = NillionClient(
    cluster_id=os.environ["NILLION_CLUSTER_ID"],
    bootnode_http_url=os.environ["NILLION_NILCHAIN_JSON_RPC"],
    bootnode_ws_url=os.environ["NILLION_BOOTNODE_WEBSOCKET"],
)

# Define the program path
program_path = "/content/nillion-python-starter/quickstart/nada_quickstart_programs/target/main.nada.bin"

# Store the program
with open(program_path, "rb") as f:
    program_binary = f.read()

store_request = StoreRequest(program_binary)
store_response = nillion_client.store_program(store_request)
program_id = store_response.program_id

print(f"Stored program_id: {program_id}")

# Define the parties
manufacturer = nillion_client.generate_party_id()
distributor = nillion_client.generate_party_id()
retailer = nillion_client.generate_party_id()
auditor = nillion_client.generate_party_id()

# Define the inputs
secret_inputs = [
    SecretInput("production_time", manufacturer, 100, SecretInputType.INT64),
    SecretInput("production_cost", manufacturer, 500, SecretInputType.INT64),
    SecretInput("transport_time", distributor, 50, SecretInputType.INT64),
    SecretInput("transport_cost", distributor, 200, SecretInputType.INT64),
    SecretInput("shelf_time", retailer, 200, SecretInputType.INT64),
    SecretInput("retail_price", retailer, 1000, SecretInputType.INT64),
]

# Create the compute request
compute_request = ComputeRequest(
    program_id=program_id,
    secret_inputs=secret_inputs,
)

# Run the computation
compute_response = nillion_client.compute(compute_request)
print(f"The computation was sent to the network. compute_id: {compute_response.compute_id}")

# Wait for the computation to complete
result = nillion_client.get_compute_result(compute_response.compute_id)
print(f"✅  Compute complete for compute_id {compute_response.compute_id}")
print(f"🖥️  The result is {result}")
