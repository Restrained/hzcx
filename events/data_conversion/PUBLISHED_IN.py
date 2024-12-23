  #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/26 09:15
# @Author  : AllenWan
# @File    : PUBLISHED_IN.py
import pandas as pd


def get_published_info(input_file1, input_file2, output_file):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    selected_list = ["_id", "year", "volume", "issue", "page_range", "journal_title"]
    df1_selected = df1[selected_list]
    df1_selected['volume'] = df1_selected['volume'].apply(lambda x: int(x) if pd.notna(x) else '')
    columns_mapping = {
        "_id": "article_id",
        "issue": "period",
    }
    df2_selected = df2[["id", "name"]]
    df1_selected = df1_selected.rename(columns=columns_mapping)
    merged = df1_selected.merge(df2_selected, left_on="journal_title", right_on="name")
    final_column_lisst = ["article_id", "id", "year", "volume", "period", "page_range"]
    merged['concatenated'] = merged[final_column_lisst].fillna("").astype(str).apply("⌘".join, axis=1)

    result = merged[['concatenated']]


    with open(output_file, 'w', encoding='utf-8') as f:
        for row in result.itertuples(index=False, name=None):
            # 将每一行的列数据按需要格式化并写入
            # 假设数据是 JSON 格式化的字符串，先去掉可能存在的双引号转义
            row_data = '⌘'.join(map(str, row))  # 将每一行的数据用 "⌘" 分隔
            f.write(row_data + '\n')  # 逐行写入

    return result

if __name__ == '__main__':
    get_published_info(
        input_file1=r"C:\Users\PY-01\Documents\local\renHeHuiZhi\article_info.csv_data", input_file2=r"D:\output\csv_data\venue_info.csv_data", output_file=r"D:\output\csv\PUBLISHED_IN.csv_data"
    )
