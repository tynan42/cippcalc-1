from wtforms import Form, TextField, FloatField, validators
import math

class ErrorValidation(Form):
    design_condition = TextField('Design Condition', [
                        validators.Required(message='Missing required field.'),
                        validators.AnyOf(['Fully Deteriorated', 'Partially Deteriorated'], message='Invalid design condition. Please select from the list.')])
    location = TextField('Location', [
                        validators.Required(message='Missing required field.'),
                        validators.AnyOf(['Highway', 'Rail', 'Airport'], message='Invalid location.')])
    host_diameter = FloatField('Host Pipe Diameter', [
                        validators.Required(message='Missing required field.'),
                        validators.NumberRange(min=4, max=96, message='Host pipe diameter must be an integer between 4 and 96 inches.')])
    surface_to_invert = FloatField('Depth to Invert', [
                        validators.InputRequired(message='Missing required field.'),
                        validators.NumberRange(min=-1, max=50, message='Depth to invert be a number between 0 and 50 feet.')])
    gw_level = FloatField('Groundwater Depth', [
                        validators.NumberRange(min=0, max=100, message='Groundwater level out of range.'),
                        validators.Optional()])
    design_modulus = FloatField('Design Elastic Modulus', [
                        validators.NumberRange(min=1, max=9999999 message='Elastic modulus out of range.'),
                        validators.Optional()])
    design_flexural_strength = FloatField('Design Flexural Strength', [
                        validators.NumberRange(min=1, max=99999 message='Design flexural strength out of range.'),
                        validators.Optional()])
    safety_factor = FloatField('Safety Factor', [
                        validators.NumberRange(min=0.001, max=20 message='Safety factor out of range.'),
                        validators.Optional()])
    ret_factor = FloatField('Long Term Retention Factor', [
                        validators.NumberRange(min=1, max=100, message='Retention out of range.'),
                        validators.Optional()])
    ovality = FloatField('Ovality', [
                        validators.NumberRange(min=0, max=100, message='Ovality out of range.'),
                        validators.Optional()])
    enhancement_factor = FloatField('Enhancement Factor', [
                        validators.NumberRange(min=1, max=20, message='Enhancement Factor out of range.'),
                        validators.Optional()])
    soil_density = FloatField('Soil Density', [
                        validators.NumberRange(min=1, max=999 message='Soil density out of range.'),
                        validators.Optional()])
    poissons = FloatField('Poisson\'s Ratio', [
                        validators.NumberRange(min=0, max=0.5, message='Poisson\'s Ratio out of range.'),
                        validators.Optional()])
    soil_mod = FloatField('Modulus of Soil Reaction', [
                        validators.NumberRange(min=1, max=3000, message='Soil Modulus out of range.'),
                        validators.Optional()])
    n_host = FloatField('Host Manning\'s', [
                        validators.NumberRange(min=0.005, max=0.20, message='Host Manning\'s out of range.'),
                        validators.Optional()])
    n_liner = FloatField('Liner Manning\'s', [
                        validators.NumberRange(min=0.005, max=0.20, message='Liner Manning\'s out of range.'),
                        validators.Optional()])
    host_age = FloatField('Host Pipe Age', [
                        validators.NumberRange(min=0, max=500, message='Host Pipe Age out of range.'),
                        validators.Optional()])
class WarningValidation(Form):
    design_modulus = FloatField('Design Elastic Modulus', [
                        validators.NumberRange(min=250000, max=750000, message='''Design elastic modulus \
                        out of normal range. ASTM minimum value is 250,000 psi.'''),
                        validators.Optional()])
    design_flexural_strength = FloatField('Design Flexural Strength', [
                        validators.NumberRange(min=4500, max=25000, message='''Design flexural strength out \
                        of normal range. ASTM minimum value is 4,500 psi.'''),
                        validators.Optional()])
    ret_factor = FloatField('Rentention Factor', [
                        validators.NumberRange(min=45, max=80, message='Retention factor is typically between 50%% and 75%%.'),
                        validators.Optional()])
    ovality = FloatField('Ovality', [
                        validators.NumberRange(min=0, max=30, message='''Ovality indicates pipe may be \
                        partially collapsed. Verify that host pipe is a canditate for CIPP lining.'''),
                        validators.Optional()])
    enhancement_factor = FloatField('Enhancement Factor', [
                        validators.NumberRange(min=7, message='''ASTM recommends a minimum enhancement \
                        factor of 7.0'''),
                        validators.Optional()])
    soil_density = FloatField('Soil Density', [
                        validators.NumberRange(min=100, max=200, message='''Soil density beyond normal \
                        values. Ensure that the host pipe exists in Earth.'''),
                        validators.Optional()])
    soil_mod = FloatField('Modulus of Soil Reaction', [
                        validators.NumberRange(min=700, max=1500, message='''Soil Modulus beyond normal \
                        range'''),
                        validators.Optional()])                   