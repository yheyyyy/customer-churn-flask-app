USE ai300_capstone;

SELECT *
from account
inner join account_usage
on account.account_id = account_usage.account_id
inner join customer
on customer.customer_id = account.customer_id
inner join city
on city.zip_code = customer.zip_code
inner join churn_status
on account.customer_id = churn_status.customer.id