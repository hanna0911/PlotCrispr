from django.http import HttpResponse
import json
from .models import Sea, Sequence, Protein
from django.shortcuts import render
from django.core.serializers import serialize


# Create your views here.


# 目录页，分类显示不同海域
def home(request):
    seas = Sea.objects.all()
    return render(request, 'home.html', { 'seas': seas })


def location(request, sea):
    sequences = Sequence.objects.filter(sea = Sea.objects.filter(name = sea).first())
    seas = Sea.objects.all()
    sequences = serialize('json', sequences, fields=['seq_id', 'excel_id'])
    return render(request, 'location_elUI.html', { 'sequences': sequences, 'current_sea': sea, 'seas': seas })


# CRISPR页，按照不同CRISPR序列显示
def crispr(request, crispr_id):
    sequence = Sequence.objects.filter(excel_id=crispr_id).first()  # 测试第一条sequence
    proteins = sequence.protein_set.all()
    seas = Sea.objects.all()
    return render(request, 'crispr.html', {'sequence': sequence, 'proteins': proteins, 'seas': seas })


def crisprs(request, crisprs_id):
    print(crisprs_id)
    crisprs_id_list = []
    id = ""
    for c in crisprs_id:
        if c == '+':
            crisprs_id_list.append(id)
            id = ""
        else:
            id += c
    crisprs_id_list.append(id)
    
    crisprs = []
    for crispr_id in crisprs_id_list:
        sequence = Sequence.objects.filter(excel_id=crispr_id).first()  # 测试第一条sequence
        proteins = sequence.protein_set.all()
        seas = Sea.objects.all()
        crisprs.append({'sequence': sequence, 'proteins': proteins})
    
    return render(request, 'crisprs.html', {'crisprs': crisprs, 'seas': seas})

# 添加Nordic数据
def importData(request):

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
    
    print('finished_importing')
    return HttpResponse('finished_importing')

