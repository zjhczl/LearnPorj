from pyproj import CRS, Transformer

# 定义WGS84坐标系
wgs84_crs = CRS("EPSG:4326")

# 定义CGCS2000坐标系
cgcs2000_crs = CRS("EPSG:4490")

# 创建转换器
transformer = Transformer.from_crs(wgs84_crs, cgcs2000_crs)

# 示例WGS84坐标 (经度, 纬度)
longitude, latitude = 117.20115, 39.12356

# 转换坐标
cgcs2000_longitude, cgcs2000_latitude = transformer.transform(
    latitude, longitude)

print(f"CGCS2000 Coordinates: {cgcs2000_longitude}, {cgcs2000_latitude}")
