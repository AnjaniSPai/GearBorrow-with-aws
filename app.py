# # # from flask import Flask, render_template, request, redirect
# # # from pymongo import MongoClient

# # # app = Flask(__name__)

# # # # Connect to local MongoDB (Simulating Amazon DynamoDB)
# # # client = MongoClient('mongodb://localhost:27017/')
# # # db = client['gearborrow_db']
# # # inventory_col = db['inventory']
# # # users_col = db['users'] # Your new Users collection!

# # # # Auto-populate the database the first time you run it
# # # if inventory_col.count_documents({}) == 0:
# # #     print("Initializing Cloud Database with Gadgets...")
# # #     initial_data = [
# # #         {"_id": "1", "name": "Meta Quest 3 VR Headset", "price_per_day": 800, "status": "Available", "emoji": "🥽"},
# # #         {"_id": "2", "name": "Sony A7IV 4K Camera", "price_per_day": 1500, "status": "Available", "emoji": "📸"},
# # #         {"_id": "3", "name": "DJI Mini 4 Pro Drone", "price_per_day": 1200, "status": "Available", "emoji": "🚁"},
# # #         {"_id": "4", "name": "MacBook Pro M3 Max", "price_per_day": 2000, "status": "Available", "emoji": "💻"}
# # #     ]
# # #     inventory_col.insert_many(initial_data)

# # # # --- AUTHENTICATION ROUTES ---

# # # @app.route('/auth')
# # # def auth_page():
# # #     return render_template('auth.html')

# # # @app.route('/signup', methods=['POST'])
# # # def signup():
# # #     username = request.form.get('username')
# # #     email = request.form.get('email')
# # #     password = request.form.get('password')
    
# # #     # Prevent duplicate accounts
# # #     if users_col.find_one({"email": email}):
# # #         return "User already exists! Please go back and login."
        
# # #     # Save the new user to MongoDB
# # #     users_col.insert_one({"username": username, "email": email, "password": password})
# # #     return redirect('/')

# # # @app.route('/login', methods=['POST'])
# # # def login():
# # #     # Simulates login and redirects to catalog
# # #     return redirect('/')

# # # # --- CATALOG & RENTAL ROUTES ---

# # # @app.route('/')
# # # def home():
# # #     # Fetch all gadgets from the MongoDB collection
# # #     gadgets = list(inventory_col.find())
# # #     return render_template('index.html', gadgets=gadgets)

# # # @app.route('/rent/<gadget_id>', methods=['POST'])
# # # def rent_gadget(gadget_id):
# # #     days = request.form.get('days')
    
# # #     # Update the document in MongoDB to 'Rented'
# # #     inventory_col.update_one(
# # #         {"_id": gadget_id, "status": "Available"},
# # #         {"$set": {"status": f"Rented for {days} days"}}
# # #     )
    
# # #     # Fetch the exact item data to display on the success page
# # #     rented_item = inventory_col.find_one({"_id": gadget_id})
# # #     return render_template('success.html', item=rented_item, days=days)

# # # @app.route('/return/<gadget_id>', methods=['POST'])
# # # def return_gadget(gadget_id):
# # #     # Reset the document status in MongoDB back to 'Available'
# # #     inventory_col.update_one(
# # #         {"_id": gadget_id},
# # #         {"$set": {"status": "Available"}}
# # #     )
# # #     return redirect('/')

# # # if __name__ == '__main__':
# # #     # Simulating EC2 hosting locally
# # #     app.run(debug=True, port=5000)
# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # # from flask import Flask, render_template, request, redirect, session
# # # from pymongo import MongoClient

# # # app = Flask(__name__)
# # # app.secret_key = "super_secret_gaming_key" # Required for user sessions!

# # # # Connect to local MongoDB
# # # client = MongoClient('mongodb://localhost:27017/')
# # # db = client['gearborrow_db']
# # # inventory_col = db['inventory']
# # # users_col = db['users']

# # # # Auto-populate the database the first time you run it
# # # if inventory_col.count_documents({}) == 0:
# # #     print("Initializing Cloud Database with Gadgets...")
# # #     initial_data = [
# # #         {"_id": "1", "name": "Meta Quest 3 VR Headset", "price_per_day": 800, "status": "Available", "emoji": "🥽"},
# # #         {"_id": "2", "name": "Sony A7IV 4K Camera", "price_per_day": 1500, "status": "Available", "emoji": "📸"},
# # #         {"_id": "3", "name": "DJI Mini 4 Pro Drone", "price_per_day": 1200, "status": "Available", "emoji": "🚁"},
# # #         {"_id": "4", "name": "MacBook Pro M3 Max", "price_per_day": 2000, "status": "Available", "emoji": "💻"}
# # #     ]
# # #     inventory_col.insert_many(initial_data)

# # # # --- AUTHENTICATION ROUTES ---

# # # @app.route('/login_page')
# # # def login_page():
# # #     return render_template('login.html')

# # # @app.route('/signup_page')
# # # def signup_page():
# # #     return render_template('signup.html')

# # # @app.route('/signup', methods=['POST'])
# # # def signup():
# # #     username = request.form.get('username')
# # #     email = request.form.get('email')
# # #     password = request.form.get('password')
    
# # #     if users_col.find_one({"email": email}):
# # #         return "User already exists! Please go back and login."
        
# # #     users_col.insert_one({"username": username, "email": email, "password": password, "role": "user"})
# # #     return redirect('/login_page')

# # # @app.route('/login', methods=['POST'])
# # # def login():
# # #     email = request.form.get('email')
# # #     password = request.form.get('password')
    
# # #     # Check if it is the Admin
# # #     if email == "admin@gearborrow.com" and password == "admin123":
# # #         session['user'] = "Administrator"
# # #         session['role'] = "admin"
# # #         return redirect('/admin')
        
# # #     # Check if it is a normal user
# # #     user = users_col.find_one({"email": email, "password": password})
# # #     if user:
# # #         session['user'] = user['username']
# # #         session['role'] = "user"
# # #         return redirect('/')
    
# # #     return "Invalid Credentials. Try again."

# # # @app.route('/logout')
# # # def logout():
# # #     session.clear()
# # #     return redirect('/login_page')

# # # # --- ROLE-BASED DASHBOARDS ---

# # # @app.route('/admin')
# # # def admin_dashboard():
# # #     # Security check: Kick them out if they aren't an admin
# # #     if session.get('role') != 'admin':
# # #         return redirect('/')
        
# # #     all_users = list(users_col.find())
# # #     return render_template('admin.html', users=all_users, current_user=session.get('user'))

# # # @app.route('/')
# # # def home():
# # #     # Security check: Force them to login first
# # #     if 'user' not in session:
# # #         return redirect('/login_page')
        
# # #     gadgets = list(inventory_col.find())
# # #     return render_template('index.html', gadgets=gadgets, current_user=session.get('user'), role=session.get('role'))

# # # # --- RENTAL ROUTES ---

