customers = [
    {
        'Name': 'Κώστας Παπαδημητρίου',
        'Balance': 1.345,
        'Address': 'Καποδιστρίου 64'
    },
    {
        'Name': 'Γιώργος Παπαβασιλείου',
        'Balance': 10.000,
        'Address': 'Χατζηζωγίδου 23'
    }
]

tasks = [
    {
        'id': '1',
        'Name': 'Κώστας Παπαδημητρίου',
        'Description': 'Τοποθέτηση μαρμάρων 30μ',
        'Cost': '1200',
        'Completion_date': '5/5/2025'
    },
    {
        'id': '2',
        'Name': 'Γιώργος Αντωνίου',
        'Description': 'Τοποθέτηση πλακάκια 30 τ.μ',
        'Cost': '1000',
        'Completion_date': '2/5/2025'
    }
]

items = [
    {
        'Id': '1',
        'Brand': 'Kraft',
        'Description': 'Τρυπάνι Δυνατό',
        'Cost': 130,
        'Size': 'Large'
    },
    {
        'Id': '2',
        'Brand': 'FF Group',
        'Description': 'Γάντια Αντοχής',
        'Cost': 1.20,
        'Size': 'S'
    }
]

last_sales = [{
    'id': 1,
    'Document_code': 'ΤΔΑ-Α-000001',
    'Document_date': '01-01-2025',
    'Total_amount': 1240,
    'Net_value': 1000,
    'Vat_amount': 240
},
    {
    'id': 2,
    'Document_code': 'ΤΔΑ-Α-000002',
    'Document_date': '01-02-2025',
    'Total_amount': 124,
    'Net_value': 100,
    'Vat_amount': 24
}]

documents = [{
    'id': 1,
    'code': 'ΤΔΑ-Α-000001',
    'date': '01-01-2025',
    'customer': 'Τερζής Δημήτρης',
    'net_value': 1000,
    'vat_value': 240,
    'gross_value': 240
},
    {
    'id': 2,
    'code': 'ΤΔΑ-Α-000002',
    'date': '01-01-2025',
    'customer': 'Χατζηδημητρίου Κωνσταντίνος',
    'net_value': 100,
    'vat_value': 24,
    'gross_value': 24
}]
