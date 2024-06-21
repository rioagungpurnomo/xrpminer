# XRPMiner
Free and multi-account XRP token mining.

| Feature | Support |
| ------- | :-------: |
| Random User Agent | ✅ |
| Proxy | ✅ |
| Multi-account | ✅ |

### Tutorial
#### STEP 1
Complete all the necessary materials and tools
1. [Download Termux](https://f-droid.org/id/packages/com.termux/)
2. [Create an Account Faucetearner](https://faucetearner.org/?r=816900323195)

#### STEP 2
Run the following command in Termux terminal
```bash
pkg update && pkg upgrade
pkg install git
pkg install python
git clone https://github.com/rioagungpurnomo/xrpminer
cd xrpminer
pip install -r requirements.txt
```

Then open your text editor or vim, then edit the accounts.json file and enter the email and account password you created previously.
You can add multiple accounts or just one, the following example
```json
[
  {
    "email": "account1@gmail.com",
    "password": "abdc"
  }
  {
    "email": "account2@gmail.com",
    "password": "abcde"
  }
  {
    "email": "account1@gmail.com",
    "password": "abcdef"
  }
]
```

#### STEP 3
then run the following command and let's mine
```bash
python xrpminer.py
```

### Donate
Your donation is a step for me to continue to grow and be enthusiastic about creating wild things.

XRP Address : rwWr7KUZ3ZFwzgaDGjKBysADByzxvohQ3C

### Support
Please send me a support ticket for progress on this tool.
Email : kangcryptoid@gmail.com