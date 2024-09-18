 <h1>Project Setup</h1>
    <h2>1. Install Necessary Packages</h2>
    <p>Before running the code, ensure that you have installed the required packages:</p>
    <pre><code>pip install smartapi-python pyotp logzero</code></pre>
  <h2>2. Add Necessary Details in <code>main.py</code></h2>
    <p>Open <code>main.py</code> and add the following details:</p>
    <pre><code>api_key = "your_api_key"
client_id = "your_client_id"
password = "your_password"
totp_secret = "your_totp_secret"  # TOTP key generated from QR code</code></pre>
<h2>3. Running the Code</h2>
    <p>Make sure to save the file with a <code>.py</code> extension (e.g., <code>websocket_script.py</code>).</p>
    <p>Run the script using:</p>
    <pre><code>python websocket main.py</code></pre>