# # # @app.route('/rent/<gadget_id>', methods=['POST'])
# # # def rent_gadget(gadget_id):
# # #     days = request.form.get('days')
# # #     inventory_col.update_one({"_id": gadget_id, "status": "Available"}, {"$set": {"status": f"Rented for {days} days"}})
# # #     rented_item = inventory_col.find_one({"_id": gadget_id})
# # #     return render_template('success.html', item=rented_item, days=days)

# # # @app.route('/return/<gadget_id>', methods=['POST'])
# # # def return_gadget(gadget_id):
# # #     inventory_col.update_one({"_id": gadget_id}, {"$set": {"status": "Available"}})
# # #     return redirect('/')

# # # if __name__ == '__main__':
# # #     app.run(debug=True, port=5000)

# # from flask import Flask, render_template, request, redirect, session
# # from pymongo import MongoClient

# # app = Flask(__name__)
# # app.secret_key = "super_secret_gaming_key" # Required to remember logged-in users

# # # Connect to local MongoDB
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['gearborrow_db']
# # inventory_col = db['inventory']
# # users_col = db['users']

# # # Auto-populate the database the first time you run it
# # if inventory_col.count_documents({}) == 0:
# #     print("Initializing Cloud Database with Gadgets...")
# #     initial_data = [
# #         {"_id": "1", "name": "Meta Quest 3 VR Headset", "price_per_day": 800, "status": "Available", "emoji": "🥽"},
# #         {"_id": "2", "name": "Sony A7IV 4K Camera", "price_per_day": 1500, "status": "Available", "emoji": "📸"},
# #         {"_id": "3", "name": "DJI Mini 4 Pro Drone", "price_per_day": 1200, "status": "Available", "emoji": "🚁"},
# #         {"_id": "4", "name": "MacBook Pro M3 Max", "price_per_day": 2000, "status": "Available", "emoji": "💻"}
# #     ]
# #     inventory_col.insert_many(initial_data)

# # # --- AUTHENTICATION ROUTES ---

# # @app.route('/login_page')
# # def login_page():
# #     return render_template('login.html')

# # @app.route('/signup_page')
# # def signup_page():
# #     return render_template('signup.html')

# # @app.route('/signup', methods=['POST'])
# # def signup():
# #     username = request.form.get('username')
# #     email = request.form.get('email')
# #     password = request.form.get('password')
    
# #     if users_col.find_one({"email": email}):
# #         return "User already exists! Please go back and login."
        
# #     users_col.insert_one({"username": username, "email": email, "password": password, "role": "user"})
# #     return redirect('/login_page')

# # @app.route('/login', methods=['POST'])
# # def login():
# #     email = request.form.get('email')
# #     password = request.form.get('password')
    
# #     # Check if it is the Admin
# #     if email == "admin@gearborrow.com" and password == "admin123":
# #         session['user'] = "Administrator"
# #         session['role'] = "admin"
# #         return redirect('/admin')
        
# #     # Check if it is a normal user
# #     user = users_col.find_one({"email": email, "password": password})
# #     if user:
# #         session['user'] = user['username']
# #         session['role'] = "user"
# #         return redirect('/')
    
# #     return "Invalid Credentials. Try again."

# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     return redirect('/login_page')

# # # --- ROLE-BASED DASHBOARDS ---

# # @app.route('/admin')
# # def admin_dashboard():
# #     # Security check: Kick them out if they aren't an admin
# #     if session.get('role') != 'admin':
# #         return redirect('/')
        
# #     all_users = list(users_col.find())
# #     return render_template('admin.html', users=all_users, current_user=session.get('user'))

# # @app.route('/')
# # def home():
# #     # Security check: Force them to login first
# #     if 'user' not in session:
# #         return redirect('/login_page')
        
# #     gadgets = list(inventory_col.find())
# #     return render_template('index.html', gadgets=gadgets, current_user=session.get('user'), role=session.get('role'))

# # # --- RENTAL ROUTES ---

# # @app.route('/rent/<gadget_id>', methods=['POST'])
# # def rent_gadget(gadget_id):
# #     if 'user' not in session:
# #         return redirect('/login_page')
        
# #     days = request.form.get('days')
# #     current_user = session.get('user')
    
# #     inventory_col.update_one(
# #         {"_id": gadget_id, "status": "Available"},
# #         {"$set": {"status": f"Rented for {days} days", "rented_by": current_user}}
# #     )
    
# #     rented_item = inventory_col.find_one({"_id": gadget_id})
# #     return render_template('success.html', item=rented_item, days=days)

# # @app.route('/return/<gadget_id>', methods=['POST'])
# # def return_gadget(gadget_id):
# #     if 'user' not in session:
# #         return redirect('/login_page')
        
# #     current_user = session.get('user')
# #     role = session.get('role')
# #     item = inventory_col.find_one({"_id": gadget_id})
    
# #     # SECURITY CHECK: Only Admin OR the person who rented it can return it!
# #     if role == 'admin' or item.get('rented_by') == current_user:
# #         inventory_col.update_one(
# #             {"_id": gadget_id},
# #             {"$set": {"status": "Available"}, "$unset": {"rented_by": ""}}
# #         )
# #     else:
# #         return "Access Denied: You cannot return an item you did not rent."
        
# #     return redirect('/')

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)


# # from flask import Flask, render_template, request, redirect, session
# # from pymongo import MongoClient
# # import random
# # import os
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # app.secret_key = "super_secret_gaming_key"

# # # Configuration for Image Uploads
# # UPLOAD_FOLDER = 'static/uploads'
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # # Connect to local MongoDB
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['gearborrow_db']
# # inventory_col = db['inventory']
# # users_col = db['users']

# # # Auto-populate the database with the NEW schema format
# # if inventory_col.count_documents({}) == 0:
# #     print("Initializing Cloud Database with Gadgets...")
# #     initial_data = [
# #         {"_id": "1", "name": "Meta Quest 3 VR Headset", "price_per_day": 800, "total_stock": 1, "available_stock": 1, "renters": [], "emoji": "🥽", "image_path": ""},
# #         {"_id": "2", "name": "Sony A7IV 4K Camera", "price_per_day": 1500, "total_stock": 1, "available_stock": 1, "renters": [], "emoji": "📸", "image_path": ""},
# #         {"_id": "3", "name": "DJI Mini 4 Pro Drone", "price_per_day": 1200, "total_stock": 1, "available_stock": 1, "renters": [], "emoji": "🚁", "image_path": ""},
# #         {"_id": "4", "name": "MacBook Pro M3 Max", "price_per_day": 2000, "total_stock": 1, "available_stock": 1, "renters": [], "emoji": "💻", "image_path": ""}
# #     ]
# #     inventory_col.insert_many(initial_data)

# # # --- AUTHENTICATION ROUTES ---
# # @app.route('/login_page')
# # def login_page(): return render_template('login.html')

# # @app.route('/signup_page')
# # def signup_page(): return render_template('signup.html')

# # @app.route('/signup', methods=['POST'])
# # def signup():
# #     username = request.form.get('username')
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     if users_col.find_one({"email": email}): return "User already exists! Please go back and login."
# #     users_col.insert_one({"username": username, "email": email, "password": password, "role": "user"})
# #     return redirect('/login_page')

