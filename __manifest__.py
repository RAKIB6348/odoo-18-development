{
    'name': 'Hospital Management System',
    'version': '1.1.1',
    'summary': 'Manage hospital operations like patients, doctors, appointments, billing, and more.',
    'description': """
        Comprehensive Hospital Management System for Odoo 18.
        Features include patient registration, doctor management, appointments,
        prescriptions, invoicing, and reports.
    """,
    'category': 'Healthcare',
    'author': 'Fahim Hasan Rakib',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',

        'data/sequence.xml',
        'data/patient.tag.csv',

        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
