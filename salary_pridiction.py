from sklearn.linear_model import LinearRegression

import pandas as pd

df = pd.read_csv('/Users/onkar/Documents/GEN-AI/emp_salary.csv')

x = df[['experience', 'location']]
y = df['salary']

# convert location into numerical value

x = pd.get_dummies(x , columns=['location'], dtype=int)

model = LinearRegression()
model.fit(x, y)

new_employee = pd.DataFrame({'experience': [5], 'location': ['Pune']})

new_employee = pd.get_dummies(new_employee, columns=['location'], dtype=int)

new_employee = new_employee.reindex(columns=x.columns, fill_value=0)

response = model.predict(new_employee)
print(response)
#print(f'Predicted Salary: ₹{response[0]:,.2f}')