# # @app.route('/login', methods=['POST'])
# # def login():
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     if email == "admin@gearborrow.com" and password == "admin123":
# #         session['user'] = "Administrator"
# #         session['role'] = "admin"
# #         return redirect('/admin')
# #     user = users_col.find_one({"email": email, "password": password})
# #     if user:
# #         session['user'] = user['username']
# #         session['role'] = "user"
# #         return redirect('/')
# #     return "Invalid Credentials. Try again."

# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     return redirect('/login_page')

# # # --- ROLE-BASED DASHBOARDS & CRUD MANAGEMENT ---
# # @app.route('/admin')
# # def admin_dashboard():
# #     if session.get('role') != 'admin': return redirect('/')
# #     return render_template('admin.html', users=list(users_col.find()), gadgets=list(inventory_col.find()), current_user=session.get('user'))

# # @app.route('/admin/add_item', methods=['POST'])
# # def add_item():
# #     if session.get('role') != 'admin': return redirect('/')
        
# #     name = request.form.get('name')
# #     price = request.form.get('price')
# #     emoji = request.form.get('emoji', '')
# #     quantity = int(request.form.get('quantity', 1))
    
# #     image_file = request.files.get('image')
# #     image_path = ""
# #     if image_file and image_file.filename != '':
# #         filename = secure_filename(image_file.filename)
# #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         image_file.save(filepath)
# #         image_path = f"/static/uploads/{filename}"

# #     # Insert ONE pooled document instead of looping!
# #     inventory_col.insert_one({
# #         "_id": str(random.randint(100, 99999)),
# #         "name": name,
# #         "price_per_day": int(price),
# #         "total_stock": quantity,
# #         "available_stock": quantity,
# #         "renters": [],
# #         "emoji": emoji,
# #         "image_path": image_path
# #     })
# #     return redirect('/admin')

# # @app.route('/admin/delete_item/<item_id>', methods=['POST'])
# # def delete_item(item_id):
# #     if session.get('role') != 'admin': return redirect('/')
# #     inventory_col.delete_one({"_id": item_id})
# #     return redirect('/admin')

# # @app.route('/')
# # def home():
# #     if 'user' not in session: return redirect('/login_page')
# #     return render_template('index.html', gadgets=list(inventory_col.find()), current_user=session.get('user'), role=session.get('role'))

# # # --- RENTAL ROUTES (Updated for Stock Pools) ---
# # # @app.route('/rent/<gadget_id>', methods=['POST'])
# # # def rent_gadget(gadget_id):
# # #     if 'user' not in session: return redirect('/login_page')
# # #     days = request.form.get('days')
# # #     current_user = session.get('user')
# # #     item = inventory_col.find_one({"_id": gadget_id})
    
# # #     # Prevent users from hoarding multiple of the same item
# # #     if current_user in item.get('renters', []):
# # #         return "You already have one of these deployed!"
        
# # #     if item and item.get('available_stock', 0) > 0:
# # #         inventory_col.update_one(
# # #             {"_id": gadget_id},
# # #             {
# # #                 "$inc": {"available_stock": -1}, # Decrease stock by 1
# # #                 "$push": {"renters": current_user} # Add username to the list
# # #             }
# # #         )
# # #     return render_template('success.html', item=inventory_col.find_one({"_id": gadget_id}), days=days)

# # @app.route('/rent/<gadget_id>', methods=['POST'])
# # def rent_gadget(gadget_id):
# #     if 'user' not in session: return redirect('/login_page')
    
# #     days = request.form.get('days')
# #     rent_qty = int(request.form.get('rent_qty', 1)) # NEW: Read the quantity!
# #     current_user = session.get('user')
    
# #     item = inventory_col.find_one({"_id": gadget_id})
        
# #     # Check if we have enough stock for what they want
# #     if item and item.get('available_stock', 0) >= rent_qty:
        
# #         # If they rent 2 units, add their name to the list 2 times
# #         new_renters = [current_user] * rent_qty
        
# #         inventory_col.update_one(
# #             {"_id": gadget_id},
# #             {
# #                 "$inc": {"available_stock": -rent_qty}, # Reduce stock by the requested quantity
# #                 "$push": {"renters": {"$each": new_renters}} # Push their name multiple times
# #             }
# #         )
        
# #     updated_item = inventory_col.find_one({"_id": gadget_id})
# #     return render_template('success.html', item=updated_item, days=days, qty=rent_qty)

# # @app.route('/return/<gadget_id>', methods=['POST'])
# # def return_gadget(gadget_id):
# #     if 'user' not in session: return redirect('/login_page')
# #     current_user = session.get('user')
# #     role = session.get('role')
# #     item = inventory_col.find_one({"_id": gadget_id})
    
# #     # If the user rented it, let them return it
# #     if current_user in item.get('renters', []):
# #         renters_list = item.get('renters', [])
# #         renters_list.remove(current_user)
# #         inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
        
# #     # Admin Override: Force return one item from the pool
# #     elif role == 'admin' and len(item.get('renters', [])) > 0:
# #         renters_list = item.get('renters', [])
# #         renters_list.pop(0) 
# #         inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
        
# #     return redirect('/')

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)

# # from flask import Flask, render_template, request, redirect, session
# # from pymongo import MongoClient
# # import random
# # import os
# # from werkzeug.utils import secure_filename
# # from datetime import datetime

# # app = Flask(__name__)
# # app.secret_key = "super_secret_gaming_key"

# # UPLOAD_FOLDER = 'static/uploads'
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # # Connect to MongoDB
# # client = MongoClient('mongodb://localhost:27017/')
# # db = client['gearborrow_db']
# # inventory_col = db['inventory']
# # users_col = db['users']
# # receipts_col = db['receipts'] # NEW: Database for Receipts!

# # if inventory_col.count_documents({}) == 0:
# #     print("Initializing Cloud Database...")
# #     initial_data =[
# #         {"_id": "1", "name": "Meta Quest 3 VR", "price_per_day": 800, "total_stock": 2, "available_stock": 2, "renters": [], "emoji": "🥽", "image_path": ""},
# #         {"_id": "2", "name": "Sony A7IV 4K Camera", "price_per_day": 1500, "total_stock": 3, "available_stock": 3, "renters": [], "emoji": "📸", "image_path": ""},
# #         {"_id": "3", "name": "DJI Mini 4 Pro Drone", "price_per_day": 1200, "total_stock": 2, "available_stock": 2, "renters": [], "emoji": "🚁", "image_path": ""},
# #         {"_id": "4", "name": "MacBook Pro M3 Max", "price_per_day": 2000, "total_stock": 4, "available_stock": 4, "renters": [], "emoji": "💻", "image_path": ""},
# #         {"_id": "5", "name": "PS5 Console", "price_per_day": 3500, "total_stock": 5, "available_stock": 5, "renters": [], "emoji": "🎮", "image_path": ""}
# #     ]
# #     inventory_col.insert_many(initial_data)

# # # --- AUTH ---
# # @app.route('/login_page')
# # def login_page(): return render_template('login.html')

# # @app.route('/signup_page')
# # def signup_page(): return render_template('signup.html')

