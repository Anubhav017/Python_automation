import requests


class Request:
    @staticmethod
    def make_request(subscription_id, environment='dev'):
        # Define the base URL for each environment
        base_urls = {
            'dev': f'https://dev-api.pictorycontent.com/customer-management/api/v2/customers/subscriptions',
        }

        # Select the appropriate base URL based on the environment
        base_url = base_urls.get(environment, base_urls['dev'])

        # Construct the full URI using the selected base URL
        uri = f"{base_url}/{subscription_id}/revert"

        # Make the POST request
        response = requests.post(uri, data=None)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print('POST request successful')
            print('Response:')
            print(response.json())  # Print the response data in JSON format
        else:
            print('POST request failed')
            print('Status code:', response.status_code)
            print('Response:')
            print(response.text)  # Print the response text

