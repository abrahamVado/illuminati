
from odoo import http, fields, api
from odoo.http import Response
from odoo.http import request
import json

class exampleClass( http.Controller ):
	@http.route('/web/update_order_webhook', type='http', csrf=False, auth="public")
	def update_order_webhook(self, **kwargs):
		results = request.env['illuminate'].search([])
		raw_data = results.read()
		return Response(json.dumps(raw_data),content_type='application/json;charset=utf-8',status=200)

	@http.route('/web/inserta', type='http', csrf=False, auth="public")
	def inserta(self, **kwargs):
		uno = request.env['illuminate'].create({ 'calle':'abraham' })
		request.env.cr.commit()
		return Response(json.dumps({ 'tst' : 'end' }), content_type='application/json;charset=utf-8', status=200)

	@http.route('/web/mapa', auth="public")
	def mapa(self, **kw):
		return http.request.render("illuminati.index")
