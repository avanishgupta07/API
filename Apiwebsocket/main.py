
from SmartApi import SmartConnect  # Import SmartConnect from SmartApi
import pyotp
from logzero import logger

api_key = ''  # Replace with your actual API Key
username = ''  # Replace with your client code
pwd = ''  # Replace with your pin or password
token = ''  # Replace with your TOTP QR value
smartApi = SmartConnect(api_key)


try:
    # Generate TOTP from QR value
    totp = pyotp.TOTP(token).now()
    logger.info(f"TOTP Generated: {totp}")
    
    # Generate session
    data = smartApi.generateSession(username, pwd, totp)
    if not data.get('status'):
        logger.error(f"Session generation failed: {data.get('message')}")
    else:
        logger.info("Session Generated Successfully")
        authToken = data['data'].get('jwtToken')
        refreshToken = data['data'].get('refreshToken')
        logger.info(f"Auth Token: {authToken}")
except Exception as e:
    logger.error("An error occurred during TOTP generation or session creation.")
    logger.exception(e)

# Historic Candle Data Fetch
try:
    # Define historic candle parameters
    historicParam = {
        "exchange": "NSE",  # Set exchange, e.g., NSE
        "symboltoken": "3045",  # Replace with your symbol token
        "interval": "ONE_MINUTE",  # Interval for candle data
        "fromdate": "2024-09-18 09:10",  # Start date and time for historical data
        "todate": "2024-09-18 09:17"  # End date and time for historical data
    }

    # Fetch historical data using getCandleData method
    candleData = smartApi.getCandleData(historicParam)
    logger.info(f"Historic Candle Data: {candleData}")
    #columns = ["time", "o","h","l","c","v"]


except Exception as e:
    logger.error("An error occurred while fetching historic candle data.")
    logger.exception(e)

# Logout and terminate session
try:
    logout = smartApi.terminateSession(username)
    if logout.get('status'):
        logger.info("Logout Successful")
    else:
        logger.error(f"Logout failed: {logout.get('message')}")
except Exception as e:
    logger.error("An error occurred during logout.")
    logger.exception(e)



