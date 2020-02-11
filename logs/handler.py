def handle_card_format(data) -> dict:
    """format the credit card data for stripe usage"""
    exp_date = data['exp_date']
    year = '20' + exp_date[-2:]
    month = exp_date[:2]
    if len(exp_date) == 3:
        month = exp_date[:1]
    return {'number': data['cc_num'], 'exp_month': month, 'exp_year': year, 'cvc': data['cvv']}


def handle_masking(item, cvv=False):
    """Return the masked credit card and cvc values(ex: ********1234, ***)"""
    return ("*" * len(item)) if cvv else "*" * (len(item) - 4) + item[-4:]
