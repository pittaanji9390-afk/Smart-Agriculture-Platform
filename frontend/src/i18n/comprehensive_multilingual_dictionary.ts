/**
 * Comprehensive Agronomic Multilingual Dictionary Master Aggregator
 */
export interface AgronomicGlossaryEntry {
  termId: string;
  english: string;
  hindi: string;
  telugu: string;
  category: string;
  definition: string;
}

import { GLOSSARY_GLOSSARY_PART_01 } from "./glossary_data/glossary_part_01";
import { GLOSSARY_GLOSSARY_PART_02 } from "./glossary_data/glossary_part_02";
import { GLOSSARY_GLOSSARY_PART_03 } from "./glossary_data/glossary_part_03";
import { GLOSSARY_GLOSSARY_PART_04 } from "./glossary_data/glossary_part_04";
import { GLOSSARY_GLOSSARY_PART_05 } from "./glossary_data/glossary_part_05";
import { GLOSSARY_GLOSSARY_PART_06 } from "./glossary_data/glossary_part_06";
import { GLOSSARY_GLOSSARY_PART_07 } from "./glossary_data/glossary_part_07";
import { GLOSSARY_GLOSSARY_PART_08 } from "./glossary_data/glossary_part_08";
import { GLOSSARY_GLOSSARY_PART_09 } from "./glossary_data/glossary_part_09";
import { GLOSSARY_GLOSSARY_PART_10 } from "./glossary_data/glossary_part_10";

export const COMPREHENSIVE_AGRONOMIC_GLOSSARY: AgronomicGlossaryEntry[] = [
  ...GLOSSARY_GLOSSARY_PART_01,
  ...GLOSSARY_GLOSSARY_PART_02,
  ...GLOSSARY_GLOSSARY_PART_03,
  ...GLOSSARY_GLOSSARY_PART_04,
  ...GLOSSARY_GLOSSARY_PART_05,
  ...GLOSSARY_GLOSSARY_PART_06,
  ...GLOSSARY_GLOSSARY_PART_07,
  ...GLOSSARY_GLOSSARY_PART_08,
  ...GLOSSARY_GLOSSARY_PART_09,
  ...GLOSSARY_GLOSSARY_PART_10,
];
