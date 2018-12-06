from edc_constants.constants import (
    NOT_APPLICABLE, OTHER, FAILED_ELIGIBILITY, UNKNOWN)
from edc_visit_tracking.constants import (
    SCHEDULED, UNSCHEDULED, LOST_VISIT, MISSED_VISIT, COMPLETED_PROTOCOL_VISIT)
from .constants import BROUGHT, REALTIME, CLOTH_NAPPY, BREASTFEED_ONLY, TUBERCULOSIS

CNS_ABNORMALITIES = (
    ('None', 'None'),
    ('Anencephaly', 'Anencephaly'),
    ('Encephaloceis', 'Encephaloceis'),
    ('Spina bifida, open', 'Spina bifida, open'),
    ('Spina bifida, closed', 'Spina bifida, closed'),
    ('Holoprosencephaly', 'Holoprosencephaly'),
    ('Isolated hydroencephaly (not associated with spina bifida)',
     'Isolated hydroencephaly (not associated with spina bifida)'),
    ('Other CNS defect, specify', 'Other CNS defect, specify'),
)

CLEFT_DISORDER = (
    ('None', 'None'),
    ('Cleft lip without cleft palate', 'Cleft lip without cleft palate'),
    ('Cleft palate without cleft lip', 'Cleft palate without cleft lip'),
    ('Cleft lip and palate', 'Cleft lip and palate'),
    ('Cleft uvula', 'Cleft uvula'),
)

RELATIONSHIP_CHOICES = (
    ('Not related', 'Not related'),
    ('Probably not related', 'Probably not related'),
    ('Possibly related', 'Possibly related'),
    ('Probably related', 'Probably related'),
    ('Definitely related', 'Definitely related'),
)

CARDIOVASCULAR_DISORDER = (
    ('None', 'None'),
    ('Truncus arteriosus', 'Truncus arteriosus'),
    ('Atrial septal defect', 'Atrial septal defect'),
    ('Ventricula septal defect', 'Ventricula septal defect'),
    ('Atrioventricular canal', 'Atrioventricular canal'),
    ('Complete transposition of the great vessels (without VSD)',
     'Complete transposition of the great vessels (without VSD)'),
    ('Complete transposition of the great vessels (with VSD)',
     'Complete transposition of the great vessels (with VSD)'),
    ('Tetralogy of Fallot', 'Tetralogy of Fallot'),
    ('Pulmonary valve stenosis or atresia',
     'Pulmonary valve stenosis or atresia'),
    ('Tricuspid valve stenosis or atresia',
     'Tricuspid valve stenosis or atresia'),
    ('Mitral valve stenosis or atresia', 'Mitral valve stenosis or atresia'),
    ('Hypoplastic left ventricle', 'Hypoplastic left ventricle'),
    ('Hypoplastic right ventricle', 'Hypoplastic right ventricle'),
    ('Congenital cardiomyopath (do not code if only isolated cardiomegaly)',
     'Congenital cardiomyopath (do not code if only isolated cardiomegaly)'),
    ('Coarclation of the aorta', 'Coarclation of the aorta'),
    ('Total anomalous pulmonary venous return',
     'Total anomalous pulmonary venous return'),
    ('Arteriovenous malformation, specify site',
     'Arteriovenous malformation, specify site'),
    ('Patent ductous arteriosus (persisting >6 weeks of age)',
     'Patent ductous arteriosus (persisting >6 weeks of age)'),
    (OTHER, 'Other cardiovascular malformation, specify'),
)

