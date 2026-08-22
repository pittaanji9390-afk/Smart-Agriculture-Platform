"""
Spatial Telemetry Interpolation Engine (IDW & Kriging)
Generates continuous raster surface heatmaps for soil moisture, nitrogen, and temperature across irregular field probe locations.
"""

import numpy as np
import math
from typing import List, Dict, Any, Tuple

class SpatialHeatmapInterpolator:
    @staticmethod
    def inverse_distance_weighting(
        sample_points: List[Tuple[float, float, float]], # (x/lon, y/lat, value)
        grid_bounds: Tuple[float, float, float, float],   # (min_lon, max_lon, min_lat, max_lat)
        grid_resolution: int = 50,
        power: float = 2.0
    ) -> Dict[str, Any]:
        """
        Calculates 2D continuous interpolated grid using Inverse Distance Weighting (IDW).
        """
        min_x, max_x, min_y, max_y = grid_bounds
        x_coords = np.linspace(min_x, max_x, grid_resolution)
        y_coords = np.linspace(min_y, max_y, grid_resolution)
        grid_z = np.zeros((grid_resolution, grid_resolution))

        samples = np.array(sample_points) # shape (N, 3)
        if len(samples) == 0:
            return {"grid": grid_z.tolist(), "min_val": 0.0, "max_val": 0.0}

        for i, y in enumerate(y_coords):
            for j, x in enumerate(x_coords):
                # Calculate Euclidean distances to all sample probes
                dx = samples[:, 0] - x
                dy = samples[:, 1] - y
                distances = np.sqrt(dx**2 + dy**2)

                # Check exact point match
                exact_idx = np.where(distances < 1e-7)[0]
                if len(exact_idx) > 0:
                    grid_z[i, j] = samples[exact_idx[0], 2]
                else:
                    weights = 1.0 / (distances ** power)
                    grid_z[i, j] = np.sum(weights * samples[:, 2]) / np.sum(weights)

        return {
            "grid": np.round(grid_z, 2).tolist(),
            "x_axis": np.round(x_coords, 6).tolist(),
            "y_axis": np.round(y_coords, 6).tolist(),
            "min_val": float(np.min(grid_z)),
            "max_val": float(np.max(grid_z)),
            "mean_val": float(np.mean(grid_z))
        }
