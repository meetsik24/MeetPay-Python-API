import requests

# Base URL for the MeetPay API
BASE_URL = 'https://api.meetpay.africa'

class MeetPaySender:
    def __init__(self, api_key):
        self.api_key = api_key  # Store user's unique API key
    
    # Create a transaction for a user
    def create_transaction(self, account_id, buyer_details, amount, webhook_url):
        try:
            buyer_name = buyer_details.get('buyer_name')
            buyer_phone = buyer_details.get('buyer_phone')
            buyer_email = buyer_details.get('buyer_email')
            
            # Ensure required fields are present
            if not all([buyer_name, buyer_phone, buyer_email, amount, account_id, webhook_url]):
                raise ValueError('Missing required transaction details.')
            
            # Payload to send
            data = {
                'buyer_name': buyer_name,
                'buyer_phone': buyer_phone,
                'buyer_email': buyer_email,
                'amount': amount,
                'account_id': account_id,
                'api_key': self.api_key,
                'webhook_url': webhook_url
            }
            
            # Make POST request to create transaction
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f'{BASE_URL}/transactions/create', 
                                   json=data,
                                   headers=headers)
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            print('Transaction created:', response.json())
            return response.json()  # Return API response
            
        except requests.exceptions.RequestException as error:
            print('Error creating transaction:', 
                  error.response.json() if hasattr(error, 'response') else str(error))
            return None