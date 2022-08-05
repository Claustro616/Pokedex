# -*- coding: utf-8 -*-

from odoo import fields, models


class PokedexPokemon(models.Model):
    _inherit = ['image.mixin']
    _name = 'pokedex.pokemon'  # Modelo de odoo
    _order = 'sequence'

    # Como se llama en la tabla: pokedex_pokemon
    name = fields.Char()
    preevolution_id = fields.Many2one('pokedex.pokemon')
    evolution_ids = fields.Many2one('pokedex.pokemon', 'preevolution_id')
    sequence = fields.Integer()
    description = fields.Char()
    height = fields.Float()
    weight = fields.Float()
    type_ids = fields.Many2many('pokedex.pokemon.type')
    move_ids = fields.Many2many('pokedex.pokemon.move')
    color = fields.Integer(string='Color Index', default=0)


class PokedexPokemonMove(models.Model):
    _name = 'pokedex.pokemon.move'
    _inherit = ['image.mixin']

    name = fields.Char()
    description = fields.Char()
    power = fields.Char()
    type_ids = fields.Many2one('pokedex.pokemon.type')
