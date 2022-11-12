import pandas as pd
import click
# PATH = 'all_v2.csv'
#
# REGION_ID = 2661  # City of Saint Petersburg
#
# MIN_AREA = 15  # Outlier range for floor area
# MAX_AREA = 300
#
# MIN_KITCHEN = 3  # Outlier range for kitchen area
# MAX_KITCHEN = 70
#
# MIN_PRICE = 1_000_000  # Outlier range for price
# MAX_PRICE = 100_000_000
#
# SEED = 15
# N_FOLDS = 5


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
@click.argument("region", type=click.INT)
def select_region(input_path: str, output_path: str, region: int) -> pd.DataFrame:
    """Function selects the listings belonging to a specified region.
    :param input_path
    :param output_path
    :param region
    :return:
    """
    df = pd.read_csv(input_path)

    df = df[df['region'] == region]
    df.drop('region', axis=1, inplace=True)
    print(f'Selected {len(df)} samples in region {region}.')
    df.to_csv(output_path)


if __name__ == '__main__':
    select_region()

# python -m src.data.select_region data/raw/all_v2.csv data/interim/data_regional.csv 2661