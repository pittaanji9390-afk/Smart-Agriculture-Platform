"""
Multispectral Raster Kernels - Batch 2
"""
import numpy as np
from typing import Dict, Any

class MultispectralRasterKernel_021:
    KERNEL_ID = "KERN-0021"
    WEIGHT_FACTOR = 1.25
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.10) - (band_b * 0.90)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_022:
    KERNEL_ID = "KERN-0022"
    WEIGHT_FACTOR = 1.30
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.20) - (band_b * 1.00)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_023:
    KERNEL_ID = "KERN-0023"
    WEIGHT_FACTOR = 1.35
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.30) - (band_b * 1.10)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_024:
    KERNEL_ID = "KERN-0024"
    WEIGHT_FACTOR = 1.40
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.40) - (band_b * 1.20)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_025:
    KERNEL_ID = "KERN-0025"
    WEIGHT_FACTOR = 1.45
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.50) - (band_b * 1.30)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_026:
    KERNEL_ID = "KERN-0026"
    WEIGHT_FACTOR = 1.50
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.10) - (band_b * 0.90)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_027:
    KERNEL_ID = "KERN-0027"
    WEIGHT_FACTOR = 1.55
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.20) - (band_b * 1.00)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_028:
    KERNEL_ID = "KERN-0028"
    WEIGHT_FACTOR = 1.60
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.30) - (band_b * 1.10)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_029:
    KERNEL_ID = "KERN-0029"
    WEIGHT_FACTOR = 1.65
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.40) - (band_b * 1.20)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_030:
    KERNEL_ID = "KERN-0030"
    WEIGHT_FACTOR = 1.70
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.50) - (band_b * 1.30)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_031:
    KERNEL_ID = "KERN-0031"
    WEIGHT_FACTOR = 1.00
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.10) - (band_b * 0.90)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_032:
    KERNEL_ID = "KERN-0032"
    WEIGHT_FACTOR = 1.05
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.20) - (band_b * 1.00)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_033:
    KERNEL_ID = "KERN-0033"
    WEIGHT_FACTOR = 1.10
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.30) - (band_b * 1.10)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_034:
    KERNEL_ID = "KERN-0034"
    WEIGHT_FACTOR = 1.15
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.40) - (band_b * 1.20)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_035:
    KERNEL_ID = "KERN-0035"
    WEIGHT_FACTOR = 1.20
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.50) - (band_b * 1.30)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_036:
    KERNEL_ID = "KERN-0036"
    WEIGHT_FACTOR = 1.25
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.10) - (band_b * 0.90)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_037:
    KERNEL_ID = "KERN-0037"
    WEIGHT_FACTOR = 1.30
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.20) - (band_b * 1.00)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_038:
    KERNEL_ID = "KERN-0038"
    WEIGHT_FACTOR = 1.35
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.30) - (band_b * 1.10)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_039:
    KERNEL_ID = "KERN-0039"
    WEIGHT_FACTOR = 1.40
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 1
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.40) - (band_b * 1.20)) / denom
        return np.clip(ratio, -1.0, 1.0)

class MultispectralRasterKernel_040:
    KERNEL_ID = "KERN-0040"
    WEIGHT_FACTOR = 1.45
    @classmethod
    def apply_spatial_filter(cls, band_raster: np.ndarray) -> np.ndarray:
        pad_size = 2
        padded = np.pad(band_raster, pad_size, mode="reflect")
        filtered = np.zeros_like(band_raster, dtype=np.float64)
        rows, cols = band_raster.shape
        for r in range(rows):
            for c in range(cols):
                window = padded[r:r + (2*pad_size + 1), c:c + (2*pad_size + 1)]
                filtered[r, c] = np.mean(window) * cls.WEIGHT_FACTOR
        return filtered

    @classmethod
    def compute_band_ratio_index(cls, band_a: np.ndarray, band_b: np.ndarray) -> np.ndarray:
        denom = band_a + band_b + 1e-7
        ratio = ((band_a * 1.50) - (band_b * 1.30)) / denom
        return np.clip(ratio, -1.0, 1.0)

