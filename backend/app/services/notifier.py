def notify_price_change(product_name, new_price):
    with open("events.log", "a") as f:
        f.write(f"{product_name} price changed to {new_price}\n")