from __future__ import unicode_literals
import frappe

def before_request():
    if frappe.session.user == 'Guest' and frappe.local.request.path == '/files':
        frappe.local.response['type'] = 'redirect'
        frappe.local.response['location'] = 'https://your-redirect-url.com'
