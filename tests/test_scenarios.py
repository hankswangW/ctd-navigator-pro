import unittest
from ctd_data import RECORDS, SOURCES
from ctd_sections import SECTION_BY_CODE
from scenario_data import scenario_records
from navigator import search_records

class ScenarioTests(unittest.TestCase):
    def test_content_and_scope(self):
        batch = scenario_records()
        self.assertEqual(len(batch), 24)
        self.assertEqual(len({r['name'] for r in RECORDS}), len(RECORDS))
        for r in batch:
            self.assertTrue(r['work_scenario']['需要向团队索取'])
            self.assertTrue(all(ref in SOURCES for ref in r['sources']))
            self.assertNotEqual(r['stage_guidance']['IND']['重点'], r['stage_guidance']['BLA']['重点'])
            for side in ('DS', 'DP'):
                self.assertTrue(all(m[0] in SECTION_BY_CODE for m in r['mappings'][side]))
            if r['category'].startswith('QA'):
                self.assertIn('没有固定独立 CTD', r['filing_note'])
                self.assertTrue(all(m[2]=='影响相关时交叉' for rows in r['mappings'].values() for m in rows))

    def test_practical_queries(self):
        for query, name in [('CAPA', 'Corrective and preventive action'), ('工艺放大', 'Process scale-up assessment'), ('原始数据缺失', 'Data integrity assessment'), ('复测合格', 'OOS invalidation assessment'), ('技术转移', 'Technology transfer package')]:
            for side in ('DS','DP'):
                self.assertEqual(search_records(query, side)[0][1]['name'], name)
