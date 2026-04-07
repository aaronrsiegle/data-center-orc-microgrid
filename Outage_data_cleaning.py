# import commmands 
import pandas as pd 
import numpy as np

# import dataset 
outage_data = pd.read_csv('Z:\\Outage_data\\eaglei_outages_2025.csv')

# output data 
output_data = 'Z:\\Outage_data\\data-center-orc-microgrid'

# subset data for Loudoun county 
loudoun_data = outage_data[(outage_data['county'] == 'Loudoun') & (outage_data['state'] == 'Virginia')]

print(loudoun_data)

# customer compared to people 
loudoun_pop = 449749
va_customer_ratio = 3.4
loudoun_customer = loudoun_pop / va_customer_ratio 
loudoun_customer

# add outage threshold column 
outage_threshold = loudoun_customer * 0.001

# create new data frame to add to HOMER Pro
outage_indicator = pd.DataFrame({
    'outage_indicator': loudoun_data['customers_out'].apply(
        lambda x: 0 if x >= outage_threshold else 1
    )
})

print(outage_indicator) 
grid_out = outage_indicator['outage_indicator'] == 0
print(grid_out)

# save outputs directly to output_data path
loudoun_data.to_csv(os.path.join(output_data, 'loudoun_data.csv'), index=False)
outage_indicator.to_csv(os.path.join(output_data, 'outage_indicator.csv'), index=False)

print("Files saved to:", output_data)