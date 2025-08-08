from odoo import models, fields

class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    name = fields.Char('Name', required=True)
