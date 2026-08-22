/**
 * WatermelonDB Offline-First Relational Database Schema
 * Stores scouting logs, offline disease diagnostics, and geo-tagged soil samples in remote farms.
 */

import { appSchema, tableSchema } from '@nozbe/watermelondb';

export const agrisphereOfflineSchema = appSchema({
  version: 1,
  tables: [
    tableSchema({
      name: 'farm_plots',
      columns: [
        { name: 'server_id', type: 'string', isIndexed: true },
        { name: 'plot_name', type: 'string' },
        { name: 'crop_type', type: 'string' },
        { name: 'area_acres', type: 'number' },
        { name: 'polygon_geojson', type: 'string' },
        { name: 'created_at', type: 'number' },
      ],
    }),
    tableSchema({
      name: 'scout_records',
      columns: [
        { name: 'plot_id', type: 'string', isIndexed: true },
        { name: 'latitude', type: 'number' },
        { name: 'longitude', type: 'number' },
        { name: 'observation_type', type: 'string' }, // PEST, DISEASE, WEED, IRRIGATION_LEAK
        { name: 'severity_level', type: 'string' }, // LOW, MEDIUM, HIGH, CRITICAL
        { name: 'diagnosis_label', type: 'string' },
        { name: 'confidence_score', type: 'number' },
        { name: 'photo_uri', type: 'string' },
        { name: 'notes', type: 'string' },
        { name: 'is_synced', type: 'boolean', isIndexed: true },
        { name: 'timestamp', type: 'number', isIndexed: true },
      ],
    }),
    tableSchema({
      name: 'soil_offline_samples',
      columns: [
        { name: 'sample_code', type: 'string' },
        { name: 'plot_id', type: 'string', isIndexed: true },
        { name: 'depth_cm', type: 'number' },
        { name: 'measured_moisture_pct', type: 'number' },
        { name: 'measured_ph', type: 'number' },
        { name: 'measured_ec', type: 'number' },
        { name: 'is_synced', type: 'boolean' },
        { name: 'timestamp', type: 'number' },
      ],
    }),
  ],
});
