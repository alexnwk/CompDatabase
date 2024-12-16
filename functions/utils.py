def read_tickers_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        # Strip newline characters and any extra spaces from each line
        tickers = [line.strip() for line in lines if line.strip()]
    return tickers