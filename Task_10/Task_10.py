import pandas as pd
from functools import partial

# ========================== PART A: General Transformation Function ==========================
def transform_data(data, column_mapping=None, date_format=None, 
                   numeric_precision=2, missing_values='drop', 
                   filters=None):
    if column_mapping:
        data = data.rename(columns=column_mapping)

    if date_format:
        data['date'] = pd.to_datetime(data['date']).dt.strftime(date_format)

    if numeric_precision is not None:
        data['value'] = data['value'].round(numeric_precision)

    if missing_values == 'drop':
        data = data.dropna()
    elif missing_values == 'fill_zero':
        data = data.fillna(0)
    elif missing_values == 'fill_mean':
        data = data.fillna(data.mean())

    if filters:
        for col, val in filters.items():
            data = data[data[col] == val]

    return data

# ========================== PART B: Specialized Processors using Partial ==========================
finance_processor = partial(transform_data, column_mapping={'value': 'amount'},
                            date_format='%Y-%m-%d', numeric_precision=2,
                            missing_values='fill_zero')

marketing_processor = partial(transform_data, column_mapping={'value': 'sales'},
                              numeric_precision=0, missing_values='drop',
                              filters={'sales': lambda x: x > 0})

scientific_processor = partial(transform_data, numeric_precision=4,
                               missing_values='fill_mean', date_format='%s')

# ========================== PART C: Process Pipeline Function ==========================
def process_pipeline(data_source, source_type):
    processor_map = {
        'finance': finance_processor,
        'marketing': marketing_processor,
        'scientific': scientific_processor
    }
    processor = processor_map.get(source_type, lambda x: x)
    return processor(data_source)

# ========================== Running the Transformations ==========================
if __name__ == "__main__":
    df = pd.read_csv("data.csv")

    finance_result = process_pipeline(df[df['category'] == 'finance'], 'finance')
    marketing_result = process_pipeline(df[df['category'] == 'marketing'], 'marketing')
    scientific_result = process_pipeline(df[df['category'] == 'scientific'], 'scientific')

    print("Processed Finance Data:")
    print(finance_result)
    print("
Processed Marketing Data:")
    print(marketing_result)
    print("
Processed Scientific Data:")
    print(scientific_result)
