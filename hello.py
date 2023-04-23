import xml.etree.ElementTree as ET
import csv
import logging

# Set up logging
logging.basicConfig(filename='DLTIN.log', level=logging.DEBUG, 
    format='%(asctime)s:%(levelname)s:%(message)s')

# Parse the XML file and get the root element
tree = ET.parse('DLTINS_20210117_01of01.xml')
root = tree.getroot()

# Create a CSV file and write the header
with open('DLTIN_Output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['FinInstrmGnlAttrbts.Id', 'FinInstrmGnlAttrbts.FullNm', 'FinInstrmGnlAttrbts.ClssfctnTp', 'FinInstrmGnlAttrbts.CmmdtyDerivInd', 'FinInstrmGnlAttrbts.NtnlCcy', 'Issr'])

    # Write content of XML file to the CSV file
    for elem in root.findall('.//FinInstrm'):
        writer.writerow([
            elem.find('FinInstrmGnlAttrbts/Id').text,
            elem.find('FinInstrmGnlAttrbts/FullNm').text,
            elem.find('FinInstrmGnlAttrbts/ClssfctnTp').text,
            elem.find('FinInstrmGnlAttrbts/CmmdtyDerivInd').text,
            elem.find('FinInstrmGnlAttrbts/NtnlCcy').text,
            elem.find('Issr').text,
        ])

    # Log a message indicating the CSV file was created
    logging.info('CSV file created: DLTIN_Output.csv')

# Parse the XML file and get the root element
tree = ET.parse('DLTINS_20210117_01of01.xml')
root = tree.getroot()

# Find all FinInstrmGnlAttrbts elements
fin_instrm_gnl_attrbts = root.findall('.//FinInstrmGnlAttrbts')

# Log the number of FinInstrmGnlAttrbts elements found
logging.info(f'{len(fin_instrm_gnl_attrbts)} FinInstrmGnlAttrbts elements found')

# Print the contents of the first FinInstrmGnlAttrbts element (if it exists)
if len(fin_instrm_gnl_attrbts) > 0:
    logging.debug(ET.tostring(fin_instrm_gnl_attrbts[0]))
else:
    logging.warning('No FinInstrmGnlAttrbts elements found')


    
