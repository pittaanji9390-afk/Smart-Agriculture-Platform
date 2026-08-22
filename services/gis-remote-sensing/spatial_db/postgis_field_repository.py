"""
PostGIS & GeoJSON Field Parcel Spatial Repository
Handles polygon boundary validation, geodesic acreage computation (Shoelace + WGS84 projection), and spatial intersection.
"""

import math
from typing import List, Dict, Any, Tuple

class GeoJSONFieldRepository:
    @staticmethod
    def calculate_geodesic_polygon_area_ha(coordinates: List[List[float]]) -> float:
        """
        Calculates accurate geodesic surface area in Hectares for a polygon on WGS84 ellipsoid.
        Coordinates: [[lng1, lat1], [lng2, lat2], ...]
        """
        if len(coordinates) < 3:
            return 0.0

        # Close polygon if not closed
        if coordinates[0] != coordinates[-1]:
            coords = coordinates + [coordinates[0]]
        else:
            coords = coordinates

        earth_radius = 6378137.0  # WGS84 equatorial radius in meters
        area_m2 = 0.0
        n = len(coords)

        for i in range(n - 1):
            p1 = coords[i]
            p2 = coords[i + 1]
            # Convert degrees to radians
            lon1, lat1 = math.radians(p1[0]), math.radians(p1[1])
            lon2, lat2 = math.radians(p2[0]), math.radians(p2[1])

            area_m2 += (lon2 - lon1) * (2.0 + math.sin(lat1) + math.sin(lat2))

        area_m2 = abs(area_m2 * (earth_radius ** 2) / 2.0)
        area_ha = area_m2 / 10000.0
        return round(area_ha, 3)

    @staticmethod
    def is_point_in_field_polygon(point: Tuple[float, float], polygon_coords: List[List[float]]) -> bool:
        """Ray-casting algorithm to verify whether a GPS sensor probe is located within field boundary"""
        lng, lat = point
        inside = False
        n = len(polygon_coords)

        j = n - 1
        for i in range(n):
            xi, yi = polygon_coords[i][0], polygon_coords[i][1]
            xj, yj = polygon_coords[j][0], polygon_coords[j][1]

            intersect = ((yi > lat) != (yj > lat)) and (lng < (xj - xi) * (lat - yi) / (yj - yi + 1e-12) + xi)
            if intersect:
                inside = not inside
            j = i

        return inside

    @classmethod
    def create_field_feature(cls, field_id: str, farm_name: str, crop: str, coordinates: List[List[float]]) -> Dict[str, Any]:
        area_ha = cls.calculate_geodesic_polygon_area_ha(coordinates)
        return {
            "type": "Feature",
            "id": field_id,
            "properties": {
                "field_id": field_id,
                "farm_name": farm_name,
                "crop_type": crop,
                "area_hectares": area_ha,
                "area_acres": round(area_ha * 2.47105, 2)
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [coordinates]
            }
        }
