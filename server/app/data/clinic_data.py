"""
Clinic Management Central Dataset.
Provides complete dummy records for MongoDB storage and LangChain AI retrieval.
Synchronized with Frontend UI & Operational Statistics.
"""

CLINIC_OVERVIEW = {
    "name": "PulseClinic Healthcare Center",
    "tagline": "Advanced Multi-Specialty Outpatient Clinic",
    "address": "450 Medical Plaza Blvd, Suite 100, New York, NY 10016",
    "phone": "+1 (800) 555-PULSE",
    "email": "contact@pulseclinic.health",
    "current_month": "August 2026",
    "today_date": "Saturday, August 29, 2026",
    "stats": {
        "total_patients": 1284,
        "monthly_revenue": 32450,
        "target_revenue": 35000,
        "today_appointments": 42,
        "today_completed": 34,
        "today_waiting": 3,
        "today_in_consult": 1,
        "today_scheduled": 4,
        "doctors_on_duty": 14,
        "total_doctors": 18,
        "pending_lab_reports": 9,
        "no_show_rate_percent": 4.2
    }
}

CLINIC_PATIENTS = [
    {
        "id": "P-1001",
        "name": "Robert Fox",
        "age": 52,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 432-8901",
        "email": "robert.fox@example.com",
        "condition": "Hypertension Stage 2",
        "allergies": [
            "Penicillin"
        ],
        "chronic_diseases": [
            "Essential Hypertension"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 14,
        "insurance_provider": "BlueCross BlueShield",
        "attendance_status": "regular",
        "address": "742 Evergreen Terrace, Brooklyn, NY"
    },
    {
        "id": "P-1002",
        "name": "Sophia Martinez",
        "age": 29,
        "gender": "Female",
        "blood_group": "A+",
        "phone": "+1 (555) 789-0123",
        "email": "sophia.m@example.com",
        "condition": "Chronic Migraine",
        "allergies": [
            "Sulfa Drugs",
            "Aspirin"
        ],
        "chronic_diseases": [
            "Migraine with Aura"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 6,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "128 W 84th St, Apt 4B, Manhattan, NY"
    },
    {
        "id": "P-1003",
        "name": "Marcus Vance",
        "age": 41,
        "gender": "Male",
        "blood_group": "B+",
        "phone": "+1 (555) 321-6549",
        "email": "m.vance@techcorp.io",
        "condition": "Arrhythmia Investigation",
        "allergies": [],
        "chronic_diseases": [
            "Mild Asthma"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 4,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "55 Water St, Jersey City, NJ"
    },
    {
        "id": "P-1004",
        "name": "Emma Watson",
        "age": 6,
        "gender": "Female",
        "blood_group": "O-",
        "phone": "+1 (555) 876-5432",
        "email": "watson.parents@example.com",
        "condition": "Routine Pediatric Check & MMR Booster",
        "allergies": [
            "Peanuts (Mild)"
        ],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 8,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "310 E 46th St, New York, NY"
    },
    {
        "id": "P-1005",
        "name": "David Miller",
        "age": 38,
        "gender": "Male",
        "blood_group": "AB+",
        "phone": "+1 (555) 654-9870",
        "email": "david.miller@builder.com",
        "condition": "Right Meniscus Tear",
        "allergies": [
            "Ibuprofen"
        ],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 3,
        "insurance_provider": "Self-Pay",
        "attendance_status": "regular",
        "address": "94 Riverside Dr, New York, NY"
    },
    {
        "id": "P-1006",
        "name": "Clara Oswald",
        "age": 33,
        "gender": "Female",
        "blood_group": "A-",
        "phone": "+1 (555) 987-1234",
        "email": "clara.oswald@academy.edu",
        "condition": "Hypothyroidism Monitoring",
        "allergies": [],
        "chronic_diseases": [
            "Hypothyroidism"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 9,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "12 Bishop St, Queens, NY"
    },
    {
        "id": "P-1007",
        "name": "Brenda Diaz",
        "age": 47,
        "gender": "Female",
        "blood_group": "O+",
        "phone": "+1 (555) 902-3341",
        "email": "brenda.diaz@mail.com",
        "condition": "Severe Lower Back Pain",
        "allergies": [
            "Codeine"
        ],
        "chronic_diseases": [
            "Lumbar Spondylosis"
        ],
        "last_visit": "2026-08-20",
        "total_visits": 5,
        "insurance_provider": "Medicare",
        "attendance_status": "no-show",
        "address": "88 Lincoln Blvd, Bronx, NY"
    },
    {
        "id": "P-1008",
        "name": "James Wilson",
        "age": 61,
        "gender": "Male",
        "blood_group": "B-",
        "phone": "+1 (555) 234-9081",
        "email": "jwilson61@verizon.net",
        "condition": "Post-Op Distal Radius Fracture",
        "allergies": [
            "Latex"
        ],
        "chronic_diseases": [
            "Type 2 Diabetes"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 11,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "410 Madison Ave, New York, NY"
    },
    {
        "id": "P-1009",
        "name": "Mark Spencer",
        "age": 44,
        "gender": "Male",
        "blood_group": "A+",
        "phone": "+1 (555) 771-4492",
        "email": "mark.spencer@corp.com",
        "condition": "Chronic Acid Reflux / GERD",
        "allergies": [],
        "chronic_diseases": [
            "GERD"
        ],
        "last_visit": "2026-07-15",
        "total_visits": 2,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "no-show",
        "address": "220 Park Ave South, New York, NY"
    },
    {
        "id": "P-1010",
        "name": "Hannah Abbott",
        "age": 24,
        "gender": "Female",
        "blood_group": "O+",
        "phone": "+1 (555) 345-6789",
        "email": "hannah.abbott@botanics.org",
        "condition": "Seasonal Allergic Rhinitis",
        "allergies": [
            "Pollen",
            "Dust Mites"
        ],
        "chronic_diseases": [],
        "last_visit": "2026-08-25",
        "total_visits": 4,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "65 Hudson Yards, New York, NY"
    },
    {
        "id": "P-1011",
        "name": "Jonathan Archer",
        "age": 58,
        "gender": "Male",
        "blood_group": "AB-",
        "phone": "+1 (555) 882-9910",
        "email": "jarcher@enterprise.org",
        "condition": "Elevated Cholesterol & Statin Review",
        "allergies": [],
        "chronic_diseases": [
            "Hyperlipidemia"
        ],
        "last_visit": "2026-08-18",
        "total_visits": 7,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "17 Battery Pl, New York, NY"
    },
    {
        "id": "P-1012",
        "name": "Angela Martin",
        "age": 39,
        "gender": "Female",
        "blood_group": "O+",
        "phone": "+1 (555) 662-8819",
        "email": "angela.martin@dunder.com",
        "condition": "Persistent Vertigo & Inner Ear Check",
        "allergies": [
            "Erythromycin"
        ],
        "chronic_diseases": [
            "Benign Paroxysmal Positional Vertigo"
        ],
        "last_visit": "2026-08-12",
        "total_visits": 3,
        "insurance_provider": "Cigna",
        "attendance_status": "no-show",
        "address": "1720 Clay Ave, Scranton, PA / NY Branch"
    },
    {
        "id": "P-1013",
        "name": "Lucas Scott",
        "age": 19,
        "gender": "Male",
        "blood_group": "A+",
        "phone": "+1 (555) 123-9988",
        "email": "lucas.scott@college.edu",
        "condition": "Sports Concussion Baseline Assessment",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 1,
        "insurance_provider": "StudentCare Health",
        "attendance_status": "new",
        "address": "Washington Square Park Dorms, NY"
    },
    {
        "id": "P-1014",
        "name": "Kevin Malone",
        "age": 46,
        "gender": "Male",
        "blood_group": "B+",
        "phone": "+1 (555) 551-7723",
        "email": "kevin.chili@scranton.net",
        "condition": "Type 2 Diabetes Glycemic Review",
        "allergies": [
            "Shellfish"
        ],
        "chronic_diseases": [
            "Type 2 Diabetes",
            "Obesity"
        ],
        "last_visit": "2026-06-30",
        "total_visits": 8,
        "insurance_provider": "Self-Pay",
        "attendance_status": "no-show",
        "address": "420 Grand St, Manhattan, NY"
    },
    {
        "id": "P-1015",
        "name": "Eleanor Vance",
        "age": 68,
        "gender": "Female",
        "blood_group": "O-",
        "phone": "+1 (555) 334-1188",
        "email": "eleanor.v@grand.org",
        "condition": "Osteoarthritis Knees & Hip Check",
        "allergies": [
            "Sulfa"
        ],
        "chronic_diseases": [
            "Osteoarthritis",
            "Mild Osteopenia"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 18,
        "insurance_provider": "Medicare Part B",
        "attendance_status": "regular",
        "address": "15 Central Park West, New York, NY"
    },
    {
        "id": "P-1016",
        "name": "Tariq Mansoor",
        "age": 35,
        "gender": "Male",
        "blood_group": "AB+",
        "phone": "+1 (555) 772-0044",
        "email": "tariq.mansoor@global.com",
        "condition": "Dermatitis & Eczema Flare-up",
        "allergies": [
            "Fragrances",
            "Nickel"
        ],
        "chronic_diseases": [
            "Atopic Dermatitis"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 5,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "800 5th Ave, New York, NY"
    },
    {
        "id": "P-1017",
        "name": "Sarah Connor",
        "age": 48,
        "gender": "Female",
        "blood_group": "A+",
        "phone": "+1 (555) 881-2201",
        "email": "sarah.connor@example.com",
        "condition": "Hypertension & Stress",
        "allergies": [
            "Penicillin"
        ],
        "chronic_diseases": [
            "Hypertension"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 3,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "100 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1018",
        "name": "John Matrix",
        "age": 42,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2202",
        "email": "john.matrix@example.com",
        "condition": "Routine Health Checkup",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 4,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "115 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1019",
        "name": "Ellen Ripley",
        "age": 36,
        "gender": "Female",
        "blood_group": "B+",
        "phone": "+1 (555) 881-2203",
        "email": "ellen.ripley@example.com",
        "condition": "Thyroid Profile Follow-up",
        "allergies": [],
        "chronic_diseases": [
            "Hypothyroidism"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 5,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "130 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1020",
        "name": "Arthur Dent",
        "age": 34,
        "gender": "Male",
        "blood_group": "AB+",
        "phone": "+1 (555) 881-2204",
        "email": "arthur.dent@example.com",
        "condition": "Chronic Insomnia & Anxiety",
        "allergies": [
            "Aspirin"
        ],
        "chronic_diseases": [
            "Generalized Anxiety"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 6,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "145 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1021",
        "name": "Ford Prefect",
        "age": 37,
        "gender": "Male",
        "blood_group": "O-",
        "phone": "+1 (555) 881-2205",
        "email": "ford.prefect@example.com",
        "condition": "Acute Gastritis Evaluation",
        "allergies": [],
        "chronic_diseases": [
            "Gastritis"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 7,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "160 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1022",
        "name": "Trillian McMillan",
        "age": 29,
        "gender": "Female",
        "blood_group": "A-",
        "phone": "+1 (555) 881-2206",
        "email": "trillian.mcmillan@example.com",
        "condition": "Allergy Skin Prick Testing",
        "allergies": [
            "Dust Mites"
        ],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 8,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "175 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1023",
        "name": "Marty McFly",
        "age": 21,
        "gender": "Male",
        "blood_group": "B-",
        "phone": "+1 (555) 881-2207",
        "email": "marty.mcfly@example.com",
        "condition": "Ankle Sprain & Ultrasound",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 9,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "190 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1024",
        "name": "Doc Brown",
        "age": 65,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2208",
        "email": "doc.brown@example.com",
        "condition": "Cardiovascular Holter Review",
        "allergies": [],
        "chronic_diseases": [
            "Coronary Artery Disease"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 10,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "205 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1025",
        "name": "Diana Prince",
        "age": 31,
        "gender": "Female",
        "blood_group": "A+",
        "phone": "+1 (555) 881-2209",
        "email": "diana.prince@example.com",
        "condition": "Annual Well-Woman Exam",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 3,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "220 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1026",
        "name": "Bruce Wayne",
        "age": 45,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2210",
        "email": "bruce.wayne@example.com",
        "condition": "Rotator Cuff Tendinitis",
        "allergies": [
            "Codeine"
        ],
        "chronic_diseases": [
            "Chronic Lumbar Strain"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 4,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "235 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1027",
        "name": "Clark Kent",
        "age": 38,
        "gender": "Male",
        "blood_group": "AB+",
        "phone": "+1 (555) 881-2211",
        "email": "clark.kent@example.com",
        "condition": "Annual Executive Physical",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 5,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "250 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1028",
        "name": "Lois Lane",
        "age": 35,
        "gender": "Female",
        "blood_group": "A+",
        "phone": "+1 (555) 881-2212",
        "email": "lois.lane@example.com",
        "condition": "Migraine Prophylaxis Review",
        "allergies": [
            "Sulfa"
        ],
        "chronic_diseases": [
            "Chronic Migraine"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 6,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "265 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1029",
        "name": "Barry Allen",
        "age": 26,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2213",
        "email": "barry.allen@example.com",
        "condition": "Metabolic Syndrome Screening",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 7,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "280 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1030",
        "name": "Hal Jordan",
        "age": 39,
        "gender": "Male",
        "blood_group": "B+",
        "phone": "+1 (555) 881-2214",
        "email": "hal.jordan@example.com",
        "condition": "Visual Field & Ocular Pressure",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 8,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "295 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1031",
        "name": "Oliver Queen",
        "age": 40,
        "gender": "Male",
        "blood_group": "AB-",
        "phone": "+1 (555) 881-2215",
        "email": "oliver.queen@example.com",
        "condition": "Shoulder Impingement Therapy",
        "allergies": [],
        "chronic_diseases": [
            "Rotator Cuff Tendinopathy"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 9,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "310 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1032",
        "name": "Dinah Lance",
        "age": 32,
        "gender": "Female",
        "blood_group": "O-",
        "phone": "+1 (555) 881-2216",
        "email": "dinah.lance@example.com",
        "condition": "Vocal Cord Laryngoscopy Followup",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 10,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "325 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1033",
        "name": "Tony Stark",
        "age": 49,
        "gender": "Male",
        "blood_group": "A+",
        "phone": "+1 (555) 881-2217",
        "email": "tony.stark@example.com",
        "condition": "Cardiac Stent Routine Review",
        "allergies": [
            "Penicillin"
        ],
        "chronic_diseases": [
            "Coronary Artery Disease"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 3,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "340 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1034",
        "name": "Pepper Potts",
        "age": 43,
        "gender": "Female",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2218",
        "email": "pepper.potts@example.com",
        "condition": "Preventive Wellness Screening",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 4,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "355 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1035",
        "name": "Steve Rogers",
        "age": 72,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2219",
        "email": "steve.rogers@example.com",
        "condition": "Geriatric Joint Mobility Check",
        "allergies": [],
        "chronic_diseases": [
            "Osteoarthritis"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 5,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "370 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1036",
        "name": "Natasha Romanoff",
        "age": 34,
        "gender": "Female",
        "blood_group": "B+",
        "phone": "+1 (555) 881-2220",
        "email": "natasha.romanoff@example.com",
        "condition": "Physical Therapy Clearance",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 6,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "385 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1037",
        "name": "Bruce Banner",
        "age": 47,
        "gender": "Male",
        "blood_group": "AB+",
        "phone": "+1 (555) 881-2221",
        "email": "bruce.banner@example.com",
        "condition": "Endocrine Stress Panel",
        "allergies": [],
        "chronic_diseases": [
            "Hypertension"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 7,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "400 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1038",
        "name": "Wanda Maximoff",
        "age": 28,
        "gender": "Female",
        "blood_group": "A-",
        "phone": "+1 (555) 881-2222",
        "email": "wanda.maximoff@example.com",
        "condition": "Neurological EEG Consultation",
        "allergies": [
            "Latex"
        ],
        "chronic_diseases": [
            "Migraine"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 8,
        "insurance_provider": "Aetna",
        "attendance_status": "regular",
        "address": "415 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1039",
        "name": "Stephen Strange",
        "age": 46,
        "gender": "Male",
        "blood_group": "B-",
        "phone": "+1 (555) 881-2223",
        "email": "stephen.strange@example.com",
        "condition": "Bilateral Carpal Tunnel Review",
        "allergies": [],
        "chronic_diseases": [
            "Peripheral Neuropathy"
        ],
        "last_visit": "2026-08-29",
        "total_visits": 9,
        "insurance_provider": "UnitedHealth",
        "attendance_status": "regular",
        "address": "430 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1040",
        "name": "Peter Parker",
        "age": 20,
        "gender": "Male",
        "blood_group": "O+",
        "phone": "+1 (555) 881-2224",
        "email": "peter.parker@example.com",
        "condition": "Sports Physical & ECG",
        "allergies": [
            "Spider Venom"
        ],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 10,
        "insurance_provider": "Cigna",
        "attendance_status": "regular",
        "address": "445 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1041",
        "name": "Miles Morales",
        "age": 17,
        "gender": "Male",
        "blood_group": "A+",
        "phone": "+1 (555) 881-2225",
        "email": "miles.morales@example.com",
        "condition": "Pediatric Adolescent Checkup",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 3,
        "insurance_provider": "Medicare",
        "attendance_status": "regular",
        "address": "460 Lexington Ave, New York, NY"
    },
    {
        "id": "P-1042",
        "name": "Gwen Stacy",
        "age": 19,
        "gender": "Female",
        "blood_group": "O-",
        "phone": "+1 (555) 881-2226",
        "email": "gwen.stacy@example.com",
        "condition": "Audiology Screening",
        "allergies": [],
        "chronic_diseases": [],
        "last_visit": "2026-08-29",
        "total_visits": 4,
        "insurance_provider": "BlueCross",
        "attendance_status": "regular",
        "address": "475 Lexington Ave, New York, NY"
    }
]

CLINIC_DOCTORS = [
    {
        "id": "doc-1",
        "name": "Dr. Sarah Jenkins",
        "specialty": "Cardiology",
        "room": "Suite 302",
        "status": "on_duty",
        "avatar": "SJ",
        "patients_today": 12,
        "experience": "14 years",
        "phone": "+1 (555) 019-2831"
    },
    {
        "id": "doc-2",
        "name": "Dr. Alex Rivera",
        "specialty": "Pediatrics",
        "room": "Suite 105",
        "status": "on_duty",
        "avatar": "AR",
        "patients_today": 10,
        "experience": "9 years",
        "phone": "+1 (555) 019-2832"
    },
    {
        "id": "doc-3",
        "name": "Dr. Emily Chen",
        "specialty": "General Medicine",
        "room": "Suite 201",
        "status": "on_duty",
        "avatar": "EC",
        "patients_today": 14,
        "experience": "11 years",
        "phone": "+1 (555) 019-2833"
    },
    {
        "id": "doc-4",
        "name": "Dr. Michael Vance",
        "specialty": "Orthopedics",
        "room": "Suite 410",
        "status": "on_duty",
        "avatar": "MV",
        "patients_today": 8,
        "experience": "16 years",
        "phone": "+1 (555) 019-2834"
    },
    {
        "id": "doc-5",
        "name": "Dr. Lisa Wong",
        "specialty": "Dermatology",
        "room": "Suite 108",
        "status": "on_duty",
        "avatar": "LW",
        "patients_today": 9,
        "experience": "8 years",
        "phone": "+1 (555) 019-2835"
    },
    {
        "id": "doc-6",
        "name": "Dr. Gregory House",
        "specialty": "Diagnostic Medicine",
        "room": "Suite 500",
        "status": "break",
        "avatar": "GH",
        "patients_today": 4,
        "experience": "22 years",
        "phone": "+1 (555) 019-2836"
    },
    {
        "id": "doc-7",
        "name": "Dr. James Wilson",
        "specialty": "Oncology",
        "room": "Suite 305",
        "status": "on_duty",
        "avatar": "JW",
        "patients_today": 7,
        "experience": "15 years",
        "phone": "+1 (555) 019-2837"
    },
    {
        "id": "doc-8",
        "name": "Dr. Allison Cameron",
        "specialty": "Immunology & Allergy",
        "room": "Suite 210",
        "status": "on_duty",
        "avatar": "AC",
        "patients_today": 8,
        "experience": "10 years",
        "phone": "+1 (555) 019-2838"
    },
    {
        "id": "doc-9",
        "name": "Dr. Robert Chase",
        "specialty": "Intensive Care & Surgery",
        "room": "Suite 315",
        "status": "on_duty",
        "avatar": "RC",
        "patients_today": 6,
        "experience": "12 years",
        "phone": "+1 (555) 019-2839"
    },
    {
        "id": "doc-10",
        "name": "Dr. Eric Foreman",
        "specialty": "Neurology",
        "room": "Suite 402",
        "status": "on_duty",
        "avatar": "EF",
        "patients_today": 9,
        "experience": "13 years",
        "phone": "+1 (555) 019-2840"
    },
    {
        "id": "doc-11",
        "name": "Dr. Chris Taub",
        "specialty": "Plastic & Reconstructive Surgery",
        "room": "Suite 112",
        "status": "on_duty",
        "avatar": "CT",
        "patients_today": 5,
        "experience": "18 years",
        "phone": "+1 (555) 019-2841"
    },
    {
        "id": "doc-12",
        "name": "Dr. Remy Hadley",
        "specialty": "Internal Medicine",
        "room": "Suite 204",
        "status": "on_duty",
        "avatar": "RH",
        "patients_today": 8,
        "experience": "8 years",
        "phone": "+1 (555) 019-2842"
    },
    {
        "id": "doc-13",
        "name": "Dr. Lawrence Kutner",
        "specialty": "Sports Medicine",
        "room": "Suite 415",
        "status": "on_duty",
        "avatar": "LK",
        "patients_today": 7,
        "experience": "7 years",
        "phone": "+1 (555) 019-2843"
    },
    {
        "id": "doc-14",
        "name": "Dr. Martha Masters",
        "specialty": "General Practice",
        "room": "Suite 102",
        "status": "on_duty",
        "avatar": "MM",
        "patients_today": 6,
        "experience": "5 years",
        "phone": "+1 (555) 019-2844"
    },
    {
        "id": "doc-15",
        "name": "Dr. Chi Park",
        "specialty": "Neurology & Rehab",
        "room": "Suite 404",
        "status": "on_duty",
        "avatar": "CP",
        "patients_today": 5,
        "experience": "6 years",
        "phone": "+1 (555) 019-2845"
    },
    {
        "id": "doc-16",
        "name": "Dr. Jessica Adams",
        "specialty": "Family Medicine",
        "room": "Suite 106",
        "status": "break",
        "avatar": "JA",
        "patients_today": 4,
        "experience": "6 years",
        "phone": "+1 (555) 019-2846"
    },
    {
        "id": "doc-17",
        "name": "Dr. Amber Volakis",
        "specialty": "Radiology",
        "room": "Suite 510",
        "status": "off_duty",
        "avatar": "AV",
        "patients_today": 0,
        "experience": "9 years",
        "phone": "+1 (555) 019-2847"
    },
    {
        "id": "doc-18",
        "name": "Dr. Jeffrey Cole",
        "specialty": "Medical Genetics",
        "room": "Suite 512",
        "status": "off_duty",
        "avatar": "JC",
        "patients_today": 0,
        "experience": "11 years",
        "phone": "+1 (555) 019-2848"
    }
]

CLINIC_APPOINTMENTS = [
    {
        "id": "apt-101",
        "token": "T-041",
        "appointment_time": "08:30 AM",
        "date": "2026-08-29",
        "patient_id": "P-1015",
        "patient_name": "Eleanor Vance",
        "phone": "+1 (555) 334-1188",
        "doctor_id": "doc-4",
        "doctor_name": "Dr. Michael Vance",
        "department": "Orthopedics",
        "room": "Suite 410",
        "visit_type": "Joint Injections & Follow-up",
        "status": "completed",
        "completed_time": "09:05 AM",
        "diagnosis": "Administered Cortisone left knee. Tolerated well.",
        "fee": 180,
        "billing_status": "paid"
    },
    {
        "id": "apt-102",
        "token": "T-042",
        "appointment_time": "09:15 AM",
        "date": "2026-08-29",
        "patient_id": "P-1001",
        "patient_name": "Robert Fox",
        "phone": "+1 (555) 432-8901",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Hypertension Follow-up",
        "status": "completed",
        "completed_time": "09:40 AM",
        "diagnosis": "BP 128/82. Controlled on current ACE inhibitor.",
        "fee": 120,
        "billing_status": "paid"
    },
    {
        "id": "apt-103",
        "token": "T-043",
        "appointment_time": "09:45 AM",
        "date": "2026-08-29",
        "patient_id": "P-1002",
        "patient_name": "Sophia Martinez",
        "phone": "+1 (555) 789-0123",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Acute Migraine Check",
        "status": "completed",
        "completed_time": "10:15 AM",
        "diagnosis": "Tension-type migraine exacerbation. Prescribed rest & Sumatriptan.",
        "fee": 95,
        "billing_status": "pending"
    },
    {
        "id": "apt-104",
        "token": "T-010",
        "appointment_time": "08:00 AM",
        "date": "2026-08-29",
        "patient_id": "P-1017",
        "patient_name": "Sarah Connor",
        "phone": "+1 (555) 881-2201",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:200 AM",
        "diagnosis": "Routine consultation for Hypertension & Stress. Vitals stable.",
        "fee": 110,
        "billing_status": "pending"
    },
    {
        "id": "apt-105",
        "token": "T-011",
        "appointment_time": "08:15 AM",
        "date": "2026-08-29",
        "patient_id": "P-1018",
        "patient_name": "John Matrix",
        "phone": "+1 (555) 881-2202",
        "doctor_id": "doc-2",
        "doctor_name": "Dr. Alex Rivera",
        "department": "Pediatrics",
        "room": "Suite 105",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:215 AM",
        "diagnosis": "Routine consultation for Routine Health Checkup. Vitals stable.",
        "fee": 115,
        "billing_status": "paid"
    },
    {
        "id": "apt-106",
        "token": "T-012",
        "appointment_time": "08:20 AM",
        "date": "2026-08-29",
        "patient_id": "P-1019",
        "patient_name": "Ellen Ripley",
        "phone": "+1 (555) 881-2203",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:220 AM",
        "diagnosis": "Routine consultation for Thyroid Profile Follow-up. Vitals stable.",
        "fee": 120,
        "billing_status": "paid"
    },
    {
        "id": "apt-107",
        "token": "T-013",
        "appointment_time": "08:40 AM",
        "date": "2026-08-29",
        "patient_id": "P-1020",
        "patient_name": "Arthur Dent",
        "phone": "+1 (555) 881-2204",
        "doctor_id": "doc-4",
        "doctor_name": "Dr. Michael Vance",
        "department": "Orthopedics",
        "room": "Suite 410",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:240 AM",
        "diagnosis": "Routine consultation for Chronic Insomnia & Anxiety. Vitals stable.",
        "fee": 125,
        "billing_status": "paid"
    },
    {
        "id": "apt-108",
        "token": "T-014",
        "appointment_time": "08:45 AM",
        "date": "2026-08-29",
        "patient_id": "P-1021",
        "patient_name": "Ford Prefect",
        "phone": "+1 (555) 881-2205",
        "doctor_id": "doc-5",
        "doctor_name": "Dr. Lisa Wong",
        "department": "Dermatology",
        "room": "Suite 108",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:245 AM",
        "diagnosis": "Routine consultation for Acute Gastritis Evaluation. Vitals stable.",
        "fee": 130,
        "billing_status": "pending"
    },
    {
        "id": "apt-109",
        "token": "T-015",
        "appointment_time": "08:50 AM",
        "date": "2026-08-29",
        "patient_id": "P-1022",
        "patient_name": "Trillian McMillan",
        "phone": "+1 (555) 881-2206",
        "doctor_id": "doc-6",
        "doctor_name": "Dr. Gregory House",
        "department": "Diagnostic Medicine",
        "room": "Suite 500",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "08:250 AM",
        "diagnosis": "Routine consultation for Allergy Skin Prick Testing. Vitals stable.",
        "fee": 135,
        "billing_status": "paid"
    },
    {
        "id": "apt-110",
        "token": "T-016",
        "appointment_time": "09:00 AM",
        "date": "2026-08-29",
        "patient_id": "P-1023",
        "patient_name": "Marty McFly",
        "phone": "+1 (555) 881-2207",
        "doctor_id": "doc-7",
        "doctor_name": "Dr. James Wilson",
        "department": "Oncology",
        "room": "Suite 305",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:200 AM",
        "diagnosis": "Routine consultation for Ankle Sprain & Ultrasound. Vitals stable.",
        "fee": 140,
        "billing_status": "paid"
    },
    {
        "id": "apt-111",
        "token": "T-017",
        "appointment_time": "09:05 AM",
        "date": "2026-08-29",
        "patient_id": "P-1024",
        "patient_name": "Doc Brown",
        "phone": "+1 (555) 881-2208",
        "doctor_id": "doc-8",
        "doctor_name": "Dr. Allison Cameron",
        "department": "Immunology & Allergy",
        "room": "Suite 210",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:205 AM",
        "diagnosis": "Routine consultation for Cardiovascular Holter Review. Vitals stable.",
        "fee": 145,
        "billing_status": "paid"
    },
    {
        "id": "apt-112",
        "token": "T-018",
        "appointment_time": "09:10 AM",
        "date": "2026-08-29",
        "patient_id": "P-1025",
        "patient_name": "Diana Prince",
        "phone": "+1 (555) 881-2209",
        "doctor_id": "doc-9",
        "doctor_name": "Dr. Robert Chase",
        "department": "Intensive Care & Surgery",
        "room": "Suite 315",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:210 AM",
        "diagnosis": "Routine consultation for Annual Well-Woman Exam. Vitals stable.",
        "fee": 150,
        "billing_status": "pending"
    },
    {
        "id": "apt-113",
        "token": "T-019",
        "appointment_time": "09:20 AM",
        "date": "2026-08-29",
        "patient_id": "P-1026",
        "patient_name": "Bruce Wayne",
        "phone": "+1 (555) 881-2210",
        "doctor_id": "doc-10",
        "doctor_name": "Dr. Eric Foreman",
        "department": "Neurology",
        "room": "Suite 402",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:220 AM",
        "diagnosis": "Routine consultation for Rotator Cuff Tendinitis. Vitals stable.",
        "fee": 155,
        "billing_status": "paid"
    },
    {
        "id": "apt-114",
        "token": "T-020",
        "appointment_time": "09:25 AM",
        "date": "2026-08-29",
        "patient_id": "P-1027",
        "patient_name": "Clark Kent",
        "phone": "+1 (555) 881-2211",
        "doctor_id": "doc-11",
        "doctor_name": "Dr. Chris Taub",
        "department": "Plastic & Reconstructive Surgery",
        "room": "Suite 112",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:225 AM",
        "diagnosis": "Routine consultation for Annual Executive Physical. Vitals stable.",
        "fee": 160,
        "billing_status": "paid"
    },
    {
        "id": "apt-115",
        "token": "T-021",
        "appointment_time": "09:30 AM",
        "date": "2026-08-29",
        "patient_id": "P-1028",
        "patient_name": "Lois Lane",
        "phone": "+1 (555) 881-2212",
        "doctor_id": "doc-12",
        "doctor_name": "Dr. Remy Hadley",
        "department": "Internal Medicine",
        "room": "Suite 204",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:230 AM",
        "diagnosis": "Routine consultation for Migraine Prophylaxis Review. Vitals stable.",
        "fee": 165,
        "billing_status": "paid"
    },
    {
        "id": "apt-116",
        "token": "T-022",
        "appointment_time": "09:35 AM",
        "date": "2026-08-29",
        "patient_id": "P-1029",
        "patient_name": "Barry Allen",
        "phone": "+1 (555) 881-2213",
        "doctor_id": "doc-13",
        "doctor_name": "Dr. Lawrence Kutner",
        "department": "Sports Medicine",
        "room": "Suite 415",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:235 AM",
        "diagnosis": "Routine consultation for Metabolic Syndrome Screening. Vitals stable.",
        "fee": 170,
        "billing_status": "pending"
    },
    {
        "id": "apt-117",
        "token": "T-023",
        "appointment_time": "09:40 AM",
        "date": "2026-08-29",
        "patient_id": "P-1030",
        "patient_name": "Hal Jordan",
        "phone": "+1 (555) 881-2214",
        "doctor_id": "doc-14",
        "doctor_name": "Dr. Martha Masters",
        "department": "General Practice",
        "room": "Suite 102",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:240 AM",
        "diagnosis": "Routine consultation for Visual Field & Ocular Pressure. Vitals stable.",
        "fee": 175,
        "billing_status": "paid"
    },
    {
        "id": "apt-118",
        "token": "T-024",
        "appointment_time": "09:50 AM",
        "date": "2026-08-29",
        "patient_id": "P-1031",
        "patient_name": "Oliver Queen",
        "phone": "+1 (555) 881-2215",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:250 AM",
        "diagnosis": "Routine consultation for Shoulder Impingement Therapy. Vitals stable.",
        "fee": 110,
        "billing_status": "paid"
    },
    {
        "id": "apt-119",
        "token": "T-025",
        "appointment_time": "09:55 AM",
        "date": "2026-08-29",
        "patient_id": "P-1032",
        "patient_name": "Dinah Lance",
        "phone": "+1 (555) 881-2216",
        "doctor_id": "doc-2",
        "doctor_name": "Dr. Alex Rivera",
        "department": "Pediatrics",
        "room": "Suite 105",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "09:255 AM",
        "diagnosis": "Routine consultation for Vocal Cord Laryngoscopy Followup. Vitals stable.",
        "fee": 115,
        "billing_status": "paid"
    },
    {
        "id": "apt-120",
        "token": "T-026",
        "appointment_time": "10:00 AM",
        "date": "2026-08-29",
        "patient_id": "P-1033",
        "patient_name": "Tony Stark",
        "phone": "+1 (555) 881-2217",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:300 AM",
        "diagnosis": "Routine consultation for Cardiac Stent Routine Review. Vitals stable.",
        "fee": 120,
        "billing_status": "pending"
    },
    {
        "id": "apt-121",
        "token": "T-027",
        "appointment_time": "10:05 AM",
        "date": "2026-08-29",
        "patient_id": "P-1034",
        "patient_name": "Pepper Potts",
        "phone": "+1 (555) 881-2218",
        "doctor_id": "doc-4",
        "doctor_name": "Dr. Michael Vance",
        "department": "Orthopedics",
        "room": "Suite 410",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:305 AM",
        "diagnosis": "Routine consultation for Preventive Wellness Screening. Vitals stable.",
        "fee": 125,
        "billing_status": "paid"
    },
    {
        "id": "apt-122",
        "token": "T-028",
        "appointment_time": "10:10 AM",
        "date": "2026-08-29",
        "patient_id": "P-1035",
        "patient_name": "Steve Rogers",
        "phone": "+1 (555) 881-2219",
        "doctor_id": "doc-5",
        "doctor_name": "Dr. Lisa Wong",
        "department": "Dermatology",
        "room": "Suite 108",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:310 AM",
        "diagnosis": "Routine consultation for Geriatric Joint Mobility Check. Vitals stable.",
        "fee": 130,
        "billing_status": "paid"
    },
    {
        "id": "apt-123",
        "token": "T-029",
        "appointment_time": "10:15 AM",
        "date": "2026-08-29",
        "patient_id": "P-1036",
        "patient_name": "Natasha Romanoff",
        "phone": "+1 (555) 881-2220",
        "doctor_id": "doc-6",
        "doctor_name": "Dr. Gregory House",
        "department": "Diagnostic Medicine",
        "room": "Suite 500",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:315 AM",
        "diagnosis": "Routine consultation for Physical Therapy Clearance. Vitals stable.",
        "fee": 135,
        "billing_status": "paid"
    },
    {
        "id": "apt-124",
        "token": "T-030",
        "appointment_time": "10:18 AM",
        "date": "2026-08-29",
        "patient_id": "P-1037",
        "patient_name": "Bruce Banner",
        "phone": "+1 (555) 881-2221",
        "doctor_id": "doc-7",
        "doctor_name": "Dr. James Wilson",
        "department": "Oncology",
        "room": "Suite 305",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:318 AM",
        "diagnosis": "Routine consultation for Endocrine Stress Panel. Vitals stable.",
        "fee": 140,
        "billing_status": "pending"
    },
    {
        "id": "apt-125",
        "token": "T-031",
        "appointment_time": "10:20 AM",
        "date": "2026-08-29",
        "patient_id": "P-1038",
        "patient_name": "Wanda Maximoff",
        "phone": "+1 (555) 881-2222",
        "doctor_id": "doc-8",
        "doctor_name": "Dr. Allison Cameron",
        "department": "Immunology & Allergy",
        "room": "Suite 210",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:320 AM",
        "diagnosis": "Routine consultation for Neurological EEG Consultation. Vitals stable.",
        "fee": 145,
        "billing_status": "paid"
    },
    {
        "id": "apt-126",
        "token": "T-032",
        "appointment_time": "10:22 AM",
        "date": "2026-08-29",
        "patient_id": "P-1039",
        "patient_name": "Stephen Strange",
        "phone": "+1 (555) 881-2223",
        "doctor_id": "doc-9",
        "doctor_name": "Dr. Robert Chase",
        "department": "Intensive Care & Surgery",
        "room": "Suite 315",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:322 AM",
        "diagnosis": "Routine consultation for Bilateral Carpal Tunnel Review. Vitals stable.",
        "fee": 150,
        "billing_status": "paid"
    },
    {
        "id": "apt-127",
        "token": "T-033",
        "appointment_time": "10:25 AM",
        "date": "2026-08-29",
        "patient_id": "P-1040",
        "patient_name": "Peter Parker",
        "phone": "+1 (555) 881-2224",
        "doctor_id": "doc-10",
        "doctor_name": "Dr. Eric Foreman",
        "department": "Neurology",
        "room": "Suite 402",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:325 AM",
        "diagnosis": "Routine consultation for Sports Physical & ECG. Vitals stable.",
        "fee": 155,
        "billing_status": "paid"
    },
    {
        "id": "apt-128",
        "token": "T-034",
        "appointment_time": "10:28 AM",
        "date": "2026-08-29",
        "patient_id": "P-1041",
        "patient_name": "Miles Morales",
        "phone": "+1 (555) 881-2225",
        "doctor_id": "doc-11",
        "doctor_name": "Dr. Chris Taub",
        "department": "Plastic & Reconstructive Surgery",
        "room": "Suite 112",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:328 AM",
        "diagnosis": "Routine consultation for Pediatric Adolescent Checkup. Vitals stable.",
        "fee": 160,
        "billing_status": "pending"
    },
    {
        "id": "apt-129",
        "token": "T-035",
        "appointment_time": "10:30 AM",
        "date": "2026-08-29",
        "patient_id": "P-1042",
        "patient_name": "Gwen Stacy",
        "phone": "+1 (555) 881-2226",
        "doctor_id": "doc-12",
        "doctor_name": "Dr. Remy Hadley",
        "department": "Internal Medicine",
        "room": "Suite 204",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:330 AM",
        "diagnosis": "Routine consultation for Audiology Screening. Vitals stable.",
        "fee": 165,
        "billing_status": "paid"
    },
    {
        "id": "apt-130",
        "token": "T-036",
        "appointment_time": "10:32 AM",
        "date": "2026-08-29",
        "patient_id": "P-1001",
        "patient_name": "Robert Fox",
        "phone": "+1 (555) 432-8901",
        "doctor_id": "doc-13",
        "doctor_name": "Dr. Lawrence Kutner",
        "department": "Sports Medicine",
        "room": "Suite 415",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:332 AM",
        "diagnosis": "Routine consultation for Hypertension Stage 2. Vitals stable.",
        "fee": 170,
        "billing_status": "paid"
    },
    {
        "id": "apt-131",
        "token": "T-037",
        "appointment_time": "10:35 AM",
        "date": "2026-08-29",
        "patient_id": "P-1002",
        "patient_name": "Sophia Martinez",
        "phone": "+1 (555) 789-0123",
        "doctor_id": "doc-14",
        "doctor_name": "Dr. Martha Masters",
        "department": "General Practice",
        "room": "Suite 102",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:335 AM",
        "diagnosis": "Routine consultation for Chronic Migraine. Vitals stable.",
        "fee": 175,
        "billing_status": "paid"
    },
    {
        "id": "apt-132",
        "token": "T-038",
        "appointment_time": "10:38 AM",
        "date": "2026-08-29",
        "patient_id": "P-1003",
        "patient_name": "Marcus Vance",
        "phone": "+1 (555) 321-6549",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:338 AM",
        "diagnosis": "Routine consultation for Arrhythmia Investigation. Vitals stable.",
        "fee": 110,
        "billing_status": "pending"
    },
    {
        "id": "apt-133",
        "token": "T-039",
        "appointment_time": "10:40 AM",
        "date": "2026-08-29",
        "patient_id": "P-1004",
        "patient_name": "Emma Watson",
        "phone": "+1 (555) 876-5432",
        "doctor_id": "doc-2",
        "doctor_name": "Dr. Alex Rivera",
        "department": "Pediatrics",
        "room": "Suite 105",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:340 AM",
        "diagnosis": "Routine consultation for Routine Pediatric Check & MMR Booster. Vitals stable.",
        "fee": 115,
        "billing_status": "paid"
    },
    {
        "id": "apt-134",
        "token": "T-040",
        "appointment_time": "10:45 AM",
        "date": "2026-08-29",
        "patient_id": "P-1005",
        "patient_name": "David Miller",
        "phone": "+1 (555) 654-9870",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Consultation & Follow-up",
        "status": "completed",
        "completed_time": "10:345 AM",
        "diagnosis": "Routine consultation for Right Meniscus Tear. Vitals stable.",
        "fee": 120,
        "billing_status": "paid"
    },
    {
        "id": "apt-135",
        "token": "T-044",
        "appointment_time": "10:30 AM",
        "date": "2026-08-29",
        "patient_id": "P-1003",
        "patient_name": "Marcus Vance",
        "phone": "+1 (555) 321-6549",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Cardiology ECG & Consult",
        "status": "in_consultation",
        "diagnosis": "Undergoing 12-lead ECG review for mild exertional palpitations.",
        "fee": 150,
        "billing_status": "pending"
    },
    {
        "id": "apt-136",
        "token": "T-045",
        "appointment_time": "11:00 AM",
        "date": "2026-08-29",
        "patient_id": "P-1004",
        "patient_name": "Emma Watson",
        "phone": "+1 (555) 876-5432",
        "doctor_id": "doc-2",
        "doctor_name": "Dr. Alex Rivera",
        "department": "Pediatrics",
        "room": "Suite 105",
        "visit_type": "Pediatric Immunization (MMR)",
        "status": "waiting",
        "fee": 80,
        "billing_status": "pending"
    },
    {
        "id": "apt-137",
        "token": "T-046",
        "appointment_time": "11:30 AM",
        "date": "2026-08-29",
        "patient_id": "P-1005",
        "patient_name": "David Miller",
        "phone": "+1 (555) 654-9870",
        "doctor_id": "doc-4",
        "doctor_name": "Dr. Michael Vance",
        "department": "Orthopedics",
        "room": "Suite 410",
        "visit_type": "Knee Meniscus Evaluation",
        "status": "waiting",
        "fee": 140,
        "billing_status": "pending"
    },
    {
        "id": "apt-138",
        "token": "T-047",
        "appointment_time": "11:45 AM",
        "date": "2026-08-29",
        "patient_id": "P-1013",
        "patient_name": "Lucas Scott",
        "phone": "+1 (555) 123-9988",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Sports Concussion Baseline Assessment",
        "status": "waiting",
        "fee": 110,
        "billing_status": "pending"
    },
    {
        "id": "apt-139",
        "token": "T-048",
        "appointment_time": "01:15 PM",
        "date": "2026-08-29",
        "patient_id": "P-1006",
        "patient_name": "Clara Oswald",
        "phone": "+1 (555) 987-1234",
        "doctor_id": "doc-3",
        "doctor_name": "Dr. Emily Chen",
        "department": "General Medicine",
        "room": "Suite 201",
        "visit_type": "Hypothyroidism Blood Panel Follow-up",
        "status": "arrived",
        "fee": 130,
        "billing_status": "pending"
    },
    {
        "id": "apt-140",
        "token": "T-049",
        "appointment_time": "01:45 PM",
        "date": "2026-08-29",
        "patient_id": "P-1008",
        "patient_name": "James Wilson",
        "phone": "+1 (555) 234-9081",
        "doctor_id": "doc-4",
        "doctor_name": "Dr. Michael Vance",
        "department": "Orthopedics",
        "room": "Suite 410",
        "visit_type": "Cast Removal & Wrist X-Ray",
        "status": "arrived",
        "fee": 175,
        "billing_status": "pending"
    },
    {
        "id": "apt-141",
        "token": "T-050",
        "appointment_time": "02:30 PM",
        "date": "2026-08-29",
        "patient_id": "P-1011",
        "patient_name": "Jonathan Archer",
        "phone": "+1 (555) 882-9910",
        "doctor_id": "doc-1",
        "doctor_name": "Dr. Sarah Jenkins",
        "department": "Cardiology",
        "room": "Suite 302",
        "visit_type": "Lipid Panel & Statin Optimization",
        "status": "scheduled",
        "fee": 140,
        "billing_status": "unbilled"
    },
    {
        "id": "apt-142",
        "token": "T-051",
        "appointment_time": "03:15 PM",
        "date": "2026-08-29",
        "patient_id": "P-1016",
        "patient_name": "Tariq Mansoor",
        "phone": "+1 (555) 772-0044",
        "doctor_id": "doc-5",
        "doctor_name": "Dr. Lisa Wong",
        "department": "Dermatology",
        "room": "Suite 108",
        "visit_type": "Severe Eczema Topical Protocol",
        "status": "scheduled",
        "fee": 160,
        "billing_status": "unbilled"
    }
]

CLINIC_INVOICES = [
    {
        "id": "inv-801",
        "invoice_number": "INV-2026-0801",
        "date": "2026-08-29",
        "patient_id": "P-1015",
        "patient_name": "Eleanor Vance",
        "doctor_name": "Dr. Michael Vance",
        "services": [
            {
                "name": "Orthopedic Specialist Consult",
                "amount": 120
            },
            {
                "name": "Knee Joint Cortisone Injection",
                "amount": 60
            }
        ],
        "total_amount": 180,
        "status": "paid",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-802",
        "invoice_number": "INV-2026-0802",
        "date": "2026-08-29",
        "patient_id": "P-1001",
        "patient_name": "Robert Fox",
        "doctor_name": "Dr. Sarah Jenkins",
        "services": [
            {
                "name": "Cardiology Followup Consult",
                "amount": 120
            }
        ],
        "total_amount": 120,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-803",
        "invoice_number": "INV-2026-0803",
        "date": "2026-08-29",
        "patient_id": "P-1002",
        "patient_name": "Sophia Martinez",
        "doctor_name": "Dr. Emily Chen",
        "services": [
            {
                "name": "Acute Migraine Consultation",
                "amount": 95
            }
        ],
        "total_amount": 95,
        "status": "pending",
        "payment_method": "Pending Settlement"
    },
    {
        "id": "inv-804",
        "invoice_number": "INV-2026-0804",
        "date": "2026-08-29",
        "patient_id": "P-1003",
        "patient_name": "Marcus Vance",
        "doctor_name": "Dr. Sarah Jenkins",
        "services": [
            {
                "name": "Cardiology Consult",
                "amount": 100
            },
            {
                "name": "12-Lead Diagnostic ECG",
                "amount": 50
            }
        ],
        "total_amount": 150,
        "status": "pending",
        "payment_method": "Pending Settlement"
    },
    {
        "id": "inv-805",
        "invoice_number": "INV-2026-0799",
        "date": "2026-08-28",
        "patient_id": "P-1008",
        "patient_name": "James Wilson",
        "doctor_name": "Dr. Michael Vance",
        "services": [
            {
                "name": "Cast Inspection & X-Ray Limb",
                "amount": 210
            }
        ],
        "total_amount": 210,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-806",
        "invoice_number": "INV-2026-0795",
        "date": "2026-08-27",
        "patient_id": "P-1005",
        "patient_name": "David Miller",
        "doctor_name": "Dr. Michael Vance",
        "services": [
            {
                "name": "Knee Ortho Consultation",
                "amount": 140
            }
        ],
        "total_amount": 140,
        "status": "overdue",
        "payment_method": "Unsettled"
    },
    {
        "id": "inv-807",
        "invoice_number": "INV-2026-0807",
        "date": "2026-08-29",
        "patient_id": "P-1017",
        "patient_name": "Sarah Connor",
        "doctor_name": "Dr. Sarah Jenkins",
        "services": [
            {
                "name": "Cardiology Consultation",
                "amount": 110
            }
        ],
        "total_amount": 110,
        "status": "pending",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-808",
        "invoice_number": "INV-2026-0808",
        "date": "2026-08-29",
        "patient_id": "P-1018",
        "patient_name": "John Matrix",
        "doctor_name": "Dr. Alex Rivera",
        "services": [
            {
                "name": "Pediatrics Consultation",
                "amount": 115
            }
        ],
        "total_amount": 115,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-809",
        "invoice_number": "INV-2026-0809",
        "date": "2026-08-29",
        "patient_id": "P-1019",
        "patient_name": "Ellen Ripley",
        "doctor_name": "Dr. Emily Chen",
        "services": [
            {
                "name": "General Medicine Consultation",
                "amount": 120
            }
        ],
        "total_amount": 120,
        "status": "paid",
        "payment_method": "UPI / Digital"
    },
    {
        "id": "inv-810",
        "invoice_number": "INV-2026-0810",
        "date": "2026-08-29",
        "patient_id": "P-1020",
        "patient_name": "Arthur Dent",
        "doctor_name": "Dr. Michael Vance",
        "services": [
            {
                "name": "Orthopedics Consultation",
                "amount": 125
            }
        ],
        "total_amount": 125,
        "status": "paid",
        "payment_method": "Cash"
    },
    {
        "id": "inv-811",
        "invoice_number": "INV-2026-0811",
        "date": "2026-08-29",
        "patient_id": "P-1021",
        "patient_name": "Ford Prefect",
        "doctor_name": "Dr. Lisa Wong",
        "services": [
            {
                "name": "Dermatology Consultation",
                "amount": 130
            }
        ],
        "total_amount": 130,
        "status": "paid",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-812",
        "invoice_number": "INV-2026-0812",
        "date": "2026-08-29",
        "patient_id": "P-1022",
        "patient_name": "Trillian McMillan",
        "doctor_name": "Dr. Gregory House",
        "services": [
            {
                "name": "Diagnostic Medicine Consultation",
                "amount": 135
            }
        ],
        "total_amount": 135,
        "status": "pending",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-813",
        "invoice_number": "INV-2026-0813",
        "date": "2026-08-29",
        "patient_id": "P-1023",
        "patient_name": "Marty McFly",
        "doctor_name": "Dr. James Wilson",
        "services": [
            {
                "name": "Oncology Consultation",
                "amount": 140
            }
        ],
        "total_amount": 140,
        "status": "paid",
        "payment_method": "UPI / Digital"
    },
    {
        "id": "inv-814",
        "invoice_number": "INV-2026-0814",
        "date": "2026-08-29",
        "patient_id": "P-1024",
        "patient_name": "Doc Brown",
        "doctor_name": "Dr. Allison Cameron",
        "services": [
            {
                "name": "Immunology & Allergy Consultation",
                "amount": 145
            }
        ],
        "total_amount": 145,
        "status": "paid",
        "payment_method": "Cash"
    },
    {
        "id": "inv-815",
        "invoice_number": "INV-2026-0815",
        "date": "2026-08-29",
        "patient_id": "P-1025",
        "patient_name": "Diana Prince",
        "doctor_name": "Dr. Robert Chase",
        "services": [
            {
                "name": "Intensive Care & Surgery Consultation",
                "amount": 150
            }
        ],
        "total_amount": 150,
        "status": "paid",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-816",
        "invoice_number": "INV-2026-0816",
        "date": "2026-08-29",
        "patient_id": "P-1026",
        "patient_name": "Bruce Wayne",
        "doctor_name": "Dr. Eric Foreman",
        "services": [
            {
                "name": "Neurology Consultation",
                "amount": 155
            }
        ],
        "total_amount": 155,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-817",
        "invoice_number": "INV-2026-0817",
        "date": "2026-08-29",
        "patient_id": "P-1027",
        "patient_name": "Clark Kent",
        "doctor_name": "Dr. Chris Taub",
        "services": [
            {
                "name": "Plastic & Reconstructive Surgery Consultation",
                "amount": 160
            }
        ],
        "total_amount": 160,
        "status": "pending",
        "payment_method": "UPI / Digital"
    },
    {
        "id": "inv-818",
        "invoice_number": "INV-2026-0818",
        "date": "2026-08-29",
        "patient_id": "P-1028",
        "patient_name": "Lois Lane",
        "doctor_name": "Dr. Remy Hadley",
        "services": [
            {
                "name": "Internal Medicine Consultation",
                "amount": 165
            }
        ],
        "total_amount": 165,
        "status": "paid",
        "payment_method": "Cash"
    },
    {
        "id": "inv-819",
        "invoice_number": "INV-2026-0819",
        "date": "2026-08-29",
        "patient_id": "P-1029",
        "patient_name": "Barry Allen",
        "doctor_name": "Dr. Lawrence Kutner",
        "services": [
            {
                "name": "Sports Medicine Consultation",
                "amount": 170
            }
        ],
        "total_amount": 170,
        "status": "paid",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-820",
        "invoice_number": "INV-2026-0820",
        "date": "2026-08-29",
        "patient_id": "P-1030",
        "patient_name": "Hal Jordan",
        "doctor_name": "Dr. Martha Masters",
        "services": [
            {
                "name": "General Practice Consultation",
                "amount": 175
            }
        ],
        "total_amount": 175,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-821",
        "invoice_number": "INV-2026-0821",
        "date": "2026-08-29",
        "patient_id": "P-1031",
        "patient_name": "Oliver Queen",
        "doctor_name": "Dr. Sarah Jenkins",
        "services": [
            {
                "name": "Cardiology Consultation",
                "amount": 110
            }
        ],
        "total_amount": 110,
        "status": "paid",
        "payment_method": "UPI / Digital"
    },
    {
        "id": "inv-822",
        "invoice_number": "INV-2026-0822",
        "date": "2026-08-29",
        "patient_id": "P-1032",
        "patient_name": "Dinah Lance",
        "doctor_name": "Dr. Alex Rivera",
        "services": [
            {
                "name": "Pediatrics Consultation",
                "amount": 115
            }
        ],
        "total_amount": 115,
        "status": "pending",
        "payment_method": "Cash"
    },
    {
        "id": "inv-823",
        "invoice_number": "INV-2026-0823",
        "date": "2026-08-29",
        "patient_id": "P-1033",
        "patient_name": "Tony Stark",
        "doctor_name": "Dr. Emily Chen",
        "services": [
            {
                "name": "General Medicine Consultation",
                "amount": 120
            }
        ],
        "total_amount": 120,
        "status": "paid",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-824",
        "invoice_number": "INV-2026-0824",
        "date": "2026-08-29",
        "patient_id": "P-1034",
        "patient_name": "Pepper Potts",
        "doctor_name": "Dr. Michael Vance",
        "services": [
            {
                "name": "Orthopedics Consultation",
                "amount": 125
            }
        ],
        "total_amount": 125,
        "status": "paid",
        "payment_method": "Insurance"
    },
    {
        "id": "inv-825",
        "invoice_number": "INV-2026-0825",
        "date": "2026-08-29",
        "patient_id": "P-1035",
        "patient_name": "Steve Rogers",
        "doctor_name": "Dr. Lisa Wong",
        "services": [
            {
                "name": "Dermatology Consultation",
                "amount": 130
            }
        ],
        "total_amount": 130,
        "status": "paid",
        "payment_method": "UPI / Digital"
    },
    {
        "id": "inv-826",
        "invoice_number": "INV-2026-0826",
        "date": "2026-08-29",
        "patient_id": "P-1036",
        "patient_name": "Natasha Romanoff",
        "doctor_name": "Dr. Gregory House",
        "services": [
            {
                "name": "Diagnostic Medicine Consultation",
                "amount": 135
            }
        ],
        "total_amount": 135,
        "status": "paid",
        "payment_method": "Cash"
    },
    {
        "id": "inv-827",
        "invoice_number": "INV-2026-0827",
        "date": "2026-08-29",
        "patient_id": "P-1037",
        "patient_name": "Bruce Banner",
        "doctor_name": "Dr. James Wilson",
        "services": [
            {
                "name": "Oncology Consultation",
                "amount": 140
            }
        ],
        "total_amount": 140,
        "status": "pending",
        "payment_method": "Credit Card"
    },
    {
        "id": "inv-828",
        "invoice_number": "INV-2026-0828",
        "date": "2026-08-29",
        "patient_id": "P-1038",
        "patient_name": "Wanda Maximoff",
        "doctor_name": "Dr. Allison Cameron",
        "services": [
            {
                "name": "Immunology & Allergy Consultation",
                "amount": 145
            }
        ],
        "total_amount": 145,
        "status": "paid",
        "payment_method": "Insurance"
    }
]

MONTHLY_FINANCIAL_REPORT = {
    "clinic_name": "PulseClinic Healthcare Center",
    "period": "August 2026 (Month-to-Date)",
    "generated_on": "2026-08-29",
    "currency": "USD ($)",
    "summary": {
        "gross_revenue": 32450,
        "total_consultations": 248,
        "average_ticket": 130.85,
        "paid_amount": 29240,
        "pending_receivables": 3210,
        "collection_rate_percent": 90.1
    },
    "breakdown_by_category": [
        {
            "category": "Specialist Physician Consultations",
            "revenue": 19800,
            "percentage": 61.0,
            "patient_count": 165
        },
        {
            "category": "Laboratory & Diagnostic Tests (ECG, Blood, Imaging)",
            "revenue": 8400,
            "percentage": 25.9,
            "patient_count": 112
        },
        {
            "category": "Outpatient Procedures & Minor Surgery",
            "revenue": 4250,
            "percentage": 13.1,
            "patient_count": 38
        }
    ],
    "breakdown_by_doctor": [
        {
            "doctor_name": "Dr. Sarah Jenkins",
            "department": "Cardiology",
            "appointments": 72,
            "revenue_generated": 10450,
            "top_procedure": "Echocardiogram & Cardiac Consult"
        },
        {
            "doctor_name": "Dr. Michael Vance",
            "department": "Orthopedics",
            "appointments": 58,
            "revenue_generated": 9200,
            "top_procedure": "Joint Injections & Fracture Care"
        },
        {
            "doctor_name": "Dr. Emily Chen",
            "department": "General Medicine",
            "appointments": 86,
            "revenue_generated": 7800,
            "top_procedure": "Preventative Checkups & Chronic Care"
        },
        {
            "doctor_name": "Dr. Alex Rivera",
            "department": "Pediatrics",
            "appointments": 44,
            "revenue_generated": 5000,
            "top_procedure": "Vaccinations & Wellness Exams"
        }
    ],
    "payment_methods": [
        {
            "method": "Insurance Direct Claims",
            "amount": 18450,
            "share": "56.8%"
        },
        {
            "method": "Credit / Debit Cards",
            "amount": 9800,
            "share": "30.2%"
        },
        {
            "method": "Digital Payments / UPI",
            "amount": 2600,
            "share": "8.0%"
        },
        {
            "method": "Cash Payments",
            "amount": 1600,
            "share": "5.0%"
        }
    ]
}

MONTHLY_EARNINGS_DATA = {
    "month": "August 2026",
    "gross_revenue": 32450,
    "paid_revenue": 29240,
    "pending_receivables": 3210,
    "total_appointments_billed": 248,
    "average_ticket": 130.85,
    "collection_rate": "90.1%",
    "categories": [
        {
            "name": "Doctor Consultations",
            "amount": 19800,
            "share": "61.0%"
        },
        {
            "name": "Diagnostic & Lab Tests",
            "amount": 8400,
            "share": "25.9%"
        },
        {
            "name": "Minor Procedures & Injections",
            "amount": 4250,
            "share": "13.1%"
        }
    ],
    "doctor_contributions": [
        {
            "doctor": "Dr. Sarah Jenkins",
            "specialty": "Cardiology",
            "revenue": 10450,
            "patients": 72
        },
        {
            "doctor": "Dr. Michael Vance",
            "specialty": "Orthopedics",
            "revenue": 9200,
            "patients": 58
        },
        {
            "doctor": "Dr. Emily Chen",
            "specialty": "General Medicine",
            "revenue": 7800,
            "patients": 86
        },
        {
            "doctor": "Dr. Alex Rivera",
            "specialty": "Pediatrics",
            "revenue": 5000,
            "patients": 44
        }
    ],
    "payment_modes": [
        {
            "mode": "Insurance Claims",
            "amount": 18450
        },
        {
            "mode": "Credit / Debit Cards",
            "amount": 9800
        },
        {
            "mode": "Digital / UPI",
            "amount": 2600
        },
        {
            "mode": "Cash",
            "amount": 1600
        }
    ]
}
