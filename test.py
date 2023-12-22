from pyproj import CRS, Transformer

# 定义WGS84坐标系
wgs84_crs = CRS('epsg:4326')

# 定义横轴墨卡托投影坐标系
tmerc_crs = CRS('+proj=tmerc +lat_0=35.0773230869776 +lon_0=117.3635622350329 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m +geoidgrids=egm96_15.gtx +vunits=m +no_defs')

# 创建一个从WGS84到横轴墨卡托投影坐标系的转换器
transformer = Transformer.from_crs(wgs84_crs, tmerc_crs)

# 假设有一个WGS84坐标点
lon, lat = 117.0, 35.0

# 将WGS84坐标转换为横轴墨卡托投影坐标
x, y = transformer.transform(lat, lon)

print(f"Projected coordinates: x={x}, y={y}")
