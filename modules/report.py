"""
Report Generation Module
"""

# TODO: Install and import pandas
# import pandas as pd


def generate_report(results, output_file):
    """Export results to CSV using pandas.
    results: list of dicts with keys: name, file, score, matched_keywords, missing_keywords
    """
    import pandas as pd
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Report exported to {output_file}")