# # @app.route('/signup', methods=['POST'])
# # def signup():
# #     username = request.form.get('username')
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     if users_col.find_one({"email": email}): return "User exists!"
# #     users_col.insert_one({"username": username, "email": email, "password": password, "role": "user"})
# #     return redirect('/login_page')

# # @app.route('/login', methods=['POST'])
# # def login():
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     if email == "admin@gearborrow.com" and password == "admin123":
# #         session['user'] = "Administrator"
# #         session['role'] = "admin"
# #         return redirect('/admin')
# #     user = users_col.find_one({"email": email, "password": password})
# #     if user:
# #         session['user'] = user['username']
# #         session['role'] = "user"
# #         return redirect('/')
# #     return "Invalid Credentials."

# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     return redirect('/login_page')

# # # --- ADMIN CRUD ---
# # @app.route('/admin')
# # def admin_dashboard():
# #     if session.get('role') != 'admin': return redirect('/')
# #     return render_template('admin.html', users=list(users_col.find()), gadgets=list(inventory_col.find()), current_user=session.get('user'))

# # @app.route('/admin/ledger')
# # def admin_ledger():
# #     # Security check: Only admins can see this master list
# #     if session.get('role') != 'admin': 
# #         return redirect('/')
        
# #     # Fetch all receipts from the database, newest first
# #     all_receipts = list(receipts_col.find().sort("date", -1))
    
# #     return render_template('ledger.html', receipts=all_receipts, current_user=session.get('user'))

# # @app.route('/admin/add_item', methods=['POST'])
# # def add_item():
# #     if session.get('role') != 'admin': return redirect('/')
# #     name = request.form.get('name')
# #     price = int(request.form.get('price'))
# #     emoji = request.form.get('emoji', '')
# #     quantity = int(request.form.get('quantity', 1))
    
# #     image_file = request.files.get('image')
# #     image_path = ""
# #     if image_file and image_file.filename != '':
# #         filename = secure_filename(image_file.filename)
# #         image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# #         image_path = f"/static/uploads/{filename}"

# #     inventory_col.insert_one({
# #         "_id": str(random.randint(100, 99999)), "name": name, "price_per_day": price,
# #         "total_stock": quantity, "available_stock": quantity, "renters": [],
# #         "emoji": emoji, "image_path": image_path
# #     })
# #     return redirect('/admin')

# # @app.route('/admin/update_item/<item_id>', methods=['POST'])
# # def update_item(item_id):
# #     if session.get('role') != 'admin': return redirect('/')
    
# #     name = request.form.get('name')
# #     price = int(request.form.get('price'))
# #     new_total_stock = int(request.form.get('total_stock'))
    
# #     item = inventory_col.find_one({"_id": item_id})
# #     stock_difference = new_total_stock - item['total_stock']
# #     new_available = item['available_stock'] + stock_difference
    
# #     inventory_col.update_one({"_id": item_id}, {"$set": {
# #         "name": name, "price_per_day": price, 
# #         "total_stock": new_total_stock, "available_stock": new_available
# #     }})
# #     return redirect('/admin')

# # @app.route('/admin/delete_item/<item_id>', methods=['POST'])
# # def delete_item(item_id):
# #     if session.get('role') != 'admin': return redirect('/')
# #     inventory_col.delete_one({"_id": item_id})
# #     return redirect('/admin')

# # # --- USER ROUTES & RECEIPTS ---
# # @app.route('/')
# # def home():
# #     if 'user' not in session: return redirect('/login_page')
# #     return render_template('index.html', gadgets=list(inventory_col.find()), current_user=session.get('user'), role=session.get('role'))

# # @app.route('/profile')
# # def profile():
# #     if 'user' not in session: return redirect('/login_page')
# #     current_user = session.get('user')
    
# #     # Fetch all receipts for this user
# #     user_receipts = list(receipts_col.find({"username": current_user}).sort("date", -1))
    
# #     # Calculate grand total spent
# #     total_spent = sum(receipt['total_cost'] for receipt in user_receipts)
    
# #     return render_template('profile.html', current_user=current_user, receipts=user_receipts, total_spent=total_spent)

# # @app.route('/rent/<gadget_id>', methods=['POST'])
# # def rent_gadget(gadget_id):
# #     if 'user' not in session: return redirect('/login_page')
    
# #     days = int(request.form.get('days', 1))
# #     rent_qty = int(request.form.get('rent_qty', 1))
# #     current_user = session.get('user')
# #     item = inventory_col.find_one({"_id": gadget_id})
        
# #     if item and item.get('available_stock', 0) >= rent_qty:
# #         # Calculate Total Cost
# #         total_cost = item['price_per_day'] * days * rent_qty
# #         receipt_id = f"REC-{random.randint(10000, 99999)}"
        
# #         # Save the Receipt
# #         receipts_col.insert_one({
# #             "_id": receipt_id, "username": current_user, "item_id": gadget_id,
# #             "item_name": item['name'], "qty": rent_qty, "days": days,
# #             "total_cost": total_cost, "status": "Active",
# #             "date": datetime.now().strftime("%Y-%m-%d %H:%M")
# #         })

# #         new_renters = [current_user] * rent_qty
# #         inventory_col.update_one(
# #             {"_id": gadget_id},
# #             {"$inc": {"available_stock": -rent_qty}, "$push": {"renters": {"$each": new_renters}}}
# #         )
        
# #     updated_item = inventory_col.find_one({"_id": gadget_id})
# #     return render_template('success.html', item=updated_item, days=days, qty=rent_qty, cost=total_cost, rec_id=receipt_id)

# # @app.route('/return/<gadget_id>', methods=['POST'])
# # def return_gadget(gadget_id):
# #     if 'user' not in session: return redirect('/login_page')
# #     current_user = session.get('user')
# #     role = session.get('role')
# #     item = inventory_col.find_one({"_id": gadget_id})
    
# #     if current_user in item.get('renters', []):
# #         renters_list = item.get('renters', [])
# #         renters_list.remove(current_user) # Removes only ONE instance
# #         inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
# #         # Mark one active receipt as returned
# #         receipts_col.update_one({"username": current_user, "item_id": gadget_id, "status": "Active"}, {"$set": {"status": "Returned"}})
        
# #     elif role == 'admin' and len(item.get('renters', [])) > 0:
# #         renters_list = item.get('renters', [])
# #         popped_user = renters_list.pop(0) 
# #         inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
# #         receipts_col.update_one({"username": popped_user, "item_id": gadget_id, "status": "Active"}, {"$set": {"status": "Returned (Force Admin)"}})
        
# #     return redirect('/')

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)

# from flask import Flask, render_template, request, redirect, session, flash
# from pymongo import MongoClient
# import random
# import os
# from werkzeug.utils import secure_filename
# from datetime import datetime, timedelta

# app = Flask(__name__)
# app.secret_key = "super_secret_gaming_key"

# UPLOAD_FOLDER = 'static/uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Database Connection
# client = MongoClient('mongodb://localhost:27017/')
# db = client['gearborrow_db']
# inventory_col = db['inventory']
# users_col = db['users']
# receipts_col = db['receipts']

