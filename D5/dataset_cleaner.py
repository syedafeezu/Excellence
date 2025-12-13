def read_raw_data(filename):
    with open(filename,'r') as file:
        data=file.read()
        return data

def clean_row(row):
    row=row.strip()
    # row=list(row.split(','))
    # for i in range(1,len(row)):
    #     if row[i]=='' or row[i]==' ':
    #         row[i]=0
    #     row[i]=str(row[i]).strip()
    # row[0]=str(row[0]).capitalize().strip()
    # if row[0]=='' or row[0]==' ':
    #     return ''
    # row=','.join(map(str,row))
    # return(row)
    #the commented code is solely mine, the below code is after reference and question clarification

    parts=row.split(',')
    if len(parts)!=3:
        return None
    name=parts[0].strip().capitalize()
    age=parts[1].strip()
    score=parts[2].strip()
    
    if name=='':
        return None
    if age=='' or not age.isdigit():
        age='0'
    if score=='' or not score.isdigit():
        score='0' # return None if we dont want rows with empty/invalid scores
    return f"{name},{age},{score}"

def clean_dataset(data):
    cleaned_data=[]
    rows=data.splitlines()
    # for row in range(1,len(rows)):
    #     rows[row]=clean_row(rows[row])
    #     if rows[row]!='':
    #         cleaned_data.append(rows[row])
        
    # cleaned_data='\n'.join(map(str,cleaned_data))
    # return cleaned_data
    #the commented code is solely mine, the below code is after reference and question clarification
    for row in rows[1:]:
        cleaned_row=clean_row(row)
        if cleaned_row is not None:
            cleaned_data.append(cleaned_row)
    cleaned_data='\n'.join(cleaned_data)
    return cleaned_data

def save_cleaned(filename, cleaned_data):
    with open(filename,'w') as file:
        file.write(cleaned_data)
        
def main():
    file=r'D5/raw_data.txt'
    print('Loading dataset...')
    data=read_raw_data(file)
    print('Cleaning dataset...')
    cleaned_data=clean_dataset(data)
    print('Saving cleaned dataset...')
    save_cleaned(r'D5/cleaned_data.txt',str(cleaned_data))
    print('Done! , Here is the cleaned data:')
    print(cleaned_data)

main()