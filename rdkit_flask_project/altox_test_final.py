from rdkit import Chem
from rdkit.Chem import Draw

from flask import Flask, render_template
from io import BytesIO

import base64

def draw_smiles_in_b64(smiles):

    molecule = Chem.MolFromSmiles(smiles)

    molecule_image = Draw.MolToImage(molecule)

    byte_convert = BytesIO()
    molecule_image.save(byte_convert, format='PNG')
    molecule_image_data = byte_convert.getvalue()

    encoded_image = base64.b64encode(molecule_image_data).decode()

    base_64_image = "data:image/png;base64, {0}".format(encoded_image)

    return base_64_image


app = Flask(__name__)

@app.route('/drawMolecule/<smiles>')
def draw_molecule(smiles):

    return render_template('draw_molecule.html', smiles=smiles, value=draw_smiles_in_b64(smiles))

app.run()