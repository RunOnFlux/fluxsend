from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint
import json
import time

# set the inital variable names
payment_file = "flux-payment-example.json"
address_sending_from = "from_address"

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_user = "rpcuser"
rpc_pass = "rpcpassword"
rpc_host = "127.0.0.1" # if running locally then 127.0.0.1
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:16124", timeout=240)

def ask_yesno(question):
    ans = ""
    while True:
        ans = input(question + " [y/n] ")
        if ans == "y":
            return True
        elif ans == "n":
            return False 

# Load the json filen
f = open(payment_file)
data = json.load(f)

# Closing file
f.close()

amount_to_send = 0
final_data = {}
for i in data:
    # Skip zero amounts
    if (data[i] == 0):
        continue
    amount_to_send += data[i]

    final_data[i] = data[i]

print(f"Sending flux using: {payment_file}")
print(f"Sending flux from: {address_sending_from}")
print(f"Number of addresses: {len(final_data)}")

if (ask_yesno(f"Please confirm you are trying to send {amount_to_send} Flux")):

    # Using the sendmany variable so that fromaccount is used. All flux comes from it, and change is sent back to it
    ###"sendmany \"fromaccount\" {\"address\":amount,...}###
    txid = rpc_client.sendmany(address_sending_from, final_data)
    pprint(txid)
else:
    print("No Flux Was Sent")
