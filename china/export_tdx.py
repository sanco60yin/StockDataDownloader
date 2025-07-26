import argparse
from pathlib import Path
import pandas as pd
from pytdx.reader import TdxDailyBarReader, TdxMinBarReader


def export_daily(data_dir: Path, output_dir: Path):
    reader = TdxDailyBarReader()
    for market in ['sh', 'sz']:
        market_dir = data_dir / 'vipdoc' / market / 'lday'
        if not market_dir.exists():
            continue
        for day_file in market_dir.glob('*.day'):
            df = reader.get_df(day_file)
            code = day_file.stem
            out_file = output_dir / f"{code}.csv"
            df.to_csv(out_file, index=False)


def export_minute(data_dir: Path, output_dir: Path):
    reader = TdxMinBarReader()
    for market in ['sh', 'sz']:
        market_dir = data_dir / 'vipdoc' / market / 'minline'
        if not market_dir.exists():
            continue
        for min_file in market_dir.glob('*.lc1'):
            df = reader.get_df(min_file)
            code = min_file.stem
            out_file = output_dir / f"{code}_1min.csv"
            df.to_csv(out_file, index=False)


def main():
    parser = argparse.ArgumentParser(description='Export TDX data to CSV')
    parser.add_argument('--tdxdir', type=Path, required=True, help='Path to Tongdaxin data directory')
    parser.add_argument('--outdir', type=Path, required=True, help='Output directory for CSV files')
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    export_daily(args.tdxdir, args.outdir)
    export_minute(args.tdxdir, args.outdir)


if __name__ == '__main__':
    main()
