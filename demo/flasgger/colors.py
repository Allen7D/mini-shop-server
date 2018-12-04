# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/4.
"""
from flask import Flask, jsonify
from flasgger import Swagger, swag_from

__author__ = 'Alimazing'

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/colors/<palette>/')
def colors(palette):
	"""Example endpoint returning a list of colors by palette
	This is using docstrings for specifications.
	---
	parameters:
	  - name: palette
		in: path
		type: string
		enum: ['all', 'rgb', 'cmyk']
		required: true
		default: all
	definitions:
	  Palette:
		type: object
		properties:
		  palette_name:
			type: array
			items:
			  $ref: '#/definitions/Color'
	  Color:
		type: string
	responses:
	  200:
		description: A list of colors (may be filtered by palette)
		schema:
		  $ref: '#/definitions/Palette'
		examples:
		  rgb: ['red', 'green', 'blue']
	"""
	all_colors = {
		'cmyk': ['cian', 'magenta', 'yellow', 'black'],
		'rgb': ['red', 'green', 'blue']
	}
	if palette == 'all':
		result = all_colors
	else:
		result = {palette: all_colors.get(palette)}

	return jsonify(result)


@app.route('/colors/<palette>/')
@swag_from('colors.yml')
def colors(palette):
	pass


# 不用装饰器
@app.route('/colors/<palette>/')
def colors(palette):
	"""
	file: colors.yml
	"""


specs_dict = {
	"parameters": [
		{
			"name": "palette",
			"in": "path",
			"type": "string",
			"enum": [
				"all",
				"rgb",
				"cmyk"
			],
			"required": "true",
			"default": "all"
		}
	],
	"definitions": {
		"Palette": {
			"type": "object",
			"properties": {
				"palette_name": {
					"type": "array",
					"items": {
						"$ref": "#/definitions/Color"
					}
				}
			}
		},
		"Color": {
			"type": "string"
		}
	},
	"responses": {
		"200": {
			"description": "A list of colors (may be filtered by palette)",
			"schema": {
				"$ref": "#/definitions/Palette"
			},
			"examples": {
				"rgb": [
					"red",
					"green",
					"blue"
				]
			}
		}
	}
}


@app.route('/colors/<palette>/')
@swag_from(specs_dict)
def colors(palette):
	"""
	Example endpoint returning a list of colors by palette
	In this example the specification is taken from specs_dict
	"""
	pass


app.run(debug=True)
