{
    'name': 'Hospital Management System',
    'version': '1.1.1',
    'summary': 'Manage hospital operations like patients, doctors, appointments, billing, and more.',
    'description': """
        Comprehensive Hospital Management System for Odoo 17.
        Features include patient registration, doctor management, appointments,
        prescriptions, invoicing, and reports.
    """,
    'category': 'Healthcare',
    'author': 'Fahim Hasan Rakibr',
    'website': 'https://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',

        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
