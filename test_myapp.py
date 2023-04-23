import unittest
import os
import csv
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from myapp import parse_xml_to_csv

class TestMyApp(unittest.TestCase):

    def test_parse_xml_to_csv(self):
        # Ensure that the CSV file is created and contains data
        xml_file = 'test_data.xml'
        csv_file = 'test_output.csv'
        parse_xml_to_csv(xml_file, csv_file)

        self.assertTrue(os.path.isfile(csv_file))
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            headers = next(csv_reader)
            self.assertEqual(headers, ['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])
            rows = list(csv_reader)
            self.assertTrue(len(rows) > 0)

        # Ensure that an exception is raised when the XML file is invalid
        invalid_xml_file = 'invalid_test_data.xml'
        with self.assertRaises(ParseError):
            parse_xml_to_csv(invalid_xml_file, csv_file)

if __name__ == '__main__':
    unittest.main()
