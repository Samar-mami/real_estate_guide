from io import StringIO
import pandas as pd


def create_df_from_links(brands, prices, filtered_links):
    # Using zip to combine the two lists into pairs
    data = {'id': range(1, len(brands) + 1), 'brand': brands, 'price': prices, 'link': filtered_links}
    df = pd.DataFrame(data)
    return df


def store_df_to_csv(df, filepath):
    csv_buffer = StringIO()
    df.to_csv(filepath, index=False)
    return csv_buffer


