# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from pprint import pprint
# Loading DataSet
train_data = load_data('rasa_data.json')
# Config Backend using Sklearn and Spacy
trainer = Trainer(config.load("config_spacy.yaml"))

# Training Data
trainer.train(train_data)
# Returns the directory the model is stored in (Creat a folder to store model in)
model_directory = trainer.persist('./projects/')
from rasa_nlu.model import Metadata, Interpreter

interpreter = Interpreter.load(model_directory)

# Prediction of Intent
pprint(interpreter.parse(open('./csv/236173-ORD3402_304220180120213604-Page(3).csv', 'r').read()))


