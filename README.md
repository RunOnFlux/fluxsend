# FluxSend Python Script (Requires Fullnode Fluxd Running)

## Prerequisites
**Python 3 is required** https://www.python.org/downloads/

```python
pip install python-bitcoinrpc
```
## Create payment file use flux-payment-example.json as an example
```json
{ 
    "t1eVqdfpJQynSzPGNCqSmUkeA1H5WCJYyir": 25621,
    "address": 0
}
```

## Updating the Script with your from address and the file you just created
### Inside sendflux.py

  ```python
  payment_file = "flux-payment-example.json"
  ```

  ```python
  address_sending_from = "from_address"
  ```

## Run the script
  ```bash
  ./sendflux.py
  ```
  or 

  ```python3 sendflux.py```
