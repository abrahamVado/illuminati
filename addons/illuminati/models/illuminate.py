# Copyright 2017-2018 Camptocamp - Abraham Gómez
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class illuminate(models.Model):
    _name = 'illuminate'
    _description = "tabla maestra para cargar luminarias"

    xap = fields.Integer( string = "xap" )
    cvecol = fields.Integer( string = "cvecol" )
    colonia = fields.Char( string = "colonia", size=250 )
    cvecalle = fields.Integer( string = "cvecalle" )
    calle = fields.Char( string = "calle", size=250 )
    tipocalle = fields.Char( string = "tipocalle", size=250 )
    referencia = fields.Char( string = "referencia", size=250 )
    tiposuelo = fields.Char( string = "tiposuelo", size=250 )
    nvcalle = fields.Char( string = "nvcalle", size=250 )
    ancalle = fields.Char( string = "ancalle", size=50 )
    modelo = fields.Char( string = "ancalle", size=50 )
    tecnologia = fields.Char( string = "tecnologia", size=50 )
    potencias = fields.Integer( string = "potencias" )
    marcas = fields.Char( string = "marcas", size=50 )
    perdidas_a = fields.Integer( string = "perdidas_a" )
    tension = fields.Char( string = "tension", size=50 )
    tipoposte = fields.Char( string = "tipoposte", size=50 )
    nlump = fields.Float( string = "nlump", digits=(6,4) )
    altoposte = fields.Float( string = "altoposte", digits=(6,4) )
    altolum = fields.Float( string = "altolum", digits=(6,4) )
    brazo = fields.Float( string = "brazo", digits=(6,4) )
    observa = fields.Char( string = "observa", size=250 )
    fechaalta = fields.Date( string = "fechaalta" )
    fcenso = fields.Date( string = "fcenso" )
    imagen = fields.Char( string = "imagen", size=250 )
    imagen = fields.Char( string = "imagen", size=250 )
    coordx = fields.Float( string = "coordx", digits=(4,7) )
    coordy = fields.Float( string = "coordy", digits=(4,7) )
    tiposerv = fields.Char( string = "tiposerv", size=50 )
    zonascfe = fields.Char( string = "zonascfe", size=50 )
    rpu = fields.Char( string = "rpu", size=250 )
    medidor = fields.Char( string = "medidor", size=50 )
    estados = fields.Char( string = "estados", size=50 )
    tcalle = fields.Integer( string = "tcalle" )
    nivelcalle = fields.Integer( string = "nivelcalle" )
    anchocalle = fields.Integer( string = "anchocalle" )
    perdidas_b = fields.Integer( string = "perdidas_b" )
