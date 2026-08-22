/**
 * GPS Field Geo-Fencing & Scouting Route Tracker
 */

export interface GeoLocation {
  latitude: number;
  longitude: number;
  accuracyMeters?: number;
}

export class GeoFencingService {
  public static isInsideFieldPolygon(
    currentPos: GeoLocation,
    polygonBoundary: Array<[number, number]>
  ): boolean {
    const { longitude: x, latitude: y } = currentPos;
    let isInside = false;

    for (let i = 0, j = polygonBoundary.length - 1; i < polygonBoundary.length; j = i++) {
      const xi = polygonBoundary[i][0];
      const yi = polygonBoundary[i][1];
      const xj = polygonBoundary[j][0];
      const yj = polygonBoundary[j][1];

      const intersect =
        yi > y !== yj > y && x < ((xj - xi) * (y - yi)) / (yj - yi + 1e-10) + xi;
      if (intersect) isInside = !isInside;
    }

    return isInside;
  }

  public static calculateHaversineDistanceMeters(
    loc1: GeoLocation,
    loc2: GeoLocation
  ): number {
    const R = 6371e3; // Earth radius in meters
    const phi1 = (loc1.latitude * Math.PI) / 180;
    const phi2 = (loc2.latitude * Math.PI) / 180;
    const deltaPhi = ((loc2.latitude - loc1.latitude) * Math.PI) / 180;
    const deltaLambda = ((loc2.longitude - loc1.longitude) * Math.PI) / 180;

    const a =
      Math.sin(deltaPhi / 2) * Math.sin(deltaPhi / 2) +
      Math.cos(phi1) * Math.cos(phi2) * Math.sin(deltaLambda / 2) * Math.sin(deltaLambda / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    return Math.round(R * c);
  }
}
