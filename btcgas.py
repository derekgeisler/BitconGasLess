from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction
from bitcoinlib.services.services import Service

def create_and_send_transaction(sender_wallet_name, recipient_address, amount, sponsor_key):
    # Load sender wallet
    sender_wallet = Wallet(sender_wallet_name)
    
    # Create a new transaction
    tx = Transaction()
    
    # Add input from sender's wallet
    tx.add_input(sender_wallet.get_key().address, amount=amount + 0.0001)  # Assuming 0.0001 BTC as fee
    
    # Add output to recipient
    tx.add_output(recipient_address, amount)
    
    # Sign the transaction with sender's private key
    sender_key = sender_wallet.get_key().key
    tx.sign(sender_key)
    
    # Broadcast the transaction using the sponsor's key to pay the fee
    sponsor_service = Service('http://localhost:8332')  # Connect to your Bitcoin Core node
    tx_hex = tx.as_hex()
    response = sponsor_service.sendrawtransaction(tx_hex)
    
    return response

def main():
    sender_wallet_name = 'SenderWallet'
    recipient_address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'  # Example recipient address
    amount = 0.0005  # Amount to send
    
    # Sponsor's private key (for demonstration; in production, handle securely)
    sponsor_key = 'cN3HXGpL5dHZoCR9Et5LkS1r5N5eYcmyC5oY9RavscD4xezTV7zQ'  # Example private key

    tx_id = create_and_send_transaction(sender_wallet_name, recipient_address, amount, sponsor_key)
    print(f"Transaction ID: {tx_id}")

if __name__ == "__main__":
    main()
