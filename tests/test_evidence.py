import unittest
from ctd_data import RECORDS, SOURCES
from ctd_sections import SECTION_BY_CODE
from evidence_data import batch_records
from navigator import search_records

class EvidenceTests(unittest.TestCase):
    def test_batch_integrity(self):
        batch = batch_records()
        self.assertEqual(len(batch), 18)
        self.assertEqual(len({r["name"] for r in RECORDS}), len(RECORDS))
        for r in batch:
            self.assertTrue(r["basics"] and r["ra_insight"] and r["review_en"])
            self.assertTrue(all(source in SOURCES for source in r["sources"]))
            for side in r["scope"]:
                self.assertTrue(r["mappings"][side])
                self.assertTrue(all(m[0] in SECTION_BY_CODE for m in r["mappings"][side]))

    def test_stage_coverage_and_difference(self):
        for r in RECORDS:
            self.assertNotEqual(r["stage_guidance"]["IND"]["重点"], r["stage_guidance"]["BLA"]["重点"])
            self.assertTrue(r["stage_guidance_level"])

    def test_batch_search(self):
        for query, name in [("p188", "Poloxamer 188"), ("ppq sampling", "PPQ sampling plan"), ("cpv plan", "Continued process verification plan")]:
            self.assertEqual(search_records(query, "DP")[0][1]["name"], name)

    def test_full_catalogue_has_explanations_and_sources(self):
        for r in RECORDS:
            with self.subTest(name=r["name"]):
                self.assertTrue(r["basics"]["是什么 / 定义"])
                self.assertTrue(r["basics"]["应用场景"])
                for field in ("申报目的", "评价的风险", "支持的结论", "证据边界", "监管关注的原因", "来源与解释性质"):
                    self.assertTrue(r["ra_insight"][field])
                self.assertEqual(r["stage_guidance_level"], "条目级解释")
                self.assertTrue(all(source in SOURCES for source in r["sources"]))

    def test_original_profiles_have_distinct_limits(self):
        from original_profiles import TESTS, REPORTS, CONCEPTS
        expected = set(TESTS) | set(REPORTS) | set(CONCEPTS)
        originals = [r for r in RECORDS if r["name"] in expected]
        self.assertEqual(len(originals), 159)
        self.assertEqual(len({r["ra_insight"]["证据边界"] for r in originals}), 159)
        by_name = {r["name"]: r for r in originals}
        self.assertIn("不证明整批", by_name["Sterility"]["ra_insight"]["证据边界"])
        self.assertIn("不同载药分布", by_name["Drug-to-antibody ratio"]["ra_insight"]["证据边界"])
        self.assertIn("相关性", by_name["Process characterization report"]["ra_insight"]["证据边界"])

    def test_missing_original_profile_is_detected(self):
        from original_profiles import upgrade_original_records
        with self.assertRaisesRegex(ValueError, "Missing original profile"):
            upgrade_original_records([{"name": "Unreviewed test", "category": "test"}])
