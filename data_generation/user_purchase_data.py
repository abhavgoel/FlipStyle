import pandas as pd
import numpy as np

def generate_simulated_purchase_data(num_users, purchases_per_user):
    total_purchases = num_users * purchases_per_user

    purchase_dates = pd.date_range(start="2021-01-01", periods=total_purchases, freq="D")
    purchase_amounts = np.random.uniform(10, 500, total_purchases)
    payment_modes = np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash'], total_purchases)
    sale_status = np.random.choice([True, False], total_purchases, p=[0.2, 0.8])

    user_ids = np.repeat(np.arange(1, num_users + 1), purchases_per_user)
    
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

    items_purchased = []
    for _ in range(total_purchases):
        subcategory = np.random.choice(list(subcategories.keys()))
        item = np.random.choice(subcategories[subcategory])
        items_purchased.append(item)

    order_numbers = np.arange(1, total_purchases + 1)
    shipping_addresses = ['City' + str(i) for i in range(1, total_purchases + 1)]
    discount_amounts = np.random.uniform(0, 50, total_purchases)
    return_statuses = np.random.choice(['Returned', 'Not Returned'], total_purchases, p=[0.1, 0.9])
    return_reasons = np.where(return_statuses == 'Returned', 
                              np.random.choice(['Wrong Size', 'Defective Item', 'Changed Mind', 'Other'], total_purchases, p=[0.4, 0.2, 0.2, 0.2]),
                              '')

    purchase_data = {
        'UserID': user_ids,
        'Date': purchase_dates,
        'OrderNumber': order_numbers,
        'ShippingAddress': shipping_addresses,
        'AmountSpent': purchase_amounts,
        'PaymentMode': payment_modes,
        'SaleStatus': sale_status,
        'ItemsPurchased': items_purchased,
        'DiscountAmount': discount_amounts,
        'ReturnStatus': return_statuses,
        'ReturnReason': return_reasons
    }

    purchase_df = pd.DataFrame(purchase_data)

    return purchase_df

def main():
    num_users = int(input("Number of simulated users: "))
    purchases_per_user = 5

    purchase_df = generate_simulated_purchase_data(num_users, purchases_per_user)
    print(purchase_df.head())

    csv_file_path = "simulated_purchase_data.csv"
    purchase_df.to_csv(csv_file_path, index=False, encoding='utf-8', date_format='%Y-%m-%d')
    print(f"Purchase CSV file saved to {csv_file_path}")

if __name__ == "__main__":
    main()
