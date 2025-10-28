# remove_bom.py
# 移除CSV文件的BOM字符

def remove_bom_from_csv(input_file, output_file):
    """移除CSV文件的BOM字符"""
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ BOM字符已移除: {input_file} -> {output_file}")


# 为所有年份文件移除BOM
for year in [2020, 2021, 2022, 2023, 2024]:
    input_file = f'{year}complete_typhoon_city_impacts.csv'
    output_file = f'{year}complete_typhoon_city_impacts_clean.csv'

    try:
        remove_bom_from_csv(input_file, output_file)
    except FileNotFoundError:
        print(f"❌ 文件未找到: {input_file}")

print("🎉 所有文件处理完成！请使用 *_clean.csv 文件上传到GEE")