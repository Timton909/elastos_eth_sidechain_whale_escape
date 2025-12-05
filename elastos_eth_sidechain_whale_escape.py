import requests, time

def elastos_escape():
    print("Elastos ETH Sidechain — Whale Escape (> $5M exiting to Ethereum mainnet)")
    seen = set()
    while True:
        # Elastos ETH Sidechain → Mainchain merge contract
        r = requests.get("https://api.elastos.io/eth/transactions?address=0x0000000000000000000000000000000000000000&limit=30")
        for tx in r.json().get("result", []):
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Official merge/withdraw to Ethereum mainnet
            if tx["to"].lower() != "0x6c17e4963a8046c2532c21c17d79b4c32f0a5d52": continue
            if "0x9d5e5d5e" not in tx.get("input", "")[:10]: continue  # withdraw selector

            value = int(tx["value"]) / 1e18
            if value >= 5_000_000:  # > $5M in ETH/ELA-bridged assets
                print(f"WHALE ESCAPE SUCCESSFUL\n"
                      f"${value:,.0f} leaving Elastos ETH sidechain → Ethereum L1\n"
                      f"Wallet: {tx['from']}\n"
                      f"Tx: https://esc.elastos.io/tx/{h}\n"
                      f"→ Someone just abandoned the 'SmartWeb' dream\n"
                      f"→ Real money fleeing the sidechain forever\n"
                      f"→ Usually final nail for dead projects on Elastos\n"
                      f"{'-'*85}")
        time.sleep(3.4)

if __name__ == "__main__":
    elastos_escape()
