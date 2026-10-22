import unittest

from navigator import confidence_label, normalize, search_records


class NavigatorTests(unittest.TestCase):
    def test_normalize_handles_case_and_punctuation(self):
        self.assertEqual(normalize("  CCI / Test "), "cci test")

    def test_coa_maps_to_ds_batch_analysis(self):
        score, record = search_records("CoA", "DS")[0]
        self.assertGreaterEqual(score, 0.9)
        self.assertEqual(record["mappings"]["DS"][0][0], "3.2.S.4.4")

    def test_cci_is_not_returned_for_ds(self):
        results = search_records("CCI", "DS")
        self.assertFalse(any(r["name"].startswith("CCI") for _, r in results))

    def test_ppq_switches_section_by_scope(self):
        ds = search_records("PPQ", "DS")[0][1]
        dp = search_records("PPQ", "DP")[0][1]
        self.assertEqual(ds["mappings"]["DS"][0][0], "3.2.S.2.5")
        self.assertEqual(dp["mappings"]["DP"][0][0], "3.2.P.3.5")

    def test_chinese_alias(self):
        _, record = search_records("使用中稳定性", "DP")[0]
        self.assertTrue(record["name"].startswith("CIU"))

    def test_confidence_labels(self):
        self.assertEqual(confidence_label(0.9), "高匹配")
        self.assertEqual(confidence_label(0.6), "可能匹配")

    def test_raw_material_release_maps_to_control_of_materials(self):
        _, record = search_records("原料放行", "DS")[0]
        self.assertEqual(record["mappings"]["DS"][0][0], "3.2.S.2.3")

    def test_packaging_release_maps_to_p7(self):
        _, record = search_records("包材放行", "DP")[0]
        self.assertEqual(record["mappings"]["DP"][0][0], "3.2.P.7")

    def test_all_records_have_operational_metadata(self):
        from ctd_data import RECORDS
        self.assertGreaterEqual(len(RECORDS), 130)
        self.assertTrue(all(r.get("category") and r.get("filing_note") and r.get("review_en") for r in RECORDS))

    def test_adc_and_ich_terms_are_searchable(self):
        self.assertEqual(search_records("HCP", "DS")[0][1]["zh"], "宿主细胞蛋白（HCP）")
        self.assertEqual(search_records("QTPP", "DP")[0][1]["name"], "Quality Target Product Profile")
        self.assertIn("Drug-to-antibody ratio", [r["name"] for _, r in search_records("DAR", "DS")])

    def test_m4q_section_map_is_complete_at_leaf_level(self):
        from ctd_sections import CTD_SECTIONS
        codes = {s["code"] for s in CTD_SECTIONS}
        self.assertGreaterEqual(len(codes), 50)
        self.assertIn("3.2.S.4.3", codes)
        self.assertIn("3.2.P.8.3", codes)
        self.assertIn("3.2.A.2", codes)


if __name__ == "__main__":
    unittest.main()

