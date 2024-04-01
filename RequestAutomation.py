def solution(balances, requests):
    for i, request in enumerate(requests, start=1):
        req_type, *params = request.split()
        if req_type == "withdraw":
            account, amount = map(int, params)
            if account < 1 or account > len(balances) or balances[account - 1] < amount:
                return [-i]
            balances[account - 1] -= amount
        elif req_type == "deposit":
            account, amount = map(int, params)
            if account < 1 or account > len(balances):
                return [-i]
            balances[account - 1] += amount
        elif req_type == "transfer":
            from_account, to_account, amount = map(int, params)
            if (from_account < 1 or from_account > len(balances) or
                to_account < 1 or to_account > len(balances) or
                balances[from_account - 1] < amount):
                return [-i]
            balances[from_account - 1] -= amount
            balances[to_account - 1] += amount
    return balances