# # --- AUTH ROUTES ---
# @app.route('/signup_page')
# def signup_page(): 
#     return render_template('signup.html')

# @app.route('/signup', methods=['POST'])
# def signup():
#     username = request.form.get('username')
#     email = request.form.get('email')
#     password = request.form.get('password')
#     phone = request.form.get('phone')
#     if users_col.find_one({"email": email}): 
#         return "User exists!"
#     users_col.insert_one({
#         "username": username, 
#         "email": email, 
#         "password": password, 
#         "phone": phone, 
#         "role": "user"
#     })
#     return redirect('/login_page')

# @app.route('/login_page')
# def login_page(): 
#     return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def login():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     # Admin default login
#     if email == "admin@gearborrow.com" and password == "admin123":
#         session['user'], session['role'] = "Administrator", "admin"
#         return redirect('/admin')
#     # User login
#     user = users_col.find_one({"email": email, "password": password})
#     if user:
#         session['user'], session['role'] = user['username'], "user"
#         return redirect('/')
#     return "Invalid Credentials."

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/login_page')

# # --- ADMIN ROUTES ---
# @app.route('/admin')
# def admin_dashboard():
#     if session.get('role') != 'admin': 
#         return redirect('/')
#     active_rentals = list(receipts_col.find({"status": "Active"}))
#     return render_template('admin.html', 
#                            gadgets=list(inventory_col.find()), 
#                            active_rentals=active_rentals, 
#                            today_date=datetime.now(), 
#                            current_user=session.get('user'))

# @app.route('/admin/ledger')
# def admin_ledger():
#     if session.get('role') != 'admin': 
#         return redirect('/')
#     # Fetch all receipts from the database, newest first
#     all_receipts = list(receipts_col.find().sort("date", -1))
#     return render_template('ledger.html', receipts=all_receipts, current_user=session.get('user'))

# # --- ADMIN PROCESS RETURN ---
# # @app.route('/return_item/<receipt_id>', methods=['GET', 'POST'])
# # def process_return(receipt_id):
# #     if session.get('role') != 'admin': 
# #         return redirect('/')
    
# #     # If someone tries to type this URL in the browser (GET), just send them back to admin
# #     if request.method == 'GET':
# #         return redirect('/admin')

# #     receipt = receipts_col.find_one({"_id": receipt_id})
# #     if not receipt: 
# #         return redirect('/admin')
    
# #     today = datetime.now()
# #     expected = receipt.get('expected_return', today)
# #     fine = 0
# #     if today > expected:
# #         fine = (today - expected).days * 500
    
# #     receipts_col.update_one({"_id": receipt_id}, {"$set": {"status": "Returned", "fine_paid": fine}})
# #     inventory_col.update_one(
# #         {"_id": receipt['item_id']}, 
# #         {"$inc": {"available_stock": receipt['qty']}, "$pull": {"renters": receipt['username']}}
# #     )
# #     flash(f"Return Processed for {receipt['username']}. Fine: ₹{fine}", "success")
# #     return redirect('/admin')

# # --- ADMIN PROCESS RETURN ---
# @app.route('/return_item/<receipt_id>', methods=['GET', 'POST'])
# def process_return(receipt_id):
#     if session.get('role') != 'admin': return redirect('/')
#     if request.method == 'GET': return redirect('/admin')

#     receipt = receipts_col.find_one({"_id": receipt_id})
#     if not receipt: return redirect('/admin')
    
#     today = datetime.now()
#     expected = receipt.get('expected_return', today)
#     fine = max(0, (today - expected).days * 500) if today > expected else 0
    
#     receipts_col.update_one({"_id": receipt_id}, {"$set": {"status": "Returned", "fine_paid": fine}})
    
#     item_id = receipt['item_id']
#     returned_qty = receipt['qty']
    
#     # 1. Return the item to inventory
#     inventory_col.update_one(
#         {"_id": item_id}, 
#         {"$inc": {"available_stock": returned_qty}, "$pull": {"renters": receipt['username']}}
#     )

#     # 2. ⚡ SMART WAITLIST AUTO-FULFILLMENT ⚡
#     item = inventory_col.find_one({"_id": item_id})
#     current_stock = item['available_stock']
#     waitlist = item.get('waitlist', [])
#     fulfilled_players = []

#     # Keep checking the queue as long as we have stock!
#     while waitlist and current_stock >= waitlist[0]['qty']:
#         next_order = waitlist.pop(0) # Remove first person from queue
#         req_qty = next_order['qty']
#         req_days = next_order['days']
#         req_user = next_order['username']
        
#         # Calculate new rental metrics
#         total_cost = item['price_per_day'] * req_days * req_qty
#         new_expected = datetime.now() + timedelta(days=req_days)
#         new_rec_id = f"REC-{random.randint(10000, 99999)}"
#         u_data = users_col.find_one({"username": req_user})
        
#         # Create an Active receipt for the waitlisted user automatically
#         receipts_col.insert_one({
#             "_id": new_rec_id, "username": req_user, 
#             "user_phone": u_data.get('phone', 'N/A') if u_data else 'N/A',
#             "item_id": item_id, "item_name": item['name'], 
#             "qty": req_qty, "days": req_days, "total_cost": total_cost, 
#             "status": "Active", "rented_on": datetime.now(), 
#             "expected_return": new_expected, "date": datetime.now().strftime("%Y-%m-%d %H:%M")
#         })
        
#         # Deduct stock and assign to new renter
#         current_stock -= req_qty
#         fulfilled_players.append(req_user)
#         inventory_col.update_one(
#             {"_id": item_id},
#             {"$inc": {"available_stock": -req_qty}, "$push": {"renters": {"$each": [req_user]*req_qty}}}
#         )
        
#     # Save the updated (shorter) waitlist back to the database
#     inventory_col.update_one({"_id": item_id}, {"$set": {"waitlist": waitlist}})

#     # Notify the Admin of the magic that just happened
#     flash_msg = f"Return Processed for {receipt['username']}. Fine: ₹{fine}."
#     if fulfilled_players:
#         flash_msg += f" ⚡ Waitlist AUTO-FULFILLED for: {', '.join(fulfilled_players)}!"
        
#     flash(flash_msg, "success")
#     return redirect('/admin')

# # --- USER RECALL EQUIPMENT ---
# # @app.route('/return/<gadget_id>', methods=['GET', 'POST'])
# # def return_gadget(gadget_id):
# #     if 'user' not in session: 
# #         return redirect('/login_page')

# #     # If someone types this URL manually (GET), just send them home
# #     if request.method == 'GET':
# #         return redirect('/')

# #     current_user = session.get('user')
# #     item = inventory_col.find_one({"_id": gadget_id})
    
# #     if item and current_user in item.get('renters', []):
# #         renters_list = item.get('renters', [])
# #         renters_list.remove(current_user)
# #         inventory_col.update_one(
# #             {"_id": gadget_id}, 
# #             {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}}
# #         )
# #         # Update the latest active receipt for this user/item
# #         receipts_col.update_one(
# #             {"username": current_user, "item_id": gadget_id, "status": "Active"}, 
# #             {"$set": {"status": "Returned"}}
# #         )
# #         flash(f"Equipment {item['name']} has been recalled and returned to the armory.", "success")
        
