from io import StringIO
import pandas as pd


def create_df_from_links(brands, prices, filtered_links):
    # Using zip to combine the two lists into pairs
    data = {'id': range(1, len(brands) + 1), 'brand': brands, 'price': prices, 'link': filtered_links}
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by='price', ascending=True)
    # Reset the index if needed
    sorted_df = sorted_df.reset_index(drop=True)
    sorted_df['id'] = range(1, len(df) + 1)  # Add the 'id' column with ascending values
    return sorted_df


def store_df_to_csv(df, filepath):
    csv_buffer = StringIO()
    df.to_csv(filepath, index=False)
    return csv_buffer


