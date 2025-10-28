import pandas as pd
import os

# 文件列表
files = [
    '2020complete_typhoon_city_impacts_clean.csv',
    '2021complete_typhoon_city_impacts_clean.csv',
    '2022complete_typhoon_city_impacts_clean.csv',
    '2023complete_typhoon_city_impacts_clean.csv',
    '2024complete_typhoon_city_impacts_clean.csv'
]

# 读取并合并所有CSV文件
all_data = []
for file in files:
    if os.path.exists(file):
        df = pd.read_csv(file)
        # 确保impact_time是字符串类型
        df['impact_time'] = df['impact_time'].astype(str)
        print(f"读取 {file}: {len(df)} 行")
        all_data.append(df)
    else:
        print(f"警告: 文件 {file} 不存在")

# 合并所有数据
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)

    print(f"\n原始数据统计:")
    print(f"总记录数: {len(combined_df)}")
    print(f"省份数量: {combined_df['province'].nunique()}")
    print(f"城市数量: {combined_df['city_name'].nunique()}")

    # 检查所有省级数据（城市名与省名相同的情况）
    province_city_same = combined_df[combined_df['province'] == combined_df['city_name']]
    print(f"\n省级数据记录（城市名与省名相同）:")
    for province in province_city_same['province'].unique():
        count = len(province_city_same[province_city_same['province'] == province])
        print(f"  {province}: {count} 条记录")


    # 为所有省级数据创建具体的城市标识
    def create_city_identifier(row):
        if row['province'] == row['city_name']:
            # 省级数据，基于经纬度创建唯一城市标识
            lat = round(row['impact_latitude'], 1)
            lon = round(row['impact_longitude'], 1)
            return f"{row['province']}_{lat}_{lon}"
        else:
            # 正常城市数据
            return row['city_name']


    # 应用城市标识处理
    combined_df['city_name_processed'] = combined_df.apply(create_city_identifier, axis=1)

    # 添加年份列
    combined_df['year'] = combined_df['impact_time'].str[:4]

    # 添加唯一标识符
    combined_df['unique_id'] = combined_df.index

    # 保存合并后的CSV文件（直接用于GEE上传）
    output_file = 'all_typhoon_impacts_combined.csv'
    combined_df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"\n合并完成!")
    print(f"总记录数: {len(combined_df)}")
    print(f"处理后的城市数量: {combined_df['city_name_processed'].nunique()}")
    print(f"保存为: {output_file}")

    # 显示统计信息
    print(f"\n详细统计:")
    print(f"台风数量: {combined_df['typhoon_id'].nunique()}")
    print(f"原始城市数量: {combined_df['city_name'].nunique()}")
    print(f"处理后城市数量: {combined_df['city_name_processed'].nunique()}")
    print(f"年份范围: {combined_df['year'].min()} - {combined_df['year'].max()}")

    # 显示各年份数据量
    year_counts = combined_df['year'].value_counts().sort_index()
    print(f"\n各年份记录数:")
    for year, count in year_counts.items():
        print(f"  {year}: {count} 条记录")

    # 显示城市统计（前15个）
    city_stats = combined_df['city_name_processed'].value_counts().head(15)
    print(f"\n影响最频繁的前15个城市/位置:")
    for city, count in city_stats.items():
        print(f"  {city}: {count} 次影响记录")

    # 显示台风统计
    typhoon_stats = combined_df.groupby('typhoon_id').agg({
        'typhoon_name': 'first',
        'city_name_processed': 'nunique'
    }).sort_values('city_name_processed', ascending=False).head(10)

    print(f"\n影响城市最多的前10个台风:")
    for typhoon_id, row in typhoon_stats.iterrows():
        print(f"  {typhoon_id}-{row['typhoon_name']}: {row['city_name_processed']} 个城市")

    # 显示省份统计
    province_stats = combined_df['province'].value_counts().head(10)
    print(f"\n影响最严重的前10个省份:")
    for province, count in province_stats.items():
        print(f"  {province}: {count} 条记录")

else:
    print("没有找到任何数据文件!")