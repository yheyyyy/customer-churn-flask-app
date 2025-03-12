def format_model_inputs(dict):
    contract_type = int(dict['contract_type'])
    num_referrals = int(dict['num_referrals'])
    num_dependents = int(dict['num_dependents'])
    tenure_months = int(dict['tenure_months'])
    internet_type = int(dict['internet_type'])
    total_monthly_fee = float(dict['total_monthly_fee'])
    age = int(dict['age'])
    avg_gb_download_monthly = int(dict['avg_gb_download_monthly'])
    total_charges_quarter = float(dict['total_charges_quarter'])
    area_id = int(dict['area_id'])

    return [contract_type, num_referrals, num_dependents, tenure_months,
    internet_type,total_monthly_fee, age, avg_gb_download_monthly, 
    total_charges_quarter, area_id]


def validate(input_dict):
    errors = []
    
    required_fields= ['contract_type', 'num_referrals', 'num_dependents', 'tenure_months',
    'internet_type','total_monthly_fee', 'age', 'avg_gb_download_monthly', 
    'total_charges_quarter', 'area_id']

    for field in required_fields:

        if field not in input_dict:
            errors.append(f'{field} not found in request.')

        if field in ['tenure_months', 'age', 'avg_gb_download_monthly', 'area_id'] and type(input_dict[field]) != int \
                and not input_dict[field].isnumeric():
            errors.append(f'Field {field} must be int type.')

        elif field in ['total_monthly_fee', 'total_charges_quarter'] and type(input_dict[field]) != float:
            try:
                float(input_dict[field])
            except ValueError:
                errors.append(f'Field {field} must be numeric.')

    return errors
