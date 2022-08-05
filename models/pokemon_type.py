# -*- coding: utf-8 -*-

from odoo import fields, models


class PokedexPokemonType(models.Model):
    _name = 'pokedex.pokemon.type'
    _inherit = ['image.mixin']

    name = fields.Char()
    description = fields.Char()
    color = fields.Integer()