COWS_MILK = (
    ('boiled', '1. Boiled from cow'),
    ('unboiled', '2. Unboiled from cow'),
    ('store', '3. From store'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

CAUSE_OF_DEATH = (
    ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
    ('Cryptococcal_meningitis_relapse_IRIS',
     'Cryptococcal meningitis relapse/IRIS'),
    (TUBERCULOSIS, 'TB'),
    ('bacteraemia', 'Bacteraemia'),
    ('bacterial_pneumonia', 'Bacterial pneumonia'),
    ('malignancy', 'Malignancy'),
    ('art_toxicity', 'ART toxicity'),
    ('IRIS_non_CM', 'IRIS non-CM'),
    ('diarrhea_wasting', 'Diarrhea/wasting'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other'),
)

SOURCE_OF_DEATH_INFO = (
    ('autopsy', 'Autopsy'),
    ('clinical_records', 'Clinical_records'),
    ('study_staff',
     'Information from study care taker staff prior participant death'),
    ('health_care_provider',
     'Contact with other (non-study) physician/nurse/other health care provider'),
    ('death_certificate', 'Death Certificate'),
    ('relatives_friends', 'Information from participant\'s relatives or friends'),
    ('obituary', 'Obituary'),
    ('pending_information', 'Information requested, still pending'),
    ('no_info', 'No information will ever be available'),
    (OTHER, 'Other, specify'),)

CAUSE_OF_DEATH_CAT = (
    ('hiv_related', 'HIV infection or HIV related diagnosis'),
    ('hiv_unrelated', 'Disease unrelated to HIV'),
    ('study_drug', 'Toxicity from Study Drug'),
    ('non_study_drug', 'Toxicity from non-Study drug'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),)

HOSPITILIZATION_REASONS = (
    ('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'),
    ('respiratory illness, cxr confirmed', 'Respiratory Illness, CXR confirmed'),
    ('respiratory illness, cxr confirmed, bacterial pathogen, specify',
     'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'),
    ('respiratory illness, cxr confirmed, tb or probable tb',
     'Respiratory Illness, CXR confirmed, TB or probable TB'),
    ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'),
    ('diarrhea illness, viral or bacterial pathogen, specify',
     'Diarrhea Illness, viral or bacterial pathogen, specify'),
    ('sepsis(unspecified)', 'Sepsis(unspecified)'),
    ('sepsis, pathogen specified, specify', 'Sepsis, pathogen specified, specify'),
    ('mengitis(unspecified)', 'Mengitis(unspecified)'),
    ('mengitis, pathogen specified, specify',
     'Mengitis, pathogen specified, specify'),
    ('non-infectious reason for hospitalization, specify',
     'Non-infectious reason for hospitalization, specify'),
    (OTHER, 'Other infection, specify'),
)


DX_INFANT = (
    ('Poor weight gain or failure to thrive',
     'Poor weight gain or failure to thrive'),
    ('Severe diarrhea or gastroenteritis',
     'Severe diarrhea or gastroenteritis'),
    ('Pneumonia, suspected (no CXR or microbiologic confirmation)',
     'Pneumonia, suspected (no CXR or microbiologic confirmation)'),
    ('Pneumonia, CXR confirmed, no bacterial pathogen',
     'Pneumonia, CXR confirmed, no bacterial pathogen'),
    ('Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)',
     'Pneumonia, CXR confirmed, bacterial pathogen isolated (specify pathogen)'),
    ('Pulmonary TB, suspected(no CXR or microbiologic confirmation)',
     'Pulmonary TB, suspected(no CXR or microbiologic confirmation)'),
    ('Pulmonary TB, CXR-confirmed (no microbiologic confirmation)',
     'Pulmonary TB, CXR-confirmed (no microbiologic confirmation)'),
    ('Pulmonary TB, smear and/or culture positive',
     'Pulmonary TB, smear and/or culture positive'),
    ('Extrapulmonary TB,suspected (no CXR or microbiologic confirmation)',
     'Extrapulmonary TB,suspected (no CXR or microbiologic confirmation)'),
    ('Bronchiolitis (not bronchitis)', 'Bronchiolitis (not bronchitis)'),
    ('Hepatitis:Drug related',
     'Hepatitis:Drug related (report for Grades 2,3,4)'),
    ('Hepatitis:Traditional medication related',
     'Hepatitis:Traditional medication related'),
    ('Hepatitis:Hepatitis A', 'Hepatitis:Hepatitis A'),
    ('Hepatitis:Hepatitis B', 'Hepatitis:Hepatitis B'),
    ('Hepatitis:Other/Unknown', 'Hepatitis:Other/Unknown'),
    ('Sepsis,unspecified', 'Sepsis,unspecified'),
    ('Sepsis,pathogen specified', 'Sepsis,pathogen specified'),
    ('Meningitis,unspecified', 'Meningitis,unspecified'),
    ('Meningitis pathogen specified', 'Meningitis pathogen specified'),
    ('Otitis media', 'Otitis media'),
    ('Appendicitis', 'Appendicitis'),
    ('Cholecystitis/cholanangitis', 'Cholecystitis/cholanangitis'),
    ('Pancreatitis', 'Pancreatitis'),
    ('Acute Renal Failure',
     'Acute Renal Failure (Record highest creatinine level if creatine tested outside of the study) '),
    ('Anemia',
     'Anemia(Only report grade 3 or 4 anemia based on a lab value drawn outside the study'),
    ('Rash', 'Rash (report for Grades 2,3,4)'),
    ('Trauma/accident', 'Trauma/accident'),
    (
        ('Other abnormallaboratory tests(other than tests listed above '
         'or tests done as part of this study), specify test and result'),
        ('Other abnormallaboratory tests(other than tests listed above or '
         'tests done as part of this study),specify test and result')
    ),
    ('New congenital abnormality not previously identified?,specify',
     'New congenital abnormality not previously identified?,specify and complete "Congenital Anomaly"form'),
    ('Other serious (grade 3 or 4)infection(not listed above),specify',
     'Other serious (grade 3 or 4)infection(not listed above),specify'),
    ('Other serious (grade 3 or 4) non-infectious(not listed above),specify',
     'Other serious (grade 3 or 4)non-infectious(not listed above),specify'),

)

DRUG_ROUTE = (
    ('Intramuscular', 'Intramuscular'),
    ('Intravenous', 'Intravenous'),
    ('Oral', 'Oral'),
    ('Topical', 'Topical'),
    ('Subcutaneous', 'Subcutaneous'),
    ('Intravaginal', 'Intravaginal'),
    ('Rectal', 'Rectal'),
    (OTHER, 'Other'),
)

FACIAL_DEFECT = (
    ('None', 'None'),
    ('Anophthalmia/micro-opthalmia', 'Anophthalmia/micro-opthalmia'),
    ('Cataracts', 'Cataracts'),
    ('Coloboma', 'Coloboma'),
    ('OTHER eye abnormality', 'Other eye abnormality, specify'),
    ('Absence of ear', 'Absence of ear'),
    ('Absence of auditory canal', 'Absence of auditory canal'),
    ('Congenital deafness', 'Congenital deafness'),
    ('Microtia', 'Microtia'),
    ('OTHER ear anomaly', 'Other ear anomaly, specify'),
    ('Brachial cleft cyst, sinus or pit', 'Brachial cleft cyst, sinus or pit'),
    ('OTHER facial malformation', 'Other facial malformation, specify'),
)

FEM_GENITAL_ANOMALY = (
    ('None', 'None'),
    ('Ambinguous genitalia, female', 'Ambinguous genitalia, female'),
    ('Vaginal agenesis', 'Vaginal agenesis'),
    ('Absent or streak ovary', 'Absent or streak ovary'),
    ('Uterine anomaly', 'Uterine anomaly'),
    (OTHER,
     'Other ovarian, fallopian, uterine, cervical, vaginal, or vulvar abnormality'),
)

NAPPY_TYPE = (
    (CLOTH_NAPPY, 'Cloth nappy'),
    ('commercial nappy', 'Commercial Nappy'),
    (OTHER, 'Other, specify'),
    (NOT_APPLICABLE, 'Not applicable'),
)


MOUTH_UP_GASTROINT_DISORDER = (
    ('None', 'None'),
    ('Aglossia', 'Aglossia'),
    ('Macroglossia', 'Macroglossia'),
    ('OTHER mouth, lip, or tongue',
     'Other mouth, lip, or tongue anomaly, specify'),
    ('Esophageal atresia', 'Esophageal atresia'),
    ('Tracheoesphageal fistula', 'Tracheoesphageal fistula'),
    ('Esophageal web', 'Esophageal web'),
    ('Pyloric stenosis', 'Pyloric stenosis'),
    ('OTHER esophageal or stomach',
     'Other esophageal or stomach abnormality, specify'),
)


MALE_GENITAL_ANOMALY = (
    ('None', 'None'),
    ('Hypospadias, specify degree', 'Hypospadias, specify degree'),
    ('Chordee', 'Chordee'),
    ('Ambiguous genitalia, male', 'Ambiguous genitalia, male'),
    ('Undescended testis', 'Undescended testis'),
    (OTHER, 'Other male genital abnormality, specify'),
)

MUSCULOSKELETAL_ABNORMALITY = (
    ('None', 'None'),
    ('Craniosynostosis', 'Craniosynostosis'),
    ('Torticollis', 'Torticollis'),
    ('Congenital scoliosis, lordosis', 'Congenital scoliosis, lordosis'),
    ('Congenital dislocation of hip', 'Congenital dislocation of hip'),
    ('Talipes equinovarus (club feet excluding metatarsus varus)',
     'Talipes equinovarus (club feet excluding metatarsus varus)'),
    ('Funnel chest or pigeon chest (pectus excavatum or carinaturn)',
     'Funnel chest or pigeon chest (pectus excavatum or carinaturn)'),
    ('Polydactyly', 'Polydactyly'),
    ('Syndactyly', 'Syndactyly'),
    ('Other hand malformation, specify', 'Other hand malformation, specify'),
    ('Webbed fingers or toes', 'Webbed fingers or toes'),
    ('Upper limb reduction defect, specify',
     'Upper limb reduction defect, specify'),
    ('Lower limb reduction defect, specify',
     'Lower limb reduction defect, specify'),
    ('Other limb defect, specify', 'Other limb defect, specify'),
    ('Other skull abnormality, specify', 'Other skull abnormality, specify'),
    ('Anthrogryposis', 'Anthrogryposis'),
    ('Vertebral or rib abnormalities, specify',
     'Vertebral or rib abnormalities, specify'),
    ('Osteogenesis imperfecta', 'Osteogenesis imperfecta'),
    ('Dwarfing syndrome, specify', 'Dwarfing syndrome, specify'),
    ('Congenital diaphramatic hernia', 'Congenital diaphramatic hernia'),
    ('Omphalocele', 'Omphalocele'),
    ('Gastroschisis', 'Gastroschisis'),
    (OTHER, 'Other muscular or skeletal abnormality or syndrome, specify'),
)

MEDICATIONS = (
    ('Acyclovir', 'Acyclovir'),
    ('Albuterol', 'Albuterol'),
    ('Albendazol', 'Albendazol'),
    ('Aminophylline', 'Aminophylline'),
    ('Amoxicillin', 'Amoxicillin'),
    ('Ampicillin', 'Ampicillin'),
    ('Antibiotic,unknown(specify 1V or oral)',
     'Antibiotic,unknown(specify 1V or oral)'),
    ('Azithromycin', 'Azithromycin'),
    ('Carbamazepine', 'Carbamazepine'),
    ('Ceftriaxone', 'Ceftriaxone'),
    ('Cotrimoxazole (trimethoprim/sulfamethoxazole)',
     'Cotrimoxazole (trimethoprim/sulfamethoxazole)'),
    ('Cefaclor,cefixime,ceftizoxime,ceftraxone',
     'Cefaclor,cefixime,ceftizoxime,ceftraxone'),
    ('Chloramphenicol', 'Chloramphenicol'),
    ('Ciprofloxacin', 'Ciprofloxacin'),
    ('Clarithromycin', 'Clarithromycin'),
    ('Cloxacillin', 'Cloxacillin'),
    ('Doxycycline', 'Doxycycline'),
    ('Dexamethasone', 'Dexamethasone'),
    ('Diazepam', 'Diazepam'),
    ('Erythromycin', 'Erythromycin'),
    ('Ethambutol', 'Ethambutol'),
    ('Ferrous sulfate', 'Ferrous sulfate'),
    ('Fuconazole', 'Fuconazole'),
    ('Foscarnate', 'Foscarnate'),
    ('Ganciclovir', 'Ganciclovir'),
    ('Gentamicin', 'Gentamicin'),
    ('Hydrocortisone', 'Hydrocortisone'),
    ('Insuline', 'Insuline'),
    ('Isoniazid', 'Isoniazid'),
    ('Ketoconazole', 'Ketoconazole'),
    ('Mebendazole', 'Mebendazole'),
    ('Metronidazole', 'Metronidazole'),
    ('Methylprednisolone', 'Methylprednisolone'),
    ('Nalidixic acid', 'Nalidixic acid'),
    ('Norfloxacin,Ofloxacin', 'Norfloxacin,Ofloxacin'),
    ('Pentamidine', 'Pentamidine'),
    ('Pyridoxine', 'Pyridoxine'),
    ('Phenytoin', 'Phenytoin'),
    ('Prednisolone', 'Prednisolone'),
    ('Pyrazinamide', 'Pyrazinamide'),
    ('Pyrimethamine', 'Pyrimethamine'),
    ('Quinidine', 'Quinidine'),
    ('Red blood cell transfusion', 'Red blood cell transfusion'),
    ('Rifampicin', 'Rifampicin'),
    ('Salbutamol', 'Salbutamol'),
    ('Streptomycin', 'Streptomycin'),
    ('Sulfadiazine', 'Sulfadiazine'),
    ('Terbinafine', 'Terbinafine'),
    ('Tetracycline', 'Tetracycline'),
    ('Theophylline', 'Theophylline'),
    ('Vancomycin', 'Vancomycin'),
    ('Vitamins(iron,B12,Folate)', 'Vitamins(iron,B12,Folate)'),
    ('Traditional medication', 'Traditional Medications'),
    (OTHER, 'Other, specify ...')
)

RENAL_ANOMALY = (
    ('None', 'None'),
    ('Bilateral renal agenesis', 'Bilateral renal agenesis'),
    ('Unilateral renal agenesis or dysplasia',
     'Unilateral renal agenesis or dysplasia'),
    ('Polycystic kidneys', 'Polycystic kidneys'),
    ('Congenital hydronephrosis', 'Congenital hydronephrosis'),
    ('Unilateral stricture, stenosis, or hypoplasia',
     'Unilateral stricture, stenosis, or hypoplasia'),
    ('Duplicated kidney or collecting system',
     'Duplicated kidney or collecting system'),
    ('Horseshoe kidney', 'Horseshoe kidney'),
    ('Exstrophy of bladder', 'Exstrophy of bladder'),
    ('Posterior urethral valves', 'Posterior urethral valves'),
    (OTHER, 'Other renal, ureteral, bladder, urethral abnormality, specify'),
)

ARV_STATUS_WITH_NEVER = (('ARV_STATUS_WITH_NEVER', 'ARV_STATUS_WITH_NEVER'),)
MIN_AGE_OF_CONSENT = 'MIN_AGE_OF_CONSENT'
STOOL_COLLECTION_TIME = (
    (REALTIME, 'Real Time'),
    (BROUGHT, 'Brought by mother'),
    (NOT_APPLICABLE, 'Not applicable'),
)

RESPIRATORY_DEFECT = (
    ('None', 'None'),
    ('Choanal atresia', 'Choanal atresia'),
    ('Agenesis or underdevelopment of nose',
     'Agenesis or underdevelopment of nose'),
    ('Nasal cleft', 'Nasal cleft'),
    ('Single nostril, proboscis', 'Single nostril, proboscis'),
    ('OTHER nasal or sinus abnormality',
     'Other nasal or sinus abnormality, specify'),
    ('Lryngeal web. glottic or subglottic',
     'Lryngeal web. glottic or subglottic'),
    ('Congenital laryngeal stenosis', 'Congenital laryngeal stenosis'),
    ('OTHER laryngeal, tracheal or bronchial anomalies',
     'Other laryngeal, tracheal or bronchial anomalies'),
    ('Single lung cyst', 'Single lung cyst'),
    ('Polycystic lung', 'Polycystic lung'),
    (OTHER, 'Other respiratory anomaly, specify'),
)

LOWER_GASTROINTESTINAL_ABNORMALITY = (
    ('None', 'None'),
    ('Duodenal atresia, stenosis, or absence',
     'Duodenal atresia, stenosis, or absence'),
    ('Jejunal atresis, stenosis, or absence',
     'Jejunal atresis, stenosis, or absence'),
    ('Ileal atresia, stenosis, or absence',
     'Ileal atresia, stenosis, or absence'),
    ('Atresia, stenosis, or absence of large intestine, rectum, or anus',
     'Atresia, stenosis, or absence of large intestine, rectum, or anus'),
    ('Hirschsprung disease', 'Hirschsprung disease'),
    ('OTHER megacolon', 'Other megacolon'),
    ('Liver, pancreas, or gall bladder defect, specify',
     'Liver, pancreas, or gall bladder defect, specify'),
    ('Diaphramtic hernia', 'Diaphramtic hernia'),
    ('OTHER GI anomaly', 'Other GI anomaly, specify'),
)

STOOL_STORED = (
    ('room temp', 'At room temperature (unrefrigerated)'),
    ('refrigerated', 'Refrigerated'),
    (NOT_APPLICABLE, 'Not applicable'),
)

TRISOME_CHROSOMESOME_ABNORMALITY = (
    ('None', 'None'),
    ('Trisomy 21', 'Trisomy 21'),
    ('Trisomy 13', 'Trisomy 13'),
    ('Trisomy 18', 'Trisomy 18'),
    ('OTHER trisomy, specify', 'Other trisomy, specify'),
    ('OTHER non-trisomic chromosome',
     'Other non-trisomic chromosome abnormality, specify'),
)

TIMES_BREASTFED = (
    ('<1 per week', '1. Less than once per week'),
    ('<1 per day, but at least once per week',
     '2. Less than once per day, but at least once per week'),
    ('about 1 per day on most days', '3. About once per day on most days'),
    ('>1 per day, but not for all feedings',
     '4. More than once per day, but not for all feedings'),
    ('For all feedings',
     '5. For all feedings (i.e no formula or other foods or liquids)'),
    (NOT_APPLICABLE, 'Not Applicable'),
)


WATER_USED = (
    ('Water direct from source', 'Water direct from source'),
    ('Water boiled immediately before use',
     'Water boiled immediately before use'),
    ('Water boiled earlier and then stored',
     'Water boiled earlier and then stored'),
    ('Specifically treated water', 'Specifically treated water'),
    (OTHER, 'Other (specify)'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

REASONS_VACCINES_MISSED = (
    ('missed scheduled vaccination', 'Mother or Caregiver has not yet taken infant '
        'to clinic for this scheduled vaccination'),
    ('caregiver declines vaccination',
     'Mother or Caregiver declines this vaccicnation'),
    ('no stock', 'Stock out at clinic'),
    (OTHER, 'Other, specify'),
)

SKIN_ABNORMALITY = (
    ('None', 'None'),
    ('Icthyosis', 'Icthyosis'),
    ('Ectodermal dysplasia', 'Ectodermal dysplasia'),
    (OTHER, 'Other skin abnormality, specify'),
)

OFF_STUDY_REASON = [
    ('not_18'.format(MIN_AGE_OF_CONSENT),
     ' Mother of infant found to be less than {} years of age'.format(MIN_AGE_OF_CONSENT)),
    ('not_citizen', ' Mother found not be a citizen of Botswana'),
    ('moved',
     ' Subject will be moving out of study area or unable to stay in study area'),
    ('lost_no_contact', ' Lost to follow-up, unable to locate'),
    ('lost_contacted',
     ' Lost to follow-up, contacted but did not come to study clinic'),
    ('withdrew_by_mother',
     ' Mother changed mind and withdrew consent'),
    ('withdrew_by_father',
     ' Father of baby did not want infant to participate and participant withdrew consent'),
    ('withdrew_by_family',
     ' Other family member did not want mother/infant to participate and participant withdrew consent'),
    ('hiv_pos', ' Infant found to be HIV-infected'),
    ('ill',
     ' Infant diagnosed with medical condition making survival to 12 months unlikely'),
    ('complete',
     (' Completion of protocol required period of time for observation (see Study '
      'Protocol for definition of Completion.) [skip to end of form]')),
    ('death',
     (' Participant death (complete the DEATH REPORT FORM AF005) (For '
      'EAE Reporting requirements see EAE Reporting Manual)')),
    (OTHER, ' Other'),
]

IMMUNIZATIONS = (
    ('Vitamin_A', 'Vitamin A'),
    ('BCG', 'BCG'),
    ('Hepatitis_B', 'Hepatitis B'),
    ('DPT', 'DPT (Diphtheria, Pertussis and Tetanus)'),
    ('Haemophilus_influenza', 'Haemophilus Influenza B Vaccine'),
    ('PCV_Vaccine', 'PCV Vaccine (Pneumonia Conjugated Vaccine)'),
    ('Polio', 'Polio'),
    ('Rotavirus', 'Rotavirus'),
    ('inactivated_polio_vaccine', 'Inactivated-Polio Vaccine'),
    ('Measles', 'Measles'),
    ('Pentavalent',
     'Pentavalent Vaccine (Contains DPT, Hepatitis B and Haemophilus Influenza B Vaccine)'),
    ('diptheria_tetanus', 'Diptheria and Tetanus'))

INFANT_VACCINATIONS = (
    ('Vitamin_A', 'Vitamin A'),
    ('BCG', 'BCG'),
    ('Hepatitis_B', 'Hepatitis B'),
    ('DPT', 'DPT (Diphtheria, Pertussis and Tetanus)'),
    ('Haemophilus_influenza', 'Haemophilus Influenza B Vaccine'),
    ('PCV_Vaccine', 'PCV Vaccine (Pneumonia Conjugated Vaccine)'),
    ('Polio', 'Polio'),
    ('inactivated_polio_vaccine', 'Inactivated-Polio Vaccine'),
    ('Rotavirus', 'Rotavirus'),
    ('Measles', 'Measles'),
    ('Pentavalent',
     'Pentavalent Vaccine (Contains DPT, Hepatitis B and Haemophilus Influenza B Vaccine)'),
    ('diphtheria_tetanus', 'Diphtheria and Tetanus'))

INFANT_AGE_VACCINE_GIVEN = (
    ('At Birth', 'At Birth'),
    ('After Birth', 'After Birth'),
    ('2', '2 months'),
    ('3', '3 months'),
    ('4', '4 months'),
    ('4-6', '4-6 months'),
    ('6-11', '6-11 months'),
    ('9', '9 months'),
    ('9-12', '9-12 months'),
    ('12-17', '12-17 months'),
    ('18', '18 months'),
    ('18-29', '18-29 months'),
    ('24-29', '24-29 months'),
    ('30-35', '30-35 months'),
    ('36-41', '36-41 months'),
    ('42-47', '42-47 months'),
    ('48-53', '48-53 months'),
    ('54-59', '54-59 months'))

ARV_MODIFICATION_REASON = (
    ('Initial dose', 'Initial dose'),
    ('Never started', 'Never started'),
    ('Toxicity decreased_resolved', 'Toxicity decreased/resolved'),
    ('Completed PMTCT intervention', 'Completed PMTCT intervention'),
    ('Completed postpartum tail', 'Completed postpartum "tail"'),
    ('Scheduled dose increase', 'Scheduled dose increase'),
    ('Confirmed infant HIV infection, ending study drug',
     'Confirmed infant HIV infection, ending study drug'),
    ('completed protocol',
     'Completion of protocol-required period of study treatment'),
    ('HAART not available', 'HAART not available'),
    ('Anemia', 'Anemia'),
    ('Bleeding', 'Bleeding'),
    ('CNS symptoms', 'CNS symptoms (sleep, psych, etc)'),
    ('Diarrhea', 'Diarrhea'),
    ('Fatigue', 'Fatigue'),
    ('Headache', 'Headache'),
    ('Hepatotoxicity', 'Hepatotoxicity'),
    ('Nausea', 'Nausea'),
    ('Neutropenia', 'Neutropenia'),
    ('Thrombocytopenia', 'Thrombocytopenia'),
    ('Vomiting', 'Vomiting'),
    ('Rash', 'Rash'),
    ('Rash resolved', 'Rash resolved'),
    ('Neuropathy', 'Neuropathy'),
    ('Hypersensitivity_allergic reaction',
     'Hypersensitivity / allergic reaction'),
    ('Pancreatitis', 'Pancreatitis'),
    ('Lactic Acidiosis', 'Lactic Acidiosis'),
    ('Pancytopenia', 'Pancytopenia'),
    ('Virologic failure', 'Virologic failure'),
    ('Immunologic failure', 'Immunologic failure(CD4)'),
    ('Clinical failure', 'Clinical failure'),
    ('Clinician request',
     'Clinician request, other reason (including convenience)'),
    ('Subject request',
     'Subject request, other reason (including convenience)'),
    ('Non-adherence with clinic visits', 'Non-adherence with clinic visits'),
    ('Non-adherence with ARVs', 'Non-adherence with ARVs'),
    ('Death', 'Death'),
    ('OTHER', 'Other'),
)

DOSE_STATUS = (
    ('New', 'New'),
    ('Permanently discontinued', 'Permanently discontinued'),
    ('Temporarily held', 'Temporarily held'),
    ('Dose modified', 'Dose modified'),
    ('Resumed', 'Resumed'),
    ('Not initiated', 'Not initiated'),
)

ARV_DRUG_LIST = (
    ('Nevirapine', 'NVP'),
    ('Kaletra', 'KAL'),
    ('Aluvia', 'ALU'),
    ('Truvada', 'TRV'),
    ('Tenoforvir', 'TDF',),
    ('Zidovudine', 'AZT'),
    ('Lamivudine', '3TC'),
    ('Efavirenz', 'EFV'),
    ('Didanosine', 'DDI'),
    ('Stavudine', 'D4T'),
    ('Nelfinavir', 'NFV'),
    ('Abacavir', 'ABC'),
    ('Combivir', 'CBV'),
    ('Ritonavir', 'RTV'),
    ('Trizivir', 'TZV'),
    ('Raltegravir', 'RAL'),
    ('Saquinavir,soft gel capsule', 'FOR'),
    ('Saquinavir,hard capsule', 'INV'),
    ('Kaletra or Aluvia', 'KAL or ALU'),
    ('Atripla', 'ATR'),
    ('HAART,unknown', 'HAART,unknown'),
)

SOLID_FOODS = (
    ('Grains, roots and tubers', 'Grains, roots and tubers'),
    ('Legumes and nuts', 'Legumes and nuts'),
    (' Dairy products (milk, yogurt, cheese)',
     ' Dairy products (milk, yogurt, cheese)'),
    ('Flesh foods', 'Flesh foods (meat, fish, poultry and liver/organ meat)'),
    ('Eggs', 'Eggs'),
    ('Vitamin A rich fruts and vegetables (carrots)',
     'Vitamin A rich fruts and vegetables (carrots)'),
    ('Other fruits and vegetables', 'Other fruits and vegetables'),
    ('Other', 'Other')

)

FEEDING_CHOICES = (
    (BREASTFEED_ONLY, 'Breastfeed only'),
    ('Formula feeding only', 'Formula feeding only'),
    ('Both breastfeeding and formula feeding',
     'Both breastfeeding and formula feeding'),
    ('Medical complications: Infant did not feed',
     'Medical complications: Infant did not feed'),
)

OTHER_DEFECT = (
    ('None', 'None'),
    (OTHER, 'Other defect/syndrome not already reported, specify'),
)

VISIT_REASON = [
    (SCHEDULED, 'Scheduled visit/contact'),
    (MISSED_VISIT, 'Missed Scheduled visit'),
    (UNSCHEDULED,
     'Unscheduled visit at which lab samples or data are being submitted'),
    (LOST_VISIT, 'Lost to follow-up (use only when taking subject off study)'),
    (FAILED_ELIGIBILITY, 'Subject failed enrollment eligibility'),
    (COMPLETED_PROTOCOL_VISIT, 'Subject has completed the study')]
