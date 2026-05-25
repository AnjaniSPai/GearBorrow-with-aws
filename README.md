1.Wake up the Server
Log into the AWS Console, select your instance, click Instance state, and click Start instance.

Wait about 45 seconds until the instance state turns green and says Running.

2. Copy the New Link
Look at the lower details panel and copy the brand-new Public IPv4 address (remember, it will be different from today's IP).

3. Restart the Backend Processes
Click the Connect button at the top right to open the black terminal window.

Once the prompt appears, copy and paste this entire block into the terminal and hit Enter:

Bash
# 1. Enter the directory and activate the environment
cd GearBorrow-with-aws && source venv/bin/activate

# 2. Restart your background MongoDB database container
sudo docker start my-mongodb

# 3. Launch the website in the background
nohup python3 app.py > app.log 2>&1 &
(Press Enter one more time to return to a clean command line).

🌐 Step 3: Present Your Project!
Open a fresh browser tab and enter your new URL:

Plaintext
http://<YOUR_NEW_PUBLIC_IP>:5000
