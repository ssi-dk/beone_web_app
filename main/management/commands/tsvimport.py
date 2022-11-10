from pathlib import Path
from sys import exit

import pymongo

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = "Import allele profile and metadata from TSV files." + \
            "'folder' must be a valid path to a folder which contains two files with TSV data; " + \
            "one named like 'alleles.tsv' and the other named like 'metadata.tsv', containing " + \
            "allele profiles and metadata, respectively."

    def add_arguments(self, parser):
        parser.add_argument('folder', type=str)
        # parser.add_argument('org', type=str)
        # parser.add_argument('dataset', type=str)

    def handle(self, *args, **options):
        folder = Path(options['folder'])
        if not folder.exists():
            self.stderr.write(f"Folder {folder} does not exist!")
            exit()
        a_path = Path(folder, 'alleles.tsv')
        if not a_path.exists():
            self.stderr.write(f"File {a_path} does not exist!")
            exit()
        m_path = Path(folder, 'metadata.tsv')    
        if not m_path.exists():
            self.stderr.write(f"File {m_path} does not exist!")
            exit()

        self.stdout.write(f"You selected folder {options['folder']} as input folder.")

        connection = pymongo.MongoClient(settings.MONGO_CONNECTION)
        db = connection.get_database()
        number = db.samples.count_documents({})
        self.stdout.write(f'MongoDB currently contains {str(number)} samples (before import).')

        
        with open(a_path) as a_file:
            with open(m_path) as m_file:
                a_header_list = a_file.readline().strip().split('\t')
                a_header_list.pop(0)  # First item is useless; throw away
                print("Allele header list:")
                print(a_header_list)
                m_header_list = m_file.readline().strip().split('\t')
                m_header_list.pop(0)  # Useless item; throw away
                print("Metadata header list:")
                print(m_header_list)
                count = 0
                while True:
                    a_line = a_file.readline().strip()
                    if not a_line:
                        self.stdout.write(f"No more lines in allele file. I have read {count} lines.")
                        break
                    m_line = m_file.readline().strip()
                    if not m_line:
                        self.stdout.write(f"No more lines in metadata file. I have read {count} lines.")
                        break
                    a_list = a_line.split('\t')
                    a_name = a_list.pop(0)
                    m_list = m_line.split('\t')
                    m_name = m_list.pop(0)
                    assert a_name == m_name
                    self.stdout.write(f"Importing sample {a_name}")
                    # Create document in MongoDB, popping off items of both a_list and m_list as they are needed
                    count += 1

        # for line in the two files:
        #     # Or maybe through API?
        #     db.samples.insert({
        #         'org': options['org'],
        #         'name': '$sample.summary.sample'
        #         # Add allele profile from allele_generator
        #         # Assert that sample name from metadata_generator == sample name from allele_generator
        #         # Add metadata from metadata_generator
        #         })

        self.stdout.write(self.style.SUCCESS('Success!'))