# #     return redirect('/')

# # --- USER RECALL EQUIPMENT ---
# @app.route('/return/<gadget_id>', methods=['GET', 'POST'])
# def return_gadget(gadget_id):
#     if 'user' not in session: return redirect('/login_page')
#     if request.method == 'GET': return redirect('/')

#     current_user = session.get('user')
#     item = inventory_col.find_one({"_id": gadget_id})
    
#     if item and current_user in item.get('renters', []):
#         renters_list = item.get('renters', [])
#         renters_list.remove(current_user)
        
#         # Return to stock
#         inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
#         receipts_col.update_one({"username": current_user, "item_id": gadget_id, "status": "Active"}, {"$set": {"status": "Returned"}})
        
#         # ⚡ SMART WAITLIST AUTO-FULFILLMENT ⚡
#         updated_item = inventory_col.find_one({"_id": gadget_id})
#         current_stock = updated_item['available_stock']
#         waitlist = updated_item.get('waitlist', [])
#         fulfilled_players = []
        
#         while waitlist and current_stock >= waitlist[0]['qty']:
#             next_order = waitlist.pop(0)
#             req_qty, req_days, req_user = next_order['qty'], next_order['days'], next_order['username']
            
#             total_cost = updated_item['price_per_day'] * req_days * req_qty
#             new_expected = datetime.now() + timedelta(days=req_days)
#             new_rec_id = f"REC-{random.randint(10000, 99999)}"
#             u_data = users_col.find_one({"username": req_user})
            
#             receipts_col.insert_one({
#                 "_id": new_rec_id, "username": req_user, "user_phone": u_data.get('phone', 'N/A') if u_data else 'N/A',
#                 "item_id": gadget_id, "item_name": updated_item['name'], "qty": req_qty, "days": req_days, 
#                 "total_cost": total_cost, "status": "Active", "rented_on": datetime.now(), 
#                 "expected_return": new_expected, "date": datetime.now().strftime("%Y-%m-%d %H:%M")
#             })
            
#             current_stock -= req_qty
#             fulfilled_players.append(req_user)
#             inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": -req_qty}, "$push": {"renters": {"$each": [req_user]*req_qty}}})
            
#         inventory_col.update_one({"_id": gadget_id}, {"$set": {"waitlist": waitlist}})
        
#         msg = f"Equipment {updated_item['name']} returned to armory."
#         if fulfilled_players:
#             msg += f" ⚡ Instantly transferred to waitlisted player(s): {', '.join(fulfilled_players)}."
#         flash(msg, "success")
        
#     return redirect('/')

# # --- USER ROUTES ---
# # --- 1. UPDATE THE HOME ROUTE ---
# @app.route('/')
# def home():
#     if 'user' not in session: return redirect('/login_page')
    
#     gadgets = list(inventory_col.find())
#     today = datetime.now()
    
#     # Calculate days until available for out-of-stock items
#     for g in gadgets:
#         if g.get('available_stock', 0) == 0:
#             # Find the earliest expected return date for this specific item
#             active = list(receipts_col.find({"item_id": g["_id"], "status": "Active"}).sort("expected_return", 1))
#             if active:
#                 earliest = active[0].get('expected_return', today)
#                 diff = (earliest - today).days
#                 g['days_until_available'] = diff if diff > 0 else 0
#             else:
#                 g['days_until_available'] = 0

#     return render_template('index.html', gadgets=gadgets, current_user=session.get('user'), role=session.get('role'))

# @app.route('/profile')
# def profile():
#     if 'user' not in session: 
#         return redirect('/login_page')
#     current_user = session.get('user')
#     # Fetch all receipts for this user, newest first
#     user_receipts = list(receipts_col.find({"username": current_user}).sort("date", -1))
#     # Calculate total spent
#     total_spent = sum(receipt.get('total_cost', 0) for receipt in user_receipts)
#     return render_template('profile.html', 
#                            current_user=current_user, 
#                            receipts=user_receipts, 
#                            total_spent=total_spent)

# @app.route('/rent/<gadget_id>', methods=['POST'])
# def rent_gadget(gadget_id):
#     if 'user' not in session: 
#         return redirect('/login_page')
#     days = int(request.form.get('days', 1))
#     qty = int(request.form.get('rent_qty', 1))
#     item = inventory_col.find_one({"_id": gadget_id})
#     user_data = users_col.find_one({"username": session['user']})
    
#     if item and item['available_stock'] >= qty:
#         expected = datetime.now() + timedelta(days=days)
#         rec_id = f"REC-{random.randint(10000, 99999)}"
#         total_price = item['price_per_day'] * days * qty
        
#         receipts_col.insert_one({
#             "_id": rec_id, 
#             "username": session['user'], 
#             "user_phone": user_data.get('phone', 'N/A') if user_data else 'N/A',
#             "item_id": gadget_id, 
#             "item_name": item['name'], 
#             "qty": qty, 
#             "days": days,
#             "total_cost": total_price, 
#             "status": "Active",
#             "rented_on": datetime.now(), 
#             "expected_return": expected, 
#             "date": datetime.now().strftime("%Y-%m-%d %H:%M")
#         })
        
#         inventory_col.update_one(
#             {"_id": gadget_id}, 
#             {"$inc": {"available_stock": -qty}, "$push": {"renters": {"$each": [session['user']]*qty}}}
#         )
#         return render_template('success.html', item=item, days=days, qty=qty, cost=total_price, rec_id=rec_id)
#     return redirect('/')

# # --- 2. UPDATE THE PREBOOK ROUTE ---
# @app.route('/prebook/<gadget_id>', methods=['POST'])
# def prebook_gadget(gadget_id):
#     if 'user' not in session: return redirect('/login_page')
    
#     qty = int(request.form.get('prebook_qty', 1))
#     days = int(request.form.get('prebook_days', 1)) # NEW: Capture requested days
    
#     item = inventory_col.find_one({"_id": gadget_id})
#     if item:
#         # Create a waitlist record
#         waitlist_entry = {
#             "username": session['user'],
#             "qty": qty,
#             "days": days,
#             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
#         }
#         # Push to the database queue
#         inventory_col.update_one({"_id": gadget_id}, {"$push": {"waitlist": waitlist_entry}})
        
#         flash(f"Success! You are on the waitlist for {qty} unit(s) of {item['name']} for {days} days.", "success")
        
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


from flask import Flask, render_template, request, redirect, session, flash
from pymongo import MongoClient
import random
import os
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
# Automatically scans and loads configuration keys if a .env file exists (on AWS)
load_dotenv()

app = Flask(__name__)
app.secret_key = "super_secret_gaming_key"

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database Connection
# client = MongoClient('mongodb://localhost:27017/')
# Database Connection
# If MONGO_URI is found in the environment, it connects to the cloud. Otherwise, it uses your local laptop database.
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')

client = MongoClient(MONGO_URI)

db = client['gearborrow_db']
inventory_col = db['inventory']
users_col = db['users']
receipts_col = db['receipts']

# Local File Upload Folder Setup
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dynamic AWS S3 Configurations
AWS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME', 'gearborrow-storage-2026')

