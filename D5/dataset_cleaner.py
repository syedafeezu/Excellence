def read_raw_data(filename):
    with open(filename,'r') as file:
        data=file.read()
        return data

def clean_row(row):
    row=row.strip().lower()
    row=list(row.split(','))
    
def clean_dataset(data):
    cleaned_data=[]
    rows=list(data.split('\n'))
    for row in rows:
        rows[row]=clean_row(row)
        cleaned_data.append(rows[row])
    return cleaned_data

def save_cleaned(filename, cleaned_data):

def main():
    