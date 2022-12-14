# -*- coding: utf-8 -*-
from odoo import fields, models, _

class ResPartnerTrainer(models.Model):
    _inherit = "res.partner" #Heradar un modelo existente
    #                               Modelo relacionado, nombre tabla,         columna 1,      columna 2 relacion modelo secundario
    pokemon_ids = fields.Many2many('pokedex.pokemon')

    def evolve_pokemon(self):
        evolve_wizard_view = self.env.ref('pokedex.evolve_pokemon_wizard_form')
        return{
         'name': _('Evolve your pokemon'),
         'type': 'ir.actions.act_window',
         'view_mode': 'form',
         'res_model': 'pokemon.evolve.wizard',
         'views': [(evolve_wizard_view.id, 'form')],
         'view_id': evolve_wizard_view.id,
         'target': 'new',
         'context': {
            'default_trainer_id': self.id,
        },
        }
