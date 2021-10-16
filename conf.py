import keyring

query = "RPA impact"
num_page = 2
sender = "fvalevats@edu.hse.ru"
password = keyring.get_password("HSEOutlookPassword", sender) #Get your OS Saved password with keyring.get_password
receiver = "fvalevats@edu.hse.ru"