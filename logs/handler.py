def card_formatter(data) -> dict:
    """format the credit card data for stripe usage"""
    exp_date = data['exp_date']
    year = '20' + exp_date[-2:]
    month = exp_date[:2]
    if len(exp_date) == 3:
        month = exp_date[:1]
    return {'number': data['cc_num'], 'exp_month': month, 'exp_year': year, 'cvc': data['cvv']}
