from dotenv import load_dotenv
load_dotenv()

def get_aws_accounts():
    
    return [
        {
            'account_id': 'Account 900',
            'access_key': os.getenv('ACCESS_KEY'),
            'secret_key': os.getenv('SECRET_ACCESS_KEY'),
        },
        {
            'account_id': 'Account 106',
            'access_key': os.getenv('ACCESS_KEY2'),
            'secret_key': os.getenv('SECRET_ACCESS_KEY2'),
        },
        {
            'account_id': 'Account 5646',
            'access_key': os.getenv('ACCESS_KEY3'),
            'secret_key': os.getenv('SECRET_ACCESS_KEY3'),
        },
        {
            'account_id': 'Account 365',
            'access_key': os.getenv('ACCESS_KEY4'),
            'secret_key': os.getenv('SECRET_ACCESS_KEY4'),
        }
    ]