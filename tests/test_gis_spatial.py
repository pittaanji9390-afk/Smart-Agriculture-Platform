"""
Unit Tests for Geodesic Area, Ray-Casting & Spatial Heatmap Interpolation
"""

from services.gis_remote_sensing.spatial_db.postgis_field_repository import GeoJSONFieldRepository
from services.gis_remote_sensing.spatial_db.heatmap_interpolator import SpatialHeatmapInterpolator

def test_geodesic_area_calculation():
    # 1 km x 1 km square near Hyderabad, India (approx 100 Hectares)
    coords = [
        [78.4800, 17.3800],
        [78.4894, 17.3800],
        [78.4894, 17.3890],
        [78.4800, 17.3890],
        [78.4800, 17.3800]
    ]
    area_ha = GeoJSONFieldRepository.calculate_geodesic_polygon_area_ha(coords)
    assert area_ha > 80.0
    assert area_ha < 120.0

def test_point_in_field():
    poly = [
        [78.0, 17.0],
        [79.0, 17.0],
        [79.0, 18.0],
        [78.0, 18.0]
    ]
    assert GeoJSONFieldRepository.is_point_in_field_polygon((78.5, 17.5), poly) is True
    assert GeoJSONFieldRepository.is_point_in_field_polygon((80.0, 17.5), poly) is False

def test_idw_interpolation():
    sample_points = [
        (78.1, 17.1, 45.0), # (lon, lat, moisture)
        (78.9, 17.1, 30.0),
        (78.5, 17.9, 55.0)
    ]
    bounds = (78.0, 79.0, 17.0, 18.0)
    result = SpatialHeatmapInterpolator.inverse_distance_weighting(sample_points, bounds, grid_resolution=20)
    assert len(result["grid"]) == 20
    assert result["min_val"] >= 25.0
    assert result["max_val"] <= 60.0
