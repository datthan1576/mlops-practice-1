import pandas as pd
import numpy as np
import click

PATH = 'all_v2.csv'

REGION_ID = 2661  # City of Saint Petersburg

MIN_AREA = 15  # Outlier range for floor area
MAX_AREA = 300

MIN_KITCHEN = 3  # Outlier range for kitchen area
MAX_KITCHEN = 70

MIN_PRICE = 1_000_000  # Outlier range for price
MAX_PRICE = 100_000_000

SEED = 15
N_FOLDS = 5


@click.command()
@click.argument("input_path", type=click.Path())
@click.argument("output_path", type=click.Path())
def add_features(input_path: str, output_path: str) -> pd.DataFrame:
    # Replace "date" with numeric features for year and month.
    df = pd.read_csv(input_path)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df.drop('date', axis=1, inplace=True)
    # Apartment floor in relation to total number of floors.
    df['level_to_levels'] = df['level'] / df['levels']
    # Average size of room in the apartment.
    df['area_to_rooms'] = (df['area'] / df['rooms']).abs()
    # Fix division by zero.
    df.loc[df['area_to_rooms'] == np.inf, 'area_to_rooms'] = \
        df.loc[df['area_to_rooms'] == np.inf, 'area']

    df.to_csv(output_path)


if __name__ == '__main__':
    add_features()