# dataset for user profile
import pandas as pd
import numpy as np

def generate_simulated_user_profiles(num_users):
    genders = np.random.choice(['Male', 'Female', 'Other'], num_users)
    ages = np.random.randint(18, 60, num_users)
    indian_states = [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
        'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
        'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
        'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
        'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
    ]
    regions = np.random.choice(indian_states, num_users)
    pincodes = np.random.randint(100000, 999999, num_users)
    body_types = np.random.choice(['Slim', 'Average', 'Athletic', 'Curvy'], num_users)
    sizes = np.random.choice(['XS','S', 'M', 'L', 'XL','XXL'], num_users)  
    
    user_profile_data = {
        'UserID': np.arange(1, num_users + 1),
        'Gender': genders,
        'Age': ages,
        'Region': regions,
        'Pincode': pincodes,
        'BodyType': body_types,
        'SizeGenerallyBought': sizes
    }
    
    user_profile_df = pd.DataFrame(user_profile_data)
    return user_profile_df

def main():
    num_users = int(input("Number of simulated users: "))

    user_profile_df = generate_simulated_user_profiles(num_users)
    print("User Profile Data:")
    print(user_profile_df.head())

    
    csv_file_path = "user_profile.csv"
    user_profile_df.to_csv(csv_file_path, index=False, encoding='utf-8', )
    print(f" CSV file saved to {csv_file_path}")

if __name__ == "__main__":
    main()
