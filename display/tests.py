from django.test import TestCase
import json
from .models import Sea, Sequence, Protein


# Create your tests here.
class importDataTests(TestCase):
    def test_importData(self):

        # Nordic海域
        with open('Nordic34.json') as f:
            sequences = json.loads(f.read())

        Sea.objects.create(name = 'Nordic')

        for sequence in sequences:
            Sequence.objects.create(sea = Sea.objects.filter(name = 'Nordic').first(), 
                                    excel_id = sequence['excel_id'],
                                    seq_id = sequence['seq_id'],
                                    CRISPR_start = sequence['CRISPR_start'],
                                    CRISPR_end = sequence['CRISPR_end'])
            crispr = Sequence.objects.get(excel_id = sequence['excel_id'])
            for protein in sequence['proteins']:
                Protein.objects.create(crispr = crispr,
                                    protein_id = protein['protein_id'],
                                    faa_id = protein['faa_id'], 
                                    protein_start = protein['protein_start'],
                                    protein_end = protein['protein_end'],
                                    E_value = protein['E_value'], 
                                    distace_between_CRISPR_pro = protein['distace_between_CRISPR_pro'],
                                    length = protein['length'], 
                                    anno_name = protein['anno_name'], 
                                    pfam_anno_name = protein['pfam_anno_name'], 
                                    function = protein['function'])

        self.assertIs(True, True)