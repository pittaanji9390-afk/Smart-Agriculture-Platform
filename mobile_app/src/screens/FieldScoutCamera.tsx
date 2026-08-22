/**
 * Field Scout Camera & Real-Time On-Device Leaf Vision Diagnostic Screen
 */

import React, { useState, useRef } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, ActivityIndicator, Image } from 'react-native';

export const FieldScoutCameraScreen: React.FC = () => {
  const [photoUri, setPhotoUri] = useState<string | null>(null);
  const [isDiagnosing, setIsDiagnosing] = useState(false);
  const [diagnosisResult, setDiagnosisResult] = useState<{
    disease: string;
    confidence: number;
    severity: string;
    remedy: string;
  } | null>(null);

  const handleCaptureAndAnalyze = async () => {
    setIsDiagnosing(true);
    // Simulate real-time on-device quantized model inference (YOLOv8 + MobileNetV3)
    setTimeout(() => {
      setDiagnosisResult({
        disease: 'Tomato Early Blight (Alternaria solani)',
        confidence: 93.8,
        severity: 'MODERATE',
        remedy: 'Apply Mancozeb 75% WP @ 2.5g/L or Copper Oxychloride. Prune lower diseased foliage.',
      });
      setIsDiagnosing(false);
    }, 1200);
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>🌱 AgriSphere Field Scout Vision</Text>
        <Text style={styles.subtitle}>On-Device Edge Leaf Disease Classifier</Text>
      </View>

      <View style={styles.previewBox}>
        {photoUri ? (
          <Image source={{ uri: photoUri }} style={styles.previewImage} />
        ) : (
          <View style={styles.placeholderBox}>
            <Text style={styles.placeholderText}>📸 Point camera at diseased crop leaf</Text>
          </View>
        )}
      </View>

      {diagnosisResult && (
        <View style={styles.resultCard}>
          <Text style={styles.diseaseName}>Detected: {diagnosisResult.disease}</Text>
          <Text style={styles.confidence}>Confidence: {diagnosisResult.confidence}% | Severity: {diagnosisResult.severity}</Text>
          <Text style={styles.remedy}>💊 Treatment: {diagnosisResult.remedy}</Text>
        </View>
      )}

      <TouchableOpacity
        style={styles.captureBtn}
        onPress={handleCaptureAndAnalyze}
        disabled={isDiagnosing}
      >
        {isDiagnosing ? (
          <ActivityIndicator color="#ffffff" />
        ) : (
          <Text style={styles.btnText}>Capture & Run AI Diagnosis</Text>
        )}
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0f172a', padding: 16 },
  header: { marginBottom: 16, marginTop: 24 },
  title: { fontSize: 18, fontWeight: 'bold', color: '#10b981' },
  subtitle: { fontSize: 12, color: '#94a3b8' },
  previewBox: { height: 280, backgroundColor: '#1e293b', borderRadius: 16, overflow: 'hidden', justifyContent: 'center', alignItems: 'center' },
  placeholderBox: { justifyContent: 'center', alignItems: 'center' },
  placeholderText: { color: '#64748b', fontSize: 14 },
  previewImage: { width: '100%', height: '100%' },
  resultCard: { backgroundColor: '#1e293b', padding: 14, borderRadius: 12, marginTop: 14, borderWidth: 1, borderColor: '#334155' },
  diseaseName: { color: '#f8fafc', fontWeight: 'bold', fontSize: 14, marginBottom: 4 },
  confidence: { color: '#10b981', fontSize: 12, marginBottom: 6 },
  remedy: { color: '#cbd5e1', fontSize: 11, lineHeight: 16 },
  captureBtn: { backgroundColor: '#059669', paddingVertical: 14, borderRadius: 12, alignItems: 'center', marginTop: 16 },
  btnText: { color: '#ffffff', fontWeight: 'bold', fontSize: 14 },
});
