#final code for browsing data dataset
import pandas as pd
import numpy as np

def generate_simulated_browsing_data(num_users, entries_per_user):
    num_browsing_entries = num_users * entries_per_user
    
    browsing_dates = pd.date_range(start="2021-01-01", periods=num_browsing_entries, freq="H")
    user_ids = np.repeat(np.arange(1, num_users + 1), entries_per_user)
    
    browsing_pages = np.random.choice(['Clothing', 'Shoes', 'Accessories', 'Sale', 'Homepage'], num_browsing_entries, p=[0.4, 0.3, 0.2, 0.05, 0.05])
    time_spent_seconds = np.random.randint(5, 600, num_browsing_entries)  
    devices = np.random.choice(['Desktop', 'Mobile', 'Tablet'], num_browsing_entries, p=[0.5, 0.4, 0.1])
    visit_frequencies = np.random.randint(1, 20, num_browsing_entries) 
    
    subcategories = {
        'Shirts': ['Casual Shirt', 'Formal Shirt', 'Printed Shirt', 'Striped Shirt', 'Graphic Shirt'],
        'Dresses': ['Summer Dress', 'Evening Dress', 'Cocktail Dress', 'Maxi Dress', 'Wrap Dress'],
        'Jeans': ['Skinny Jeans', 'Straight Jeans', 'Bootcut Jeans', 'Distressed Jeans', 'High-rise Jeans'],
        'Jackets': ['Winter Jacket', 'Leather Jacket', 'Denim Jacket', 'Bomber Jacket', 'Puffer Jacket'],
        'Sneakers': ['Running Sneakers', 'Casual Sneakers', 'High-top Sneakers', 'Platform Sneakers', 'Slip-on Sneakers'],
        'Boots': ['Ankle Boots', 'Knee-high Boots', 'Hiking Boots', 'Chelsea Boots', 'Combat Boots'],
        'Sandals': ['Flat Sandals', 'Wedge Sandals', 'Platform Sandals', 'Slide Sandals', 'Gladiator Sandals'],
        'Heels': ['Stiletto Heels', 'Block Heels', 'Wedge Heels', 'Platform Heels', 'Ankle-strap Heels'],
        'Bags': ['Tote Bag', 'Crossbody Bag', 'Backpack', 'Clutch Bag', 'Satchel Bag'],
        'Hats': ['Fedora Hat', 'Beanie Hat', 'Wide Brim Hat', 'Bucket Hat', 'Baseball Cap'],
        'Scarves': ['Knit Scarf', 'Silk Scarf', 'Infinity Scarf', 'Printed Scarf', 'Fringe Scarf'],
        'Jewelry': ['Necklace', 'Earrings', 'Bracelet', 'Ring', 'Anklet'],
        'Sunglasses': ['Aviator Sunglasses', 'Round Sunglasses', 'Cat-eye Sunglasses', 'Square Sunglasses', 'Oversized Sunglasses'],
        'Watches': ['Analog Watch', 'Digital Watch', 'Smart Watch', 'Dress Watch', 'Sports Watch'],
        'Makeup': ['Foundation', 'Concealer', 'Blush', 'Eyeshadow', 'Mascara'],
        'Skincare': ['Moisturizer', 'Cleanser', 'Face Mask', 'Serum', 'Eye Cream'],
        # Male categories
        'T-Shirts': ['Plain T-Shirt', 'Graphic T-Shirt', 'V-Neck T-Shirt', 'Striped T-Shirt', 'Pocket T-Shirt'],
        'Pants': ['Chinos', 'Jeans', 'Cargo Pants', 'Track Pants', 'Dress Pants'],
        'Suits': ['Single-Breasted Suit', 'Double-Breasted Suit', 'Tuxedo', 'Business Suit', 'Casual Suit'],
        'Jackets': ['Blazer', 'Bomber Jacket', 'Leather Jacket', 'Windbreaker', 'Denim Jacket'],
        'Sneakers': ['Classic Sneakers', 'High-Top Sneakers', 'Running Shoes', 'Skate Shoes', 'Canvas Sneakers'],
        'Accessories': ['Necktie', 'Bowtie', 'Pocket Square', 'Cufflinks', 'Belt'],
        'Hats': ['Baseball Cap', 'Beanie', 'Fedora', 'Bucket Hat', 'Trucker Hat'],
        'Swimwear': ['Board Shorts', 'Swim Trunks', 'Rash Guard', 'Swim Briefs', 'Swim Shirt'],
        'Shorts': ['Cargo Shorts', 'Chino Shorts', 'Athletic Shorts', 'Bermuda Shorts', 'Denim Shorts'],
        'Hoodies': ['Pullover Hoodie', 'Zip-Up Hoodie', 'Fleece Hoodie', 'Graphic Hoodie', 'Athletic Hoodie'],
        'Sweaters': ['Crewneck Sweater', 'V-Neck Sweater', 'Cardigan', 'Cable Knit Sweater', 'Turtleneck Sweater'],
        'Ties': ['Silk Tie', 'Knit Tie', 'Bowtie', 'Skinny Tie', 'Woven Tie'],
        'Watches': ['Dress Watch', 'Sports Watch', 'Chronograph Watch', 'Automatic Watch', 'Military Watch'],
        # Unisex categories
        'Backpacks': ['Travel Backpack', 'Hiking Backpack', 'Canvas Backpack', 'Laptop Backpack', 'Daypack'],
        'Sunglasses': ['Aviator Sunglasses', 'Round Sunglasses', 'Cat-Eye Sunglasses', 'Wayfarer Sunglasses', 'Square Sunglasses'],
        'Watches': ['Analog Watch', 'Digital Watch', 'Smart Watch', 'Dress Watch', 'Sports Watch'],
        'Hats': ['Baseball Cap', 'Beanie', 'Bucket Hat', 'Wide Brim Hat', 'Trucker Hat'],
        'Scarves': ['Knit Scarf', 'Silk Scarf', 'Infinity Scarf', 'Plaid Scarf', 'Fringe Scarf'],
        'Jewelry': ['Necklace', 'Earrings', 'Bracelet', 'Ring', 'Anklet'],
        'Ties': ['Silk Tie', 'Knit Tie', 'Bowtie', 'Skinny Tie', 'Woven Tie'],
        'Gloves': ['Leather Gloves', 'Knit Gloves', 'Touchscreen Gloves', 'Driving Gloves', 'Wool Gloves'],
        'Belts': ['Leather Belt', 'Canvas Belt', 'Braided Belt', 'Webbed Belt', 'Studded Belt'],
    }
    
    product_categories_list = ['Clothing', 'Shoes', 'Accessories', 'Beauty', 'Sale']
    product_subcategories_list = [sub for sub in subcategories.keys()]
    product_categories = np.random.choice(product_categories_list, size=num_browsing_entries)
    product_subcategories = np.random.choice(product_subcategories_list, size=num_browsing_entries)
    
    product_descriptions = []
    for subcategory in product_subcategories:
        subcategory_descriptions = subcategories[subcategory]
        description = np.random.choice(subcategory_descriptions)
        product_descriptions.append(f" {description}")
    
    browsing_data = {
        'UserID': user_ids,
        'Date': browsing_dates,
        'TimeSpentSeconds': time_spent_seconds,
        'Device': devices,
        'VisitFrequency': visit_frequencies,
        'ProductType': product_subcategories,
        'ProductDescription': product_descriptions
    }
    
    browsing_df = pd.DataFrame(browsing_data)

    return browsing_df

def main():
    num_users = int(input("Number of simulated users: "))
    entries_per_user = int(input("Number of entries per user: "))

    browsing_df = generate_simulated_browsing_data(num_users, entries_per_user)

    #csv_file_path = "browsing_history.csv"
    #browsing_df.to_csv(csv_file_path, index=False, encoding='utf-8',date_format='%Y-%m-%d %H:%M:%S')
    #print(f"CSV file saved to {csv_file_path}")

if __name__ == "__main__":
    main()