s3_client = None
if AWS_KEY and AWS_SECRET:
    import boto3
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET
    )

def upload_file_safely(file):
    """
    Uploads directly to AWS S3 Cloud if credentials exist (on the AWS EC2 instance).
    Gracefully falls back to your local laptop storage folder if you are testing offline.
    """
    filename = secure_filename(file.filename)
    
    # Strategy A: Upload to AWS S3 Cloud
    if s3_client:
        try:
            s3_client.upload_fileobj(
                file,
                BUCKET_NAME,
                filename,
                ExtraArgs={"ACL": "public-read", "ContentType": file.content_type}
            )
            return f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        except Exception as e:
            print(f"AWS S3 Upload failed, falling back to local storage: {e}")
            file.seek(0)  # Reset file reader pointer if upload failed halfway

    # Strategy B: Local Laptop Fallback Storage
    local_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(local_path)
    return f"/static/uploads/{filename}"

# --- AUTH ROUTES ---
@app.route('/signup_page')
def signup_page(): 
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    phone = request.form.get('phone')
    if users_col.find_one({"email": email}): 
        return "User exists!"
    users_col.insert_one({
        "username": username, 
        "email": email, 
        "password": password, 
        "phone": phone, 
        "role": "user"
    })
    return redirect('/login_page')

@app.route('/login_page')
def login_page(): 
    return render_template('login.html')

# --- UPDATE THIS IN YOUR LOGIN ROUTE ---
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email == "admin@gearborrow.com" and password == "admin123":
        session['user'], session['role'] = "Administrator", "admin"
        return redirect('/admin')
        
    user = users_col.find_one({"email": email, "password": password})
    if user:
        session['user'], session['role'] = user['username'], "user"
        # ⚡ ADD THESE TWO LINES TO FIX THE "N/A" ISSUE
        session['email'] = user.get('email', 'N/A')
        session['phone'] = user.get('phone', 'N/A')
        return redirect('/')
    return "Invalid Credentials."

