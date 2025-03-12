import joblib


class Model:
    def __init__(self):
        self.model = joblib.load('model/final1_catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)

'''#Churn example-
churn_example = {
    "contract_type": 1,
    "num_referrals": 3,
    "num_dependents": 0,
    "tenure_months": 3,
    "internet_type": 3,
    "total_monthly_fee": 83.90,
    "age": 75,
    "avg_gb_download_monthly": 11,
    "total_charges_quarter": 267.40,
    "area_id": 607
    }

model_inputs = list(churn_example.values())

print(model_inputs) 
print(Model().predict(model_inputs))'''


'''#Non-Churn example-
nonchurn_example = {
    "contract_type": 24,
    "num_referrals": 8,
    "num_dependents": 0,
    "tenure_months": 63,
    "internet_type": 3,
    "total_monthly_fee": 84.65,
    "age": 52,
    "avg_gb_download_monthly": 7,
    "total_charges_quarter": 5377.80,
    "area_id": 963
    }

model_inputs = list(nonchurn_example.values())

print(model_inputs) 
print(Model().predict(model_inputs))'''

