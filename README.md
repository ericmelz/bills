# bills
Automation for downloading bills.

See `Wells Fargo.ipynb` for an example.

Installation:
```
git clone git@github.com:ericmelz/bills.git
cd bills
python3 -m venv venv
. /venv/bin/activate
pip install -r requirements.txt

```

`secrets.py`
download_dir='</Path/to/statements/directory/>'
wellsfargo_user='<user name>'
wellsfargo_password='<password>'
wellsfargo_accounts = [
    '<account name 1>',
    '<account name 2>',
]