# --- ADD THIS NEW ROUTE FOR THE ADMIN USER REGISTRY ---
@app.route('/admin/users')
def admin_users():
    if session.get('role') != 'admin': 
        return redirect('/')
    # Fetch all users from the database
    all_users = list(users_col.find())
    return render_template('user_registry.html', users=all_users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login_page')

# --- ADMIN ROUTES ---
@app.route('/admin')
def admin_dashboard():
    if session.get('role') != 'admin': 
        return redirect('/')
    active_rentals = list(receipts_col.find({"status": "Active"}))
    return render_template('admin.html', 
                           gadgets=list(inventory_col.find()), 
                           active_rentals=active_rentals, 
                           today_date=datetime.now(), 
                           current_user=session.get('user'))

@app.route('/admin/ledger')
def admin_ledger():
    if session.get('role') != 'admin': 
        return redirect('/')
    # Fetch all receipts from the database, newest first
    all_receipts = list(receipts_col.find().sort("date", -1))
    return render_template('ledger.html', receipts=all_receipts, current_user=session.get('user'))

# --- ADMIN PROCESS RETURN WITH AUTO-FULFILLMENT ---
# @app.route('/return_item/<receipt_id>', methods=['GET', 'POST'])
# def process_return(receipt_id):
#     if session.get('role') != 'admin': return redirect('/')
#     if request.method == 'GET': return redirect('/admin')

#     receipt = receipts_col.find_one({"_id": receipt_id})
#     if not receipt: return redirect('/admin')
    
#     today = datetime.now()
#     expected = receipt.get('expected_return', today)
#     fine = max(0, (today - expected).days * 500) if today > expected else 0
    
#     receipts_col.update_one({"_id": receipt_id}, {"$set": {"status": "Returned", "fine_paid": fine}})
    
#     item_id = receipt['item_id']
#     returned_qty = receipt['qty']
    
#     # Find this section in your process_return route in app.py
#     receipt = receipts_col.find_one({"_id": receipt_id})
#     today = datetime.now()
#     expected = receipt.get('expected_return', today)

#     # 1. Calculate the fine
#     fine = max(0, (today - expected).days * 500) if today > expected else 0

#     # 2. Update the total_cost by ADDING the fine to the original rental price
#     new_total = receipt.get('total_cost', 0) + fine

#     receipts_col.update_one(
#         {"_id": receipt_id}, 
#         {"$set": {
#             "status": "Returned", 
#             "fine_paid": fine,
#             "total_cost": new_total  # This ensures the grand total includes the fine
#         }}
#     )

#     # 1. Return the item to inventory
#     inventory_col.update_one(
#         {"_id": item_id}, 
#         {"$inc": {"available_stock": returned_qty}, "$pull": {"renters": receipt['username']}}
#     )

#     # 2. ⚡ SMART WAITLIST AUTO-FULFILLMENT ENGINE ⚡
#     trigger_waitlist_assignment(item_id)

#     flash(f"Return Processed for {receipt['username']}. Fine: ₹{fine}", "success")
#     return redirect('/admin')

@app.route('/return_item/<receipt_id>', methods=['GET', 'POST'])
def process_return(receipt_id):
    if session.get('role') != 'admin': return redirect('/')
    if request.method == 'GET': return redirect('/admin')

    receipt = receipts_col.find_one({"_id": receipt_id})
    if not receipt: return redirect('/admin')
    
    today = datetime.now()
    expected = receipt.get('expected_return', today)
    
    # Calculate the fine (₹500 per day late)
    fine = max(0, (today - expected).days * 500) if today > expected else 0
    
    # Update the total_cost by ADDING the fine to the original rental price
    # This ensures the grand total includes the fine correctly
    # new_total = receipt.get('total_cost', 0) + fine
    
    receipts_col.update_one(
        {"_id": receipt_id}, 
        {"$set": {
            "status": "Returned", 
            "fine_paid": fine,
            # "total_cost": new_total  
        }}
    )
    
    # Return the item to inventory
    inventory_col.update_one(
        {"_id": receipt['item_id']}, 
        {"$inc": {"available_stock": receipt['qty']}, "$pull": {"renters": receipt['username']}}
    )

    # Trigger waitlist auto-fulfillment logic
    trigger_waitlist_assignment(receipt['item_id'])

    flash(f"Return Processed for {receipt['username']}. Fine: ₹{fine}", "success")
    return redirect('/admin')

# --- USER ROUTES ---
@app.route('/')
def home():
    if 'user' not in session: return redirect('/login_page')
    
    gadgets = list(inventory_col.find())
    today = datetime.now()
    
    for g in gadgets:
        # Initialize the attribute for ALL gadgets to prevent Jinja2 errors
        g['days_until_available'] = 0
        if g.get('available_stock', 0) == 0:
            active = list(receipts_col.find({"item_id": g["_id"], "status": "Active"}).sort("expected_return", 1))
            if active:
                earliest = active[0].get('expected_return', today)
                diff = (earliest - today).days
                g['days_until_available'] = diff if diff > 0 else 0
          

    return render_template('index.html', gadgets=gadgets, current_user=session.get('user'), role=session.get('role'))

@app.route('/profile')
def profile():
    if 'user' not in session: return redirect('/login_page')
    current_user = session.get('user')
    
    user_receipts = list(receipts_col.find({"username": current_user}).sort("date", -1))
    
    # This sum will now include the updated total_costs (including any added fines)
    # total_spent = sum(receipt.get('total_cost', 0) for receipt in user_receipts)
    
    # NEW logic: Sum (Base Cost + Fine) for every receipt
    total_spent = sum((r.get('total_cost', 0) + r.get('fine_paid', 0)) for r in user_receipts)

    return render_template('profile.html', 
                           current_user=current_user, 
                           receipts=user_receipts, 
                           total_spent=total_spent)

@app.route('/rent/<gadget_id>', methods=['POST'])
def rent_gadget(gadget_id):
    if 'user' not in session: 
        return redirect('/login_page')
    days = int(request.form.get('days', 1))
    qty = int(request.form.get('rent_qty', 1))
    item = inventory_col.find_one({"_id": gadget_id})
    user_data = users_col.find_one({"username": session['user']})
    
    if item and item['available_stock'] >= qty:
        create_rental_receipt(session['user'], user_data.get('phone', 'N/A'), item, qty, days)
        return redirect('/') # Standard redirect after manual rent
    return redirect('/')

@app.route('/prebook/<gadget_id>', methods=['POST'])
def prebook_gadget(gadget_id):
    if 'user' not in session: return redirect('/login_page')
    
    qty = int(request.form.get('prebook_qty', 1))
    days = int(request.form.get('prebook_days', 1))
    
    item = inventory_col.find_one({"_id": gadget_id})
    if item:
        waitlist_entry = {
            "username": session['user'],
            "qty": qty,
            "days": days,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        inventory_col.update_one({"_id": gadget_id}, {"$push": {"waitlist": waitlist_entry}})
        flash(f"Success! You are on the waitlist for {qty} unit(s) of {item['name']}.", "success")
        
    return redirect('/')

@app.route('/return/<gadget_id>', methods=['POST'])
def return_gadget(gadget_id):
    if 'user' not in session: return redirect('/login_page')

    current_user = session.get('user')
    item = inventory_col.find_one({"_id": gadget_id})
    
    if item and current_user in item.get('renters', []):
        renters_list = item.get('renters', [])
        renters_list.remove(current_user)
        
        inventory_col.update_one({"_id": gadget_id}, {"$inc": {"available_stock": 1}, "$set": {"renters": renters_list}})
        receipts_col.update_one({"username": current_user, "item_id": gadget_id, "status": "Active"}, {"$set": {"status": "Returned"}})
        
        # ⚡ Trigger auto-fulfillment check
        trigger_waitlist_assignment(gadget_id)
        flash(f"Equipment {item['name']} returned.", "success")
        
    return redirect('/')

# --- SMART LOGIC HELPERS ---

def create_rental_receipt(username, phone, item, qty, days):
    """Utility to handle database updates for a successful rental."""
    expected = datetime.now() + timedelta(days=days)
    rec_id = f"REC-{random.randint(10000, 99999)}"
    total_price = item['price_per_day'] * days * qty
    
    receipts_col.insert_one({
        "_id": rec_id, 
        "username": username, 
        "user_phone": phone,
        "item_id": item['_id'], 
        "item_name": item['name'], 
        "qty": qty, 
        "days": days,
        "total_cost": total_price, 
        "status": "Active",
        "rented_on": datetime.now(), 
        "expected_return": expected, 
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    
    inventory_col.update_one(
        {"_id": item['_id']}, 
        {"$inc": {"available_stock": -qty}, "$push": {"renters": {"$each": [username]*qty}}}
    )

# def trigger_waitlist_assignment(item_id):
#     """Automatically assigns stock to the waitlist queue if available."""
#     item = inventory_col.find_one({"_id": item_id})
#     current_stock = item['available_stock']
#     waitlist = item.get('waitlist', [])
    
#     while waitlist and current_stock >= waitlist[0]['qty']:
#         next_up = waitlist.pop(0)
#         u_data = users_col.find_one({"username": next_up['username']})
        
#         # Transform waitlist entry into an active rental
#         create_rental_receipt(
#             next_up['username'], 
#             u_data.get('phone', 'N/A'), 
#             item, 
#             next_up['qty'], 
#             next_up['days']
#         )
        
#         # Update local stock count for the loop check
#         current_stock -= next_up['qty']
    
#     # Save the cleared queue back to the item
#     inventory_col.update_one({"_id": item_id}, {"$set": {"waitlist": waitlist}})

def trigger_waitlist_assignment(item_id):
    """Automatically assigns stock to the waitlist queue if available."""
    item = inventory_col.find_one({"_id": item_id})
    current_stock = item['available_stock']
    waitlist = item.get('waitlist', [])

    fulfilled_any = False

    while waitlist and current_stock >= waitlist[0]['qty']:
        next_up = waitlist.pop(0)
        u_data = users_col.find_one({"username": next_up['username']})
        user_phone = u_data.get('phone', 'N/A') if u_data else 'N/A'

        # 1. Create the actual active rental record
        create_rental_receipt(
            next_up['username'], 
            user_phone, # Pass the fresh phone number here 
            item, 
            next_up['qty'], 
            next_up['days']
        )
        
        # 2. ⚡ CRITICAL: Update the actual database stock ⚡
        inventory_col.update_one(
            {"_id": item_id},
            {"$inc": {"available_stock": -next_up['qty']}, 
             "$push": {"renters": {"$each": [next_up['username']] * next_up['qty']}}}
        )
        
        current_stock -= next_up['qty']
        fulfilled_any = True

    # 3. Save the shortened waitlist back to the database
    if fulfilled_any:
        inventory_col.update_one({"_id": item_id}, {"$set": {"waitlist": waitlist}})

# --- ADMIN USER DIRECTORY ---
@app.route('/admin/users')
def admin_user_directory():
    if session.get('role') != 'admin': 
        return redirect('/')
    # Fetch all registered users
    all_users = list(users_col.find())
    return render_template('user_directory.html', users=all_users, current_user=session.get('user'))

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user' not in session: return redirect('/login_page')
    
    new_email = request.form.get('email')
    new_phone = request.form.get('phone')
    username = session['user']
    
    # Update the database
    users_col.update_one(
        {"username": username},
        {"$set": {"email": new_email, "phone": new_phone}}
    )
    
    # Update the session so the changes show up immediately on the profile
    session['email'] = new_email
    session['phone'] = new_phone
    
    flash("Profile updated successfully!", "success")
    return redirect('/profile')

if __name__ == '__main__':
    # If running on AWS (where credentials exist), listen on 0.0.0.0 so the internet can access it.
    # If running on your laptop, restrict it safely to localhost 127.0.0.1.
    if os.environ.get('AWS_ACCESS_KEY_ID'):
        host_env = '0.0.0.0'
    else:
        host_env = '127.0.0.1'
        
    print(f"Starting GearBorrow App on host: {host_env}")
    app.run(host=host_env, port=5000, debug=True)
    # app.run(debug=True, port=5000)