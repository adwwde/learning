绘图步骤：
1.导入all_typhoon_impacts_combined.csv输入文件
2.运行gee绘图代码

注：
1.2020-2024complete_typhoon_city_impacts_clean.csv为处理过后的台风城市记录，多次同一台风经历同一城市算作多次记录
解释如下：
字段名	示例值	含义解释
typhoon_id	2304	台风编号，国际标准编号（2023年第4号台风）
typhoon_name	TALIM	台风英文名称（泰利）
province	Guangxi	影响的省份名称（广西）
city_name	Beihai	影响的具体城市名称（北海）
impact_time	2023071800	影响时间，格式：YYYYMMDDHH（2023年7月18日00时）
impact_latitude	21.7	影响点的纬度坐标
impact_longitude	109.0	影响点的经度坐标
wind_speed	25	风速（m/s），25米/秒相当于10级风
pressure	980	中心气压（hPa），气压越低台风越强
intensity_code	3	强度等级代码（用于分类可视化）
intensity_level	台风	强度等级中文描述
track_point_index	26	轨迹点序号，表示这是台风路径中的第26个记录点
impact_type	中心经过	影响类型：中心经过/外围影响/登陆等
sequence_in_city	1	在该城市的影响顺序（同一台风可能多次影响同一城市）

2.all_typhoon_impacts_combined.csv为2020-2024汇总文件，按照城市汇总，将对应台风去重，多次同一台风经历同一城市算作一次记录（唯一标识）
解释如下：
字段名	示例值	含义解释
typhoon_id	2002	台风编号（2020年第2号台风）
typhoon_name	Nuri	台风英文名称（鹦鹉）
province	Guangdong	影响的省份名称（广东）
city_name	Yangjiang	影响的具体城市名称（阳江）
impact_time	2020061403	影响时间：2020年6月14日03时
impact_latitude	21.8	影响点的纬度坐标
impact_longitude	111.7	影响点的经度坐标
wind_speed	18	风速（18m/s，相当于8级风）
pressure	995	中心气压（995 hPa）
intensity_code	2	强度等级代码：2=强热带风暴
intensity_level	强热带风暴	强度等级中文描述
track_point_index	22	轨迹点序号（第22个记录点）
impact_type	中心经过	影响类型
sequence_in_city	1	在该城市的影响顺序
city_name_processed	Yangjiang	处理后的城市名称（用于数据匹配）
year	2020	年份（便于按年统计分析）
unique_id	0	唯一标识符（用于数据去重和关联）
