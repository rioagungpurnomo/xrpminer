![XRPMiner](https://github.com/rioagungpurnomo/xrpminer/assets/161745412/25590a2d-3143-45cb-897b-9b351b9ae873)

# XRPMiner
Free and multi-account XRP token mining.

| Feature | Support |
| ------- | :-------: |
| Random User Agent | ✅ |
| Proxy | ✅ |
| Multi-account | ✅ |
| Auto Withdrawal | ✅ |

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
  },
  {
    "email": "account2@gmail.com",
    "password": "abcde"
  },
  {
    "email": "account1@gmail.com",
    "password": "abcdef"
  }
]
```

#### STEP 3
Next, edit the contents of the wallet.json file and enter the XRP wallet address and Destination Tag. You can activate and deactivate automatic withdrawals by changing the auto key to false, Automatic withdrawals every time your balance reaches 1 XRP or more will be sent directly to your XRP wallet address.
```json
{
  "auto": true,
  "address": "",
  "destination_tag": ""
}
```

#### STEP 4
Then run the following command and start automatic mining
```bash
python xrpminer.py
```

### Donate
Your donation is a step for me to continue to grow and be enthusiastic about creating wild things.

XRP Address : rwWr7KUZ3ZFwzgaDGjKBysADByzxvohQ3C

Destination Tag : 6691170

### Support
Please send me a support ticket for progress on this tool.
Email : kangcryptoid@gmail.